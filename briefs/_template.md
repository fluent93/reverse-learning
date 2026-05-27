# Brief Template

> Copy this file to `briefs/<your-slug>.md`, fill in every section, then run the Drafter agent (`agents/01_drafter.md`) with it. See `agents/RUNBOOK.md` Step 0 for the full sequence.

> **How to use this template:** Replace each `<...>` placeholder. Delete the explanatory "guidance" lines after each heading once you've filled them in. The Drafter is allowed to push back on a brief if something is missing — but a well-formed brief produces a much stronger v1.

---

## Slug

`<your-slug>`

*guidance: lowercase-with-dashes, will be reused for branch name (`pipeline/<slug>`) and `pipeline_id` in `state.json`. Pick a slug that will still make sense to you in 6 months.*

---

## Artifact type

`<paper | checklist | rubric | guide | one_pager | blog_source | education>`

*guidance: this drives Critic rubric weighting (see `agents/rubrics/rlf-core-rubric.md` for artifact-type emphasis adjustments). Choose carefully.*

---

## Target version

`v1.0`

*guidance: starts at v1.0 for new artifacts. For revisions of an existing artifact, bump appropriately (v1.1 for refinement, v2.0 for structural change).*

---

## Primary language

`<en | ko | both>`

*guidance: if `both`, specify in the body which sections are which. Bilingual artifacts cost more iterations — budget accordingly.*

---

## Audience

`<who this is for>`

*guidance: be specific. "Educators" is too vague. "Korean undergraduate students taking their first AI literacy course" is the right level of specificity. Include any constraints: age, professional background, prior exposure to RLF, language fluency.*

---

## Purpose

`<what this artifact should accomplish>`

*guidance: one sentence. If you can't say what success looks like in one sentence, the brief is not ready.*

---

## Length target

`<word count or page count>`

*guidance: be honest. "About 2 pages" is fine. "Around 1,500 words" is better. The Drafter will calibrate length; the Critic will flag padding or thinness.*

---

## Scope — what to include

`<bulleted list of must-cover topics>`

*guidance: 3–7 bullets typically. More than 7 and the artifact will sprawl; fewer than 3 and the Drafter may invent scope.*

---

## Scope — what to exclude

`<bulleted list of things explicitly NOT in scope>`

*guidance: this is often more useful than the include list. Examples: "Do not cover technical ML methods", "Do not discuss copyright law", "Do not include code samples". The Drafter respects exclusions strictly.*

---

## RLF stage focus

`<which of the 7 RLF stages this artifact emphasizes>`

*guidance: optional but useful. Examples: "Heavy emphasis on Stages 2–3 (Skepticism + Verification); Stage 7 only briefly mentioned." Helps Critic weight evaluation.*

---

## Voice and tone

`<scholar | scholar-practitioner | practitioner | conversational | educational>`

*guidance: pick one. The Drafter and Finalist will both honor this. If unsure, default to "scholar-practitioner" — that's the house style for RLF outputs.*

---

## Source materials to draw from

`<bulleted list of files in this repo OR external references>`

*guidance: list which files in the repo should anchor this artifact. Always include canon files when relevant:*

- `Reverse Learning Framework One-Pager.md`
- `RLF-Checklist-AIOutputReview-v1.0.md`
- `README.md`

*If you have a previous version of this artifact in `final/`, list it here.*

---

## Known constraints

`<any constraint the Drafter must respect>`

*guidance: examples — "must fit on one slide", "must be readable in 10 minutes", "no marketing language", "must work without internet access for verification". Practical constraints, not aesthetic preferences.*

---

## Open questions the Drafter should flag

`<questions you want the Drafter Notes section to address>`

*guidance: optional. If you're uncertain about a design choice, list it here and the Drafter will surface its decision in the Drafter Notes section at the end of v1. This is faster than guessing.*

---

## Acceptance criteria (for the Critic)

`<what would make this artifact a 90+>`

*guidance: optional but powerful. If you can describe what "great" looks like, the Critic uses this as a signal. Examples:*

- *"Every claim has a verifiable source or is flagged."*
- *"A first-year undergraduate can paraphrase the core idea after one read."*
- *"The Ownership Statement reads as if a working professional wrote it, not an academic ghost."*

---

## Notes for the human owner (not for the Drafter)

`<reminders to yourself>`

*guidance: anything you want to remember when reviewing the final PR. The Drafter does not read this section.*
