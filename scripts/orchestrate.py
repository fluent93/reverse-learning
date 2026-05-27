#!/usr/bin/env python3
"""Deterministic RLF pipeline router. No LLM calls."""
from __future__ import annotations

import argparse
import json
import sys

from rlf_lib.orchestrate import apply_decision, decide


def main() -> int:
    parser = argparse.ArgumentParser(description="RLF Orchestrator (rule-based)")
    parser.add_argument("--json", action="store_true", help="Print decision as JSON")
    parser.add_argument("--no-write", action="store_true", help="Do not update state.json")
    args = parser.parse_args()

    decision = decide()
    if not args.no_write and decision.next_agent not in ("done",):
        apply_decision(decision, persist=True)

    payload = {
        "next_agent": decision.next_agent,
        "rule_applied": decision.rule_applied,
        "reason": decision.reason,
        "state_updates": decision.state_updates,
    }

    if args.json:
        print(json.dumps(payload))
    else:
        print(f"next_agent={decision.next_agent}")
        print(f"reason={decision.reason}")

    if decision.next_agent == "human":
        return 0
    if decision.next_agent == "done":
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
