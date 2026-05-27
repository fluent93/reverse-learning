# Agents — Multi-Agent Pipeline for the Reverse Learning Framework

> **Self-reference:** This pipeline is a *reference implementation* of the Reverse Learning Framework. The system itself follows the same skepticism → verification → reconstruction → ownership pattern that RLF prescribes for human learners. We do not use a single agent because that would collapse the Generator–Critic dialectic that RLF depends on.

---

## Why multi-agent (and not single-agent)

The RLF workflow has four structural patterns:

| Pattern | Stages | Why a single agent fails |
|---|---|---|
| **Generator–Critic** | draft ↔ review | Self-evaluation by the same model produces self-confirmation bias — the exact failure mode RLF warns against. |
| **Iterative Refinement** | review → revise → re-review | Requires a stable, model-distinct critic to converge on quality. |
| **Format Transformation** | repo / Brunch (KR) / LinkedIn (EN) | Different audiences, tones, and languages — separation of concerns. |
| **Channel Switching** | mobile ↔ PC/Mac | Asynchronous handoffs only work if state is externalized (git, not RAM). |

Therefore: **one Orchestrator + role-specialized sub-agents**, with **git as the single source of truth**.

---

## Agent roster

| # | Agent | Model intent | Trigger | Reads | Writes |
|--:|---|---|---|---|---|
| 00 | **Orchestrator** | Cursor Background Agent (Claude family) | Push to `drafts/**` or manual | `state.json` | `state.json`, routes to next agent |
| 01 | **Drafter** | GPT-5 (ChatGPT) | Human prompt OR Reviser fallback | topic spec | `drafts/v{n}.md` |
| 02 | **Critic** | Claude Opus 4.6 / 4.7 | New `drafts/v{n}.md` exists | `drafts/v{n}.md`, `rubrics/rlf-core-rubric.md` | `reviews/v{n}-review.md` + `reviews/v{n}-review.json` |
| 03 | **Reviser** | GPT-5 | Critic score `< 90` AND `iteration < 3` | latest draft + latest review | `drafts/v{n+1}.md` |
| 04 | **Finalist** | Claude Opus 4.6 / 4.7 | Critic score `>= 90` OR `iteration == 3` | latest draft + full review history | `final/v{ver}.md` |
| 05 | **Verifier** | GPT-5 | New `final/v{ver}.md` exists | final + framework canon (`README.md`, One-Pager, Checklist) | `verification/v{ver}-check.md` |
| 06 | **Publisher** | Claude (local Cursor or BG) | Human approval comment on PR | `final/v{ver}.md` | `posts/brunch_v{ver}_ko.md`, `posts/linkedin_v{ver}_en.md` |

> Models named above are the *intended* operators. Each agent file is model-agnostic in wording so the same prompt can be served by an upgraded model without rewrite.

---

## Pipeline (state machine)

```
        ┌──────────┐
        │  Drafter │◀──────────────────────┐
        └────┬─────┘                       │
             │ drafts/v{n}.md              │ revise
             ▼                             │
        ┌──────────┐    score < 90    ┌────┴────┐
        │  Critic  │─────────────────▶│ Reviser │
        └────┬─────┘  & iter < 3      └─────────┘
             │ score ≥ 90  OR  iter == 3
             ▼
        ┌──────────┐
        │ Finalist │
        └────┬─────┘
             │ final/v{ver}.md
             ▼
        ┌──────────┐
        │ Verifier │
        └────┬─────┘
             │ pass
             ▼
        ┌──────────┐
        │  HUMAN   │  ← Approve PR on GitHub mobile
        └────┬─────┘
             ▼
        ┌──────────┐
        │Publisher │  → Brunch (KR) + LinkedIn (EN) drafts
        └──────────┘
```

Hard limits:

- `iteration_max = 3` (Critic ↔ Reviser loop). After 3 rounds the artifact is escalated to Finalist regardless of score, with the failure reason logged.
- `score_threshold = 90` (configurable in `state.json`).
- All transitions are recorded in `state.json` → fully reproducible audit trail.

