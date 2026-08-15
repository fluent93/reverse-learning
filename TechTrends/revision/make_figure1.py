"""Generate Figure 1: The Reverse Learning Framework (iterative version)."""
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

parser = argparse.ArgumentParser()
parser.add_argument(
    "--out",
    default="/home/ubuntu/work/reverse-learning/TechTrends/revision/Figure1_Reverse_Learning_Framework.png",
)
args = parser.parse_args()

fig, ax = plt.subplots(figsize=(13.5, 6.2))
ax.set_xlim(0, 13.5)
ax.set_ylim(0, 6.2)
ax.axis("off")

BOX_FC = "#eef2f7"
BOX_EC = "#37474f"
GROUP_EC = "#78909c"
FAIL_EC = "#b0bec5"
TXT = "#1c2733"
ANNOT = "#607d8b"

def box(cx, cy, w, h, text, fc=BOX_FC, ec=BOX_EC, fs=10.5, bold=True, dashed=False, tc=TXT):
    p = FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0.06,rounding_size=0.12",
        fc=fc, ec=ec, lw=1.4, linestyle="--" if dashed else "-", zorder=3)
    ax.add_patch(p)
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
            color=tc, weight="bold" if bold else "normal", zorder=4)

def arrow(x1, y1, x2, y2, dashed=False, rad=0.0, color=BOX_EC, lw=1.6, mut=16):
    a = FancyArrowPatch((x1, y1), (x2, y2),
                        connectionstyle=f"arc3,rad={rad}",
                        arrowstyle="-|>", mutation_scale=mut,
                        lw=lw, color=color,
                        linestyle="--" if dashed else "-", zorder=2)
    ax.add_patch(a)

# ---- main components ------------------------------------------------------
box(1.35, 3.6, 2.1, 1.0, "AI-Generated\nArtifact")
box(3.85, 3.6, 1.9, 1.0, "Learner\nSkepticism")

# inquiry loop group
group = FancyBboxPatch((5.35, 2.15), 2.7, 2.95,
                       boxstyle="round,pad=0.08,rounding_size=0.16",
                       fc="none", ec=GROUP_EC, lw=1.2, linestyle=(0, (4, 3)), zorder=1)
ax.add_patch(group)
box(6.7, 4.3, 2.15, 0.85, "Verification")
box(6.7, 2.95, 2.15, 0.85, "Iterative\nPrompting")
ax.text(6.7, 5.35, "Inquiry loop", ha="center", va="center",
        fontsize=9.5, style="italic", color=ANNOT)

# conversion group
box(9.55, 4.3, 2.3, 0.85, "Contextual\nIntegration")
box(9.55, 2.95, 2.3, 0.85, "Human\nReconstruction")

box(12.15, 3.6, 2.15, 1.15, "Explainable\nOwnership")

# failure exit
box(3.85, 1.15, 2.5, 0.85, "Passive delegation\n(no learning process)",
    fc="#fafbfc", ec=FAIL_EC, fs=9, bold=False, dashed=True, tc="#78909c")

# ---- arrows ----------------------------------------------------------------
arrow(2.42, 3.6, 2.88, 3.6)                                  # artifact -> skepticism
arrow(4.82, 3.6, 5.45, 3.85, rad=-0.12)                      # skepticism -> loop
arrow(3.85, 3.08, 3.85, 1.62, dashed=True, color=FAIL_EC)    # skepticism -> passive delegation

# verification <-> prompting loop arrows
arrow(6.15, 3.92, 6.15, 3.34, rad=0.55)
arrow(7.25, 3.34, 7.25, 3.92, rad=0.55)

arrow(7.82, 4.3, 8.36, 4.3)                                  # verification -> contextual integration
arrow(9.55, 3.86, 9.55, 3.4)                                 # integration -> reconstruction
arrow(10.74, 3.15, 11.03, 3.38)                              # reconstruction -> ownership

# feedback: conversion -> inquiry loop (new gaps exposed)
arrow(8.86, 2.62, 7.4, 2.6, dashed=True, rad=-0.25, color=ANNOT)
arrow(9.0, 4.75, 7.35, 4.78, dashed=True, rad=0.28, color=ANNOT)

# ---- annotations -----------------------------------------------------------
ax.text(3.32, 4.35, "gateway (P1)", fontsize=8.5, style="italic", color=ANNOT, ha="center")
ax.text(6.7, 1.85, "verification and prompting\nmutually discipline each other (P2)",
        fontsize=8.5, style="italic", color=ANNOT, ha="center", va="top")
ax.text(9.55, 1.85, "conversion; regression to the\ninquiry loop is expected (P3)",
        fontsize=8.5, style="italic", color=ANNOT, ha="center", va="top")
ax.text(12.15, 2.6, "exit state (P4):\nexplain, defend, and revise\nwithout AI assistance",
        fontsize=8.5, style="italic", color=ANNOT, ha="center", va="top")
ax.text(4.45, 2.35, "skepticism\nnot activated", fontsize=8, style="italic",
        color="#90a4ae", ha="left", va="center")
ax.text(8.2, 5.35, "new gaps exposed", fontsize=8.5, style="italic", color=ANNOT, ha="center")
ax.text(6.75, 5.85, "expertise and task stakes moderate cycle intensity (P5)",
        fontsize=8.5, style="italic", color=ANNOT, ha="center")

plt.tight_layout()
out = args.out
plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
print("saved", out)
