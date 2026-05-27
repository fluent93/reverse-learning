from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .repo import repo_root


def load_state(path: Path | None = None) -> dict:
    p = path or (repo_root() / "state.json")
    if not p.exists():
        raise FileNotFoundError(f"state.json not found at {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(state: dict, path: Path | None = None) -> None:
    p = path or (repo_root() / "state.json")
    p.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_history(
    state: dict,
    from_stage: str | None,
    to_stage: str,
    reason: str,
    actor: str = "orchestrator",
    rule_applied: int | None = None,
) -> None:
    state.setdefault("history", []).append(
        {
            "at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "from_stage": from_stage,
            "to_stage": to_stage,
            "reason": reason,
            "actor": actor,
            "rule_applied": rule_applied,
        }
    )
    state["current_stage"] = to_stage
