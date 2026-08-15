"""Create selective-highlight and clean R2 manuscript sources.

The authoring source preserves the full rewrite history. The marked submission
source highlights the principal reviewer-responsive conceptual revisions so the
revision remains readable, while the clean source contains identical prose with
no revision shading.
"""
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "Manuscript_R2_improved.md"
MARKED = BASE / "Manuscript_R2_marked.md"
CLEAN = BASE / "Manuscript_R2_clean.md"

blocks = [block.strip() for block in SOURCE.read_text().split("\n\n") if block.strip()]
if len(blocks) != 137:
    raise RuntimeError(f"Expected 137 manuscript blocks, found {len(blocks)}; review the highlight map.")

# Principal reviewer-responsive additions and conceptual revisions.
selected = {
    # Learner agency and activation
    22, 23, 24, 25,
    # Pedagogical meaning of the reversal
    29,
    # Integrated mechanism: the fluency-validity gap
    31, 32, 33, 36,
    # Revised definition
    38,
    # Redeveloped iterative figure and note
    41, 42, 44,
    # Relationships and Propositions 1-5
    45, 48, 49, 50, 51, 52,
    # Explainable ownership and its evidence table
    62, 63, 64, 66, 67, 68,
    # Readiness, novice-expert differences, scaffolding, and equity
    69, 70, 71, 72, 73,
    # Educational concept boundaries and novelty
    74, 76, 77, 79, 80,
    # Disciplinary variation, boundary conditions, and limitations
    90, 91, 92, 93,
}

# References that were added during revision remain highlighted.
selected.update(i for i, block in enumerate(blocks) if i >= 108 and "==" in block)

clean_blocks = [block.replace("==", "") for block in blocks]


def mark_block(block):
    if block.startswith("[TABLE]"):
        return "\n".join(f"=={line}==" for line in block.splitlines())
    return f"=={block}=="


marked_blocks = [mark_block(block) if i in selected else block for i, block in enumerate(clean_blocks)]

CLEAN.write_text("\n\n".join(clean_blocks) + "\n")
MARKED.write_text("\n\n".join(marked_blocks) + "\n")

print(f"saved {MARKED}")
print(f"saved {CLEAN}")
print(f"highlighted blocks: {len(selected)} of {len(blocks)}")
