# RLF Core Rubric — 100-point Scoring Matrix

**Version:** v1.0
**Status:** Canonical. Changes require a dedicated PR labeled `rubric-change`.
**Used by:** Agent 02 — Critic.

> The Critic uses this rubric to evaluate any RLF-related artifact (paper, checklist, rubric, guide, one-pager, blog source, education material). Different artifact types use the same dimensions but with adjusted weight emphasis described at the bottom.

---

## The 7 dimensions

The rubric is intentionally structured to mirror the 7 stages of the Reverse Learning Framework. This is not decorative — it forces the Critic to evaluate RLF artifacts using RLF's own conceptual lens, which is the most rigorous form of self-consistency the system can apply.

| # | Dimension | Max Points | RLF Stage Mapping |
|--:|---|--:|---|
| 1 | Conceptual Clarity | 20 | Stage 1 (Artifact framing) |
| 2 | Epistemic Honesty | 15 | Stage 2 (Skepticism) |
| 3 | Evidence & Verification | 20 | Stage 3 (Verification) |
| 4 | Dialogic Quality | 10 | Stage 4 (Iterative prompting) |
| 5 | Contextual Relevance | 15 | Stage 5 (Contextual integration) |
| 6 | Structural Reconstruction | 10 | Stage 6 (Human reconstruction) |
| 7 | Ownership & Defensibility | 10 | Stage 7 (Explainable ownership) |
| | **Total** | **100** | |

---

## 1. Conceptual Clarity (20 points)

**What this measures:** Does the artifact define what RLF is, what it is not, and what its distinct contribution is — clearly enough that a first-time reader can paraphrase the core claim correctly?

| Criterion | Points |
|---|--:|
| Core principle ("AI output is not the final answer; it is the starting point of learning") stated or operationalized | 4 |
| Distinction from inverse RL / ML term collision is preserved where relevant | 3 |
| The 7 stages are referenced correctly (order, names, no confusion of Skepticism vs Iterative Prompting) | 5 |
| Distinct contribution articulated (starting artifact is AI-generated; not just "non-linear learning") | 4 |
| No unjustified jargon; if introduced, defined | 4 |

**Score 0** if the artifact misrepresents what RLF is.

---

## 2. Epistemic Honesty (15 points)

**What this measures:** Does the artifact resist the failure mode RLF was built to prevent — confident-sounding claims with no support?

| Criterion | Points |
|---|--:|
| Empirical claims are either cited or flagged as needing citation | 5 |
| Claims about study results / publication status are accurately stated (e.g., "submitted to TechTrends, under review" — not "published in TechTrends") | 4 |
| Limitations are explicitly stated where they exist | 3 |
| No marketing-grade hyperbole ("revolutionary", "game-changing", "transforms education forever") | 3 |

**Score 0** if the artifact claims peer-reviewed status for work still under review, or invents citations.

---

## 3. Evidence & Verification (20 points) — heaviest dimension

**What this measures:** Is each non-trivial claim supported, and is supporting material genuine?

| Criterion | Points |
|---|--:|
| Theoretical anchors (constructionism, epistemic cognition, info literacy, metacognition, situated learning, generative learning, self-explanation) are correctly attributed when invoked | 6 |
| Citations resolve to real works (where checkable by name/title/year heuristics) | 5 |
| Examples are concrete, not generic | 4 |
| Quantitative claims include source or scope | 3 |
| Code, calculations, or procedures (if any) are testable | 2 |

This dimension is weighted heaviest because Verification is the *core mechanism* of RLF. An artifact that fails this dimension undermines the framework it represents.

---

## 4. Dialogic Quality (10 points)

**What this measures:** Does the artifact invite engagement (questions, dialogue, follow-up prompts) rather than terminate thought?

| Criterion | Points |
|---|--:|
| Includes reflection prompts, questions, or self-test elements where artifact type warrants | 3 |
| Anticipates objections and addresses them | 3 |
| Provides examples of generative dialogue with AI (when relevant to artifact type) | 2 |
| Does not foreclose alternative pedagogical approaches (PBL, inquiry-based, etc.) | 2 |

