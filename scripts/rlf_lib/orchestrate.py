from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .repo import (
    latest_file,
    repo_root,
    review_path_for_draft,
    verification_path_for_final,
)
from .state_io import append_history, load_state, save_state


@dataclass
class RouteDecision:
    next_agent: str
    rule_applied: int
    reason: str
    state_updates: dict


def _read_review_score(review_path: Path) -> int | None:
    if not review_path.exists():
        return None
    data = json.loads(review_path.read_text(encoding="utf-8"))
    return data.get("total_score")


def _verifier_verdict(verification_path: Path) -> str | None:
    if not verification_path.exists():
        return None
    text = verification_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.strip().startswith("**Verdict:**"):
            if "FAIL" in line:
                return "FAIL"
            if "PASS_WITH_FLAGS" in line:
                return "PASS_WITH_FLAGS"
            if "PASS" in line:
                return "PASS"
    return None


def decide(state: dict | None = None) -> RouteDecision:
    root = repo_root()
    state = state or load_state()
    threshold = state.get("score_threshold", 90)
    iter_max = state.get("iteration_max", 3)
    iteration = state.get("iteration", 0)
    stage = state.get("current_stage", "kickoff")

    latest_draft = latest_file("drafts/v*.md", root)
    latest_final = latest_file("final/v*.md", root)

    human = state.get("human_gates") or {}
    approved = human.get("approved", False)
    publish_ok = human.get("publish_authorized", False)

    # Rule 6 — publisher (check before other terminal states)
    if approved and publish_ok and latest_final and latest_final.exists():
        posts = list((root / "posts").glob("*.md")) if (root / "posts").exists() else []
        target = state.get("target_version", "v1.0").replace(".", "_")
        if not any(target in p.name for p in posts):
            return RouteDecision(
                "publisher",
                6,
                "Human approved and authorized publish; post drafts missing.",
                {},
            )

    if latest_final and latest_final.exists():
        vpath = verification_path_for_final(latest_final)
        verdict = _verifier_verdict(vpath)
        if verdict == "FAIL":
            return RouteDecision(
                "reviser",
                7,
                "Verifier returned FAIL; route to Reviser for remediation.",
                {"current_stage": "remediation", "escalation_reason": "verifier_fail"},
            )
        if verdict in ("PASS", "PASS_WITH_FLAGS") and not approved:
            return RouteDecision(
                "human",
                0,
                f"Verifier {verdict}; awaiting human PR approval.",
                {"current_stage": "awaiting_human_approval"},
            )

    # Rule 5 — verifier
    if latest_final and latest_final.exists():
        vpath = verification_path_for_final(latest_final)
        if not vpath.exists():
            return RouteDecision(
                "verifier",
                5,
                f"Final {latest_final.name} exists without verification report.",
                {"current_stage": "verifying", "latest_final": str(latest_final.relative_to(root)).replace("\\", "/")},
            )

    # Rules 3–4 — after critic review exists
    if latest_draft and latest_draft.exists():
        rpath = review_path_for_draft(latest_draft)
        score = _read_review_score(rpath)
        rel_draft = str(latest_draft.relative_to(root)).replace("\\", "/")

        if score is None:
            return RouteDecision(
                "critic",
                2,
                f"Draft {latest_draft.name} has no paired review JSON.",
                {"current_stage": "critiquing", "latest_draft": rel_draft},
            )

        state["latest_total_score"] = score
        state["latest_review"] = str(rpath.relative_to(root)).replace("\\", "/")

        if score >= threshold or iteration >= iter_max:
            reason = (
                f"Score {score} >= {threshold}."
                if score >= threshold
                else f"iteration {iteration} >= {iter_max} (escalation)."
            )
            updates = {"current_stage": "finalizing", "latest_draft": rel_draft}
            if iteration >= iter_max and score < threshold:
                updates["escalation_reason"] = "iter_max"
            return RouteDecision("finalist", 4, reason, updates)

        if score < threshold and iteration < iter_max:
            return RouteDecision(
                "reviser",
                3,
                f"Score {score} < {threshold} and iteration {iteration} < {iter_max}.",
                {
                    "current_stage": "revising",
                    "latest_draft": rel_draft,
                    "iteration": iteration + 1,
                },
            )

    # Rule 1 — drafter
    if latest_draft is None or not latest_draft.exists():
        return RouteDecision(
            "drafter",
            1,
            "No draft exists; route to Drafter from brief.",
            {"current_stage": "drafting"},
        )

    return RouteDecision("done", 0, "No routing rule matched; pipeline may be complete.", {})


def apply_decision(decision: RouteDecision, persist: bool = True) -> RouteDecision:
    state = load_state()
    prev = state.get("current_stage")
    for k, v in decision.state_updates.items():
        state[k] = v
    if decision.next_agent != "done" and decision.next_agent != "human":
        append_history(
            state,
            prev,
            state.get("current_stage", prev),
            decision.reason,
            actor="orchestrator",
            rule_applied=decision.rule_applied,
        )
    elif decision.next_agent == "human":
        append_history(
            state,
            prev,
            "awaiting_human_approval",
            decision.reason,
            actor="orchestrator",
            rule_applied=None,
        )
    if persist:
        save_state(state)
    return decision
