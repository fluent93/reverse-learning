from __future__ import annotations

import json
import re
from pathlib import Path

from .llm import AGENT_MODEL, call_agent
from .prompts import agent_prompt_path, load_system_prompt
from .repo import latest_file, repo_root, review_path_for_draft, version_num
from .state_io import load_state


def _extract_json_block(text: str) -> dict:
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    raw = fence.group(1) if fence else text.strip()
    return json.loads(raw)


def _extract_markdown_body(text: str) -> str:
    """Prefer full response; strip JSON fence if critic returned both."""
    if "```json" in text:
        parts = re.split(r"```json.*?```", text, flags=re.DOTALL)
        return "\n".join(p.strip() for p in parts if p.strip())
    return text.strip()


def run_drafter() -> list[Path]:
    root = repo_root()
    state = load_state()
    pid = state["pipeline_id"]
    brief = root / "briefs" / f"{pid}.md"
    if not brief.exists():
        raise FileNotFoundError(f"Brief not found: {brief}")

    system = load_system_prompt(agent_prompt_path("drafter"))
    user = (
        f"Produce drafts/v1.md from this brief.\n\n"
        f"--- BRIEF ---\n{brief.read_text(encoding='utf-8')}\n--- END BRIEF ---\n\n"
        "Output ONLY the complete markdown file content (including YAML frontmatter)."
    )
    out = call_agent(AGENT_MODEL["drafter"], system, user)
    dest = root / "drafts" / "v1.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out.strip() + "\n", encoding="utf-8")
    return [dest]


def run_critic() -> list[Path]:
    root = repo_root()
    draft = latest_file("drafts/v*.md", root)
    if not draft:
        raise FileNotFoundError("No draft to review")

    n = version_num(draft)
    rubric = (root / "agents" / "rubrics" / "rlf-core-rubric.md").read_text(encoding="utf-8")
    canon = "\n\n".join(
        (root / f).read_text(encoding="utf-8")
        for f in [
            "README.md",
            "Reverse Learning Framework One-Pager.md",
            "RLF-Checklist-AIOutputReview-v1.0.md",
        ]
        if (root / f).exists()
    )

    system = load_system_prompt(agent_prompt_path("critic"))
    user = (
        f"Review `{draft.relative_to(root)}` (version v{n}).\n\n"
        f"--- DRAFT ---\n{draft.read_text(encoding='utf-8')}\n--- END DRAFT ---\n\n"
        f"--- RUBRIC ---\n{rubric}\n--- END RUBRIC ---\n\n"
        f"--- CANON (excerpt) ---\n{canon[:120000]}\n--- END CANON ---\n\n"
        "Produce TWO outputs in your response:\n"
        "1) A JSON object conforming to agents/schema/review.schema.json in a ```json fence.\n"
        f"2) A markdown narrative for reviews/v{n}-review.md.\n"
        "The JSON must include total_score, recommendation, dimensions, top_issues."
    )
    out = call_agent(AGENT_MODEL["critic"], system, user)

    reviews = root / "reviews"
    reviews.mkdir(parents=True, exist_ok=True)

    json_path = reviews / f"v{n}-review.json"
    md_path = reviews / f"v{n}-review.md"

    # Parse JSON
    try:
        data = _extract_json_block(out)
        json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Critic did not return valid JSON: {e}") from e

    # Markdown: everything outside json fence, or generate stub
    md_body = _extract_markdown_body(out)
    if len(md_body) < 200:
        md_body = (
            f"# Critic Review — v{n}\n\n"
            f"**Total: {data.get('total_score', '?')}/100** — "
            f"**{data.get('recommendation', '?')}**\n\n"
            "See JSON for full dimension breakdown.\n"
        )
    md_path.write_text(md_body.strip() + "\n", encoding="utf-8")
    return [json_path, md_path]


def run_reviser() -> list[Path]:
    root = repo_root()
    draft = latest_file("drafts/v*.md", root)
    if not draft:
        raise FileNotFoundError("No draft to revise")
    n = version_num(draft)
    rjson = review_path_for_draft(draft)
    rmd = rjson.with_suffix(".md").name.replace("-review.json", "-review.md")
    rmd_path = rjson.parent / f"v{n}-review.md"

    system = load_system_prompt(agent_prompt_path("reviser"))
    user = (
        f"Produce drafts/v{n + 1}.md revising from v{n}.\n\n"
        f"--- DRAFT v{n} ---\n{draft.read_text(encoding='utf-8')}\n--- END ---\n\n"
        f"--- REVIEW JSON ---\n{rjson.read_text(encoding='utf-8')}\n--- END ---\n\n"
    )
    if rmd_path.exists():
        user += f"--- REVIEW MD ---\n{rmd_path.read_text(encoding='utf-8')}\n--- END ---\n\n"
    user += "Output ONLY the complete revised markdown file with Reviser Changelog at end."

    out = call_agent(AGENT_MODEL["reviser"], system, user)
    dest = root / "drafts" / f"v{n + 1}.md"
    dest.write_text(out.strip() + "\n", encoding="utf-8")
    return [dest]


