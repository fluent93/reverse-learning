from __future__ import annotations

import re
from pathlib import Path


def load_system_prompt(agent_md: Path) -> str:
    text = agent_md.read_text(encoding="utf-8")
    # First fenced block under "## System prompt"
    section = re.search(
        r"## System prompt\s*\n+```(?:\w+)?\n(.*?)```",
        text,
        re.DOTALL,
    )
    if section:
        return section.group(1).strip()
    raise ValueError(f"No system prompt block found in {agent_md}")


def agent_prompt_path(agent_id: str) -> Path:
    from .repo import repo_root

    mapping = {
        "drafter": "01_drafter.md",
        "critic": "02_critic.md",
        "reviser": "03_reviser.md",
        "finalist": "04_finalist.md",
        "verifier": "05_verifier.md",
        "publisher": "06_publisher.md",
    }
    name = mapping.get(agent_id)
    if not name:
        raise KeyError(agent_id)
    return repo_root() / "agents" / name