For artifact types where dialogic elements are not natural (e.g., a one-pager), criterion 1 may be marked N/A and its points redistributed to criteria 2–4 proportionally.

---

## 5. Contextual Relevance (15 points)

**What this measures:** Is the artifact usable in real settings, by real people, with real constraints?

| Criterion | Points |
|---|--:|
| Audience is named and addressed (students / instructors / corporate L&D / facilitators) | 4 |
| At least one concrete, recognizable use case is described | 4 |
| Constraints (time, stakes, format) are acknowledged | 3 |
| Cultural / linguistic context is considered where relevant | 2 |
| Avoids US-centric or English-only assumptions when scope is global | 2 |

---

## 6. Structural Reconstruction (10 points)

**What this measures:** Does the artifact show evidence of human reconstruction — not just sequenced AI output?

| Criterion | Points |
|---|--:|
| Voice is consistent across sections | 3 |
| Structure serves the argument (not template-driven filler) | 3 |
| Transitions are reasoned, not formulaic | 2 |
| Length is justified by content, not padded | 2 |

---

## 7. Ownership & Defensibility (10 points)

**What this measures:** Can the human author of the artifact defend it? Are responsibility and limits explicit?

| Criterion | Points |
|---|--:|
| Ownership Statement is present (RLF Part 7 dogfooded) | 4 |
| Author / responsible party is identified | 2 |
| Limitations are owned, not hidden | 2 |
| The artifact identifies what would falsify or challenge it | 2 |

---

## Calibration anchors

These anchors are required reading for the Critic on every run. They prevent score drift across iterations.

### 95–100 — publishable as-is (rare)
- Every dimension scores at or above the 90th percentile of its max.
- Zero blockers, zero major issues.
- The artifact reads as if it has already been through this pipeline — internally consistent, honestly hedged, structurally tight.

### 85–94 — strong, minor polish needed
- One or two minor issues per dimension.
- No major issues in Conceptual Clarity, Epistemic Honesty, or Evidence & Verification.
- Worth finalizing; may still benefit from a light pass.

### 70–84 — sound but with at least one major issue
- One dimension shows a major issue, OR multiple minor issues clustered.
- Reviser should address before Finalist runs.
- Common pattern: Conceptual Clarity is strong but Evidence & Verification has unsupported claims.

### 50–69 — significant rework needed
- Two or more dimensions show major issues.
- Multiple `[NEEDS CITATION]` markers unresolved by the time of Critic review.
- May indicate the brief was underspecified.

### Below 50 — off-canon or structurally broken
- One or more dimensions score 0.
- Examples: misrepresents what RLF is; claims peer review for work under review; invents citations; uses RLF's name for an inverse-RL discussion.
- Reviser cannot fix this in one iteration — Orchestrator should consider routing back to Drafter with a corrected brief.

---

## Artifact-type emphasis adjustments

The Critic uses dimension WEIGHTING (the score caps stay 100 total) but emphasizes different dimensions when reading different artifact types:

| Artifact type | Emphasize | De-emphasize |
|---|---|---|
| `paper` (academic manuscript) | 1, 2, 3, 6 | 4 |
| `checklist` / `rubric` | 1, 4, 5, 7 | 6 |
| `one_pager` | 1, 5 | 4, 6 |
| `guide` (instructor / corporate) | 1, 3, 5, 7 | — |
| `blog_source` | 1, 5, 7 | 3 (full citation rigor relaxed) |
| `education` (lesson plan / module) | 4, 5, 7 | 3 (research-grade rigor relaxed) |

Emphasis adjustments mean the Critic considers an 18/20 in Conceptual Clarity as more decisive for an artifact type that emphasizes that dimension. The numeric score does not change.

---

## Out-of-rubric observations

The Critic occasionally finds problems that do not fit any dimension. These go into `out_of_rubric_observations` in the JSON output and do NOT affect the numeric score. Examples:

- Filename or frontmatter inconsistencies.
- Repository hygiene issues (file in wrong folder, missing `final/` companion).
- Style issues that are subjective (e.g., title length preference).

If a pattern of out-of-rubric observations recurs across iterations, that is a signal the rubric itself may need a revision PR.