---

## Folder layout

```
agents/
├── README.md                       ← this file
├── 00_orchestrator.md              ← state machine + routing prompt
├── 01_drafter.md                   ← GPT system prompt
├── 02_critic.md                    ← Claude Opus rubric-based reviewer
├── 03_reviser.md                   ← GPT revision prompt
├── 04_finalist.md                  ← Claude Opus final writer
├── 05_verifier.md                  ← GPT canon-consistency checker
├── 06_publisher.md                 ← Brunch + LinkedIn dual-output
├── rubrics/
│   └── rlf-core-rubric.md          ← 100-point scoring matrix
└── schema/
    ├── state.schema.json           ← state machine contract
    ├── state.example.json          ← reference instance
    └── review.schema.json          ← Critic JSON output contract
```

Pipeline artifacts (produced at runtime, lives at repo root):

```
drafts/        ← Drafter / Reviser outputs (versioned)
reviews/       ← Critic outputs (.md narrative + .json structured)
final/         ← Finalist canonical output
verification/  ← Verifier sign-off
posts/         ← Publisher outputs (KR + EN)
state.json     ← current pipeline state
```

---

## Where each agent runs (environment mapping)

| Environment | Used for | Reason |
|---|---|---|
| **Mobile — ChatGPT app** | Drafter, Reviser (manual fallback) | Available in corporate environment, no file upload barrier |
| **Mobile — Cursor mobile app** | Triggering Background Agents | Spawns Orchestrator on company commute / off-desk |
| **Mobile — GitHub app** | Final PR approval, Publisher trigger | One-tap human gate |
| **Corporate PC — Cursor Web (browser)** | Critic, Reviser, Finalist, Verifier as Background Agents | No local file upload needed — agent reads from git |
| **Mac / PC — Cursor Desktop** | Publisher final polish, occasional manual override | Full IDE for review and edits |

**Key insight:** because every agent reads from and writes to git, the "Cursor Web ↔ local Cursor sync" question becomes trivial — they are already synchronized through the repository. Pull on the desktop, you get whatever the cloud agents produced.

---

## How a human interacts with this pipeline

You only need to act at **three points**:

1. **Kickoff**  — give Drafter the topic (mobile ChatGPT or open a PR with a `briefs/` doc).
2. **Approval** — review the PR Verifier flagged as ready, approve on mobile GitHub.
3. **Publish review** — read Publisher's Brunch + LinkedIn drafts, edit as needed, post.

Everything else is observed by reading `state.json` (one screen) or the PR conversation.

---

## Design principles (non-negotiable)

1. **Git is the only state.** No agent holds memory between runs. Reproducibility > convenience.
2. **JSON for machine, Markdown for human.** Every Critic / Verifier output ships in both formats.
3. **The rubric is canon.** `rubrics/rlf-core-rubric.md` is the single source of evaluation truth. Changes to it require a separate PR.
4. **No silent disagreement.** When Reviser ignores a Critic point, it must say so explicitly in the next draft's changelog block.
5. **The pipeline dogfoods RLF.** Every output includes an Ownership Statement section so the framework's own outputs satisfy Part 7.

---

## Future extensions (post-MVP)

- Add **Dissent Agent**: a third-model adversary that argues against the Finalist's draft to stress-test ownership.
- Add **Student-Persona Critic**: reads outputs as a learner unfamiliar with RLF, scores accessibility.
- Add **Citation Agent**: cross-references claims against the TechTrends manuscript bibliography.
- Add **Translator QA**: round-trip translation check on Brunch ↔ LinkedIn content.

---

## Automation

See **[agents/AUTOMATION.md](./AUTOMATION.md)** for GitHub Actions setup (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) and one-push-one-agent workflow. Manual steps remain in **[agents/RUNBOOK.md](./RUNBOOK.md)**.
