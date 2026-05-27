# Brief — Student-Facing Simplified Checklist

> This is a worked example brief. Use it as a reference for how a well-formed brief looks. The actual artifact this brief would produce does not yet exist in `final/` — it would be the result of running the pipeline with this brief.

---

## Slug

`student-checklist-v1`

---

## Artifact type

`checklist`

---

## Target version

`v1.0`

---

## Primary language

`ko`

(English summary section at the end, ~200 words.)

---

## Audience

Korean undergraduate students (years 1–4) taking their first course that involves generative AI as a learning tool. Assumed reading time per session: 15 minutes. No prior exposure to the Reverse Learning Framework expected. Most students will have used ChatGPT casually but not for academic work.

---

## Purpose

Give a student a short, friendly, classroom-usable checklist they can apply to any AI-assisted assignment, so they can demonstrate Reverse Learning behaviors without reading the full v1.0 checklist.

---

## Length target

Roughly 800–1,200 Korean characters in the body, plus a 200-word English summary. Should fit on two printed pages.

---

## Scope — what to include

- Plain-Korean restatement of the 7 RLF stages (one paragraph per stage maximum).
- A 5-question "before submitting" mini-checklist students can mentally run through.
- One classroom-realistic example per stage (use scenarios like "writing an essay on climate policy", "designing a poster", "translating a research paper").
- A short Ownership Statement template adapted to a student voice (not corporate).
- A "what counts as evidence" sidebar for each stage.

---

## Scope — what to exclude

- No academic theory citations (constructionism, situated learning, etc.) — those belong in the full v1.0 checklist, not the student version.
- No instructor-facing guidance (a separate brief will produce that).
- No discussion of grading or assessment policy — out of scope for the student-facing artifact.
- No emoji or playful illustrations — keep it clean, not childish.

---

## RLF stage focus

Stages 1–7, but weighted toward Stages 2 (Skepticism), 3 (Verification), and 7 (Ownership). Stages 4 and 6 can be shorter — undergraduates rarely struggle with iterative prompting (they prompt naturally) or reconstruction (they're trained to rewrite by their instructors).

---

## Voice and tone

`educational` — warm, direct, second-person. Treat the student as a capable adult, not a child. Avoid jargon. Define any required term inline at first use.

Korean: 합니다체 default. Switch to 해요체 only in the closing reflection prompts where a softer voice helps.

---

## Source materials to draw from

- `Reverse Learning Framework One-Pager.md` (for core principle and stage definitions)
- `RLF-Checklist-AIOutputReview-v1.0.md` (for stage detail and evidence checkpoints — distill, don't copy)
- `README.md` (for framing language)

External references: none required. This is a distillation, not an expansion.

---

## Known constraints

- Must be readable on a phone screen without horizontal scrolling — i.e., no tables wider than 3 columns.
- Must avoid headers deeper than `###`.
- Must work if printed in black-and-white (no color-dependent meaning).
- Must remain usable by a student who has never read the v1.0 checklist.

---

## Open questions the Drafter should flag

1. Should the "before submitting" mini-checklist appear at the top (TLDR-style) or at the bottom (as a summary)? Flag the choice and reasoning in the Drafter Notes.
2. Is 7 stages too many for a 15-minute read? If the Drafter believes a collapsing of stages (e.g., merging 4 and 6 into one) is warranted, surface that as a canon-conflict in Drafter Notes — but the Drafter must NOT silently merge them. Canon conflict resolution is the human owner's call.

---

## Acceptance criteria (for the Critic)

- An undergraduate who has never read the v1.0 checklist can correctly paraphrase the core principle after one reading.
- Every stage has at least one concrete classroom example.
- The Ownership Statement reads like a student's own voice, not a paraphrase of the v1.0 statement.
- No theoretical anchor citations leak in from the v1.0 version (those belong in instructor-facing material).
- Korean body and English summary make the same factual claims with no contradictions.

---

## Notes for the human owner (not for the Drafter)

- This is the first student-facing artifact in the RLF catalog. If it works, it becomes the basis for university partnerships.
- Watch for tone drift in iteration 2+ — the Reviser tends to over-formalize when given Critic feedback. If voice degrades, push back in the Reviser's Changelog DISAGREE column.
- Consider whether to release the English summary as a separate `final/v1.0-en.md` companion artifact rather than embedding it. Decide before publication.
