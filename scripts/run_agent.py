#!/usr/bin/env python3
"""Run one RLF sub-agent via OpenAI or Anthropic API."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Allow running from repo root or scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent))

from rlf_lib.llm import AGENT_MODEL
from rlf_lib.repo import repo_root
from rlf_lib.run_agent_impl import RUNNERS
from rlf_lib.state_io import load_state, save_state


def _check_keys(agent: str) -> None:
    family = AGENT_MODEL[agent]
    if family == "openai" and not os.environ.get("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set")
    if family == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY"):
        raise EnvironmentError("ANTHROPIC_API_KEY is not set")


def _update_state_after(agent: str, written: list[Path]) -> None:
    state = load_state()
    root = repo_root()
    rel = lambda p: str(p.relative_to(root)).replace("\\", "/")

    if agent == "drafter" and written:
        state["latest_draft"] = rel(written[0])
        state["current_stage"] = "critiquing"
    elif agent == "critic" and written:
        for p in written:
            if p.suffix == ".json":
                state["latest_review"] = rel(p)
        state["current_stage"] = "revising"
    elif agent == "reviser" and written:
        state["latest_draft"] = rel(written[0])
        state["current_stage"] = "critiquing"
    elif agent == "finalist" and written:
        state["latest_final"] = rel(written[0])
        state["current_stage"] = "verifying"
    elif agent == "verifier" and written:
        state["latest_verification"] = rel(written[0])
        state["current_stage"] = "awaiting_human_approval"

    save_state(state)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one RLF agent")
    parser.add_argument("--agent", required=True, choices=list(RUNNERS.keys()))
    args = parser.parse_args()

    if args.agent == "publisher":
        state = load_state()
        if not state.get("human_gates", {}).get("publish_authorized"):
            print("Publisher skipped: human_gates.publish_authorized is false", file=sys.stderr)
            return 0

    _check_keys(args.agent)
    written = RUNNERS[args.agent]()
    _update_state_after(args.agent, written)
    for p in written:
        print(f"Wrote {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
