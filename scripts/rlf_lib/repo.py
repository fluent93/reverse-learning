from __future__ import annotations

import re
from pathlib import Path


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "agents" / "00_orchestrator.md").exists():
            return parent
    raise RuntimeError("Could not find reverse-learning repo root")


def version_num(path: Path) -> int:
    m = re.search(r"v(\d+)", path.stem)
    return int(m.group(1)) if m else 0


def latest_file(glob_pattern: str, root: Path | None = None) -> Path | None:
    root = root or repo_root()
    files = list(root.glob(glob_pattern))
    if not files:
        return None
    return max(files, key=version_num)


def review_path_for_draft(draft: Path) -> Path:
    n = version_num(draft)
    return draft.parent.parent / "reviews" / f"v{n}-review.json"


def verification_path_for_final(final: Path) -> Path:
    # final/v1.0.md -> verification/v1.0-check.md
    ver = final.stem  # v1.0
    return final.parent.parent / "verification" / f"{ver}-check.md"