def run_finalist() -> list[Path]:
    root = repo_root()
    state = load_state()
    target = state.get("target_version", "v1.0")
    draft = latest_file("drafts/v*.md", root)
    reviews_dir = root / "reviews"
    reviews = ""
    if reviews_dir.exists():
        reviews = "\n\n".join(
            p.read_text(encoding="utf-8") for p in sorted(reviews_dir.glob("*-review.json"))
        )

    system = load_system_prompt(agent_prompt_path("finalist"))
    user = (
        f"Produce final/{target}.md at repo root naming.\n\n"
        f"--- LATEST DRAFT ---\n{draft.read_text(encoding='utf-8') if draft else 'MISSING'}\n--- END ---\n\n"
        f"--- ALL REVIEWS JSON ---\n{reviews}\n--- END ---\n\n"
        f"state escalation_reason: {state.get('escalation_reason')}\n\n"
        "Output ONLY the complete final markdown file."
    )
    out = call_agent(AGENT_MODEL["finalist"], system, user)
    dest = root / "final" / f"{target}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out.strip() + "\n", encoding="utf-8")
    return [dest]


def run_verifier() -> list[Path]:
    root = repo_root()
    state = load_state()
    target = state.get("target_version", "v1.0")
    final = root / "final" / f"{target}.md"
    if not final.exists():
        raise FileNotFoundError(final)

    canon = "\n\n".join(
        (root / f).read_text(encoding="utf-8")
        for f in [
            "Reverse Learning Framework One-Pager.md",
            "RLF-Checklist-AIOutputReview-v1.0.md",
            "README.md",
        ]
        if (root / f).exists()
    )

    system = load_system_prompt(agent_prompt_path("verifier"))
    user = (
        f"Verify final/{target}.md. Write verification/{target}-check.md.\n\n"
        f"--- FINAL ---\n{final.read_text(encoding='utf-8')}\n--- END ---\n\n"
        f"--- CANON ---\n{canon[:100000]}\n--- END ---\n\n"
        "Output ONLY the verifier report markdown. Include **Verdict:** PASS, PASS_WITH_FLAGS, or FAIL."
    )
    out = call_agent(AGENT_MODEL["verifier"], system, user)
    dest = root / "verification" / f"{target}-check.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out.strip() + "\n", encoding="utf-8")
    return [dest]


def run_publisher() -> list[Path]:
    root = repo_root()
    state = load_state()
    target = state.get("target_version", "v1.0")
    final = root / "final" / f"{target}.md"
    ver = root / "verification" / f"{target}-check.md"

    system = load_system_prompt(agent_prompt_path("publisher"))
    user = (
        f"Create posts/brunch_{target}_ko.md and posts/linkedin_{target}_en.md\n\n"
        f"--- FINAL ---\n{final.read_text(encoding='utf-8')}\n--- END ---\n\n"
    )
    if ver.exists():
        user += f"--- VERIFICATION ---\n{ver.read_text(encoding='utf-8')}\n--- END ---\n\n"
    user += (
        "Output TWO markdown files separated by a line containing exactly:\n"
        "=== FILE: posts/brunch_...\n"
        "then content, then\n"
        "=== FILE: posts/linkedin_...\n"
    )
    out = call_agent(AGENT_MODEL["publisher"], system, user)

    posts = root / "posts"
    posts.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    chunks = re.split(r"=== FILE:\s*(\S+)\s*\n", out)
    if len(chunks) >= 3:
        for i in range(1, len(chunks), 2):
            rel = chunks[i].strip()
            body = chunks[i + 1].strip()
            path = root / rel.replace("/", "\\") if "\\" in rel else root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(body + "\n", encoding="utf-8")
            written.append(path)
    else:
        # fallback single-file split
        ko = posts / f"brunch_{target}_ko.md"
        en = posts / f"linkedin_{target}_en.md"
        ko.write_text(out[: len(out) // 2] + "\n", encoding="utf-8")
        en.write_text(out[len(out) // 2 :] + "\n", encoding="utf-8")
        written = [ko, en]

    return written


RUNNERS = {
    "drafter": run_drafter,
    "critic": run_critic,
    "reviser": run_reviser,
    "finalist": run_finalist,
    "verifier": run_verifier,
    "publisher": run_publisher,
}
