# RUNBOOK — How to Operate the RLF Pipeline Today (Manual Mode)

> Before automation, the pipeline runs by hand. This runbook tells you exactly what to do, where to do it, and how to know it worked. Once this manual loop is comfortable, Phase 1b will automate the steps that don't need a human.

**Audience:** The repo owner (Changhan Ryu) and any future collaborator running an RLF artifact through the multi-agent pipeline.

**Prerequisite reading:** `agents/README.md` (architecture overview). You don't need to memorize it — keep it open in another tab.

---

## TL;DR — the 7 manual steps

| # | What | Where | Who acts |
|--:|---|---|---|
| 0 | Write a brief in `briefs/<slug>.md` and commit | Mobile (GitHub app) or Cursor Web | You |
| 1 | Run **Drafter** prompt with the brief → save output to `drafts/v1.md` | Mobile ChatGPT | You (paste, copy result) |
| 2 | Run **Critic** prompt in Cursor Web on the latest draft | Cursor Web (browser) | You (paste prompt, agent reads repo) |
| 3 | If score < 90: run **Reviser** prompt with draft + review → `drafts/v2.md`. Repeat 2–3 with each new version, max 3 iterations. | Mobile ChatGPT + Cursor Web | You |
| 4 | When score ≥ 90 OR iter == 3: run **Finalist** prompt → `final/v{ver}.md` | Cursor Web | You |
| 5 | Run **Verifier** prompt on the final → `verification/v{ver}-check.md` | Mobile ChatGPT | You |
| 6 | Open PR on the branch, review on mobile, **Approve & Merge** | GitHub mobile / browser | You |
| 7 | Run **Publisher** prompt for Brunch (KR) + LinkedIn (EN) drafts → `posts/` | Cursor Desktop (Mac/PC) preferred | You |

Each step ends with a commit. Git is the handoff mechanism.

---

## Environment cheat sheet

| Environment | When to use it | Why |
|---|---|---|
| **Mobile — ChatGPT app** | Steps 1, 3 (Drafter, Reviser), 5 (Verifier) | GPT-family work; available even in restricted corporate environments |
| **Mobile — GitHub app** | Steps 0, 6 (commit / approve / merge) | Single-tap workflow; works on commute |
| **Cursor Web (corporate browser)** | Steps 2 (Critic), 4 (Finalist) | Reads repo directly; no file upload needed |
| **Cursor Desktop (Mac at home or PC)** | Step 7 (Publisher), occasional override | Best for interactive polishing of Brunch/LinkedIn drafts |

**Key principle:** every step reads from git and writes to git. You never carry a file between apps; you carry only a commit hash (or a branch name) in your head.

---

## Naming conventions (memorize these)

- **Pipeline branch:** `pipeline/<pipeline-id>` — e.g. `pipeline/student-checklist-v1`
- **Brief file:** `briefs/<slug>.md`
- **Draft files:** `drafts/v1.md`, `drafts/v2.md`, ... (iteration number)
- **Review files:** `reviews/v1-review.json` + `reviews/v1-review.md` (paired)
- **Final file:** `final/v1.0.md` (semver, NOT iteration)
- **Verification file:** `verification/v1.0-check.md` (re-runs append `-2`, `-3`, etc.)
- **Post files:** `posts/brunch_v1.0_ko.md`, `posts/linkedin_v1.0_en.md`
- **State file:** `state.json` at repo root (one per branch)

---

## Step 0 — Kickoff: write the brief

### 0.1 Create a brief

Copy `briefs/_template.md` to `briefs/<your-slug>.md`. Fill it in. The slug should be lowercase-with-dashes and match what you'll use for the pipeline branch.

Example briefs already provided:

- `briefs/example-student-checklist.md` — a worked example you can copy from.

### 0.2 Create a pipeline branch

Branch name = `pipeline/<your-slug>`. From any environment:

**Mobile (GitHub app):** Branch dropdown → New branch → name it `pipeline/<your-slug>` based on `main`.

**Cursor Web / Desktop:**
```bash
git checkout main && git pull
git checkout -b pipeline/<your-slug>
```

### 0.3 Initialize `state.json` for this pipeline

Copy `state.json.template` to `state.json` at the repo root. Fill in:

- `pipeline_id` — same as your slug
- `artifact_type` — one of: `paper | checklist | rubric | guide | one_pager | blog_source | education`
- `target_version` — start with `v1.0`
- `current_stage` — `kickoff`

Commit:

```
chore(pipeline): kickoff <slug> — brief and state initialized
```

---

## Step 1 — Drafter (mobile ChatGPT)

### 1.1 Open ChatGPT mobile, start a new conversation

### 1.2 Paste the Drafter prompt

The full system prompt is in `agents/01_drafter.md`. Copy the block inside the triple backticks (`## System prompt` section). Then send it as your first message.

After ChatGPT acknowledges the role, send your second message with the brief content:

> Here is the brief. Produce `drafts/v1.md` per the system prompt.
>
> [paste the contents of `briefs/<slug>.md`]

### 1.3 Save the output

ChatGPT will produce the complete `drafts/v1.md` content. Copy the full markdown.

### 1.4 Commit the draft (mobile GitHub app)

GitHub app → Repository → your `pipeline/<slug>` branch → **Add file** → Create new file → path: `drafts/v1.md` → paste content → Commit:

```
feat(draft): v1 by Drafter (gpt-5) for <slug>
```

### 1.5 Update `state.json`

GitHub app → edit `state.json` → set `current_stage: "critiquing"`, `latest_draft: "drafts/v1.md"`, append a history entry. Commit:

```
chore(state): drafting → critiquing
```

---

## Step 2 — Critic (Cursor Web)

### 2.1 Open Cursor Web in your corporate browser, point at `fluent93/reverse-learning` on branch `pipeline/<slug>`

### 2.2 In the chat, paste the Critic prompt from `agents/02_critic.md`

(Just the `## System prompt` block.)

### 2.3 Second message:

> Please review `drafts/v1.md` per the rubric in `agents/rubrics/rlf-core-rubric.md`. Produce both files: `reviews/v1-review.json` and `reviews/v1-review.md`. Conform JSON to `agents/schema/review.schema.json`.

### 2.4 Cursor Web will write both files directly into the repo (this is what makes the corporate environment workable — no file upload required).

### 2.5 Commit both files in the same commit:

```
feat(review): v1 critic review — <total_score>/100 — <FINALIZE|REVISE>
```

### 2.6 Update `state.json`:

- `latest_review: "reviews/v1-review.json"`
- `latest_total_score: <n>`
- `current_stage: "revising"` if score < 90, else `"finalizing"`

---

## Step 3 — Reviser loop (mobile ChatGPT)

Only if Critic recommended REVISE. Skip to Step 4 if FINALIZE.

### 3.1 Mobile ChatGPT, new conversation

Paste the Reviser prompt from `agents/03_reviser.md`.

### 3.2 Send:

> Here is `drafts/v1.md`: [paste content]
>
> Here is `reviews/v1-review.json`: [paste content]
>
> Here is `reviews/v1-review.md`: [paste content]
>
> Produce `drafts/v2.md` per the Reviser system prompt. Include the Reviser Changelog.

### 3.3 Commit `drafts/v2.md` (mobile GitHub app):

```
feat(draft): v2 by Reviser — addressed <N> issues from v1 review
```

### 3.4 Update `state.json`: increment `iteration`, set `latest_draft: "drafts/v2.md"`, `current_stage: "critiquing"`.

### 3.5 Loop back to Step 2 with the new version number.

**Iteration cap:** maximum 3 Critic↔Reviser cycles. After iteration 3, regardless of score, proceed to Step 4 with `escalation_reason: "iter_max"` in `state.json`.

---

## Step 4 — Finalist (Cursor Web)

### 4.1 Cursor Web, paste the Finalist prompt from `agents/04_finalist.md`

### 4.2 Send:

> Produce `final/v1.0.md` from the latest draft and all reviews in this branch. Follow the system prompt. Use `state.target_version` for the filename.

### 4.3 Verify the output includes:

- Frontmatter with all required fields
- Body of the artifact
- Ownership Statement section
- Open Items for Verifier section
- Known Quality Risks section *only if* `escalation_reason: "iter_max"`

### 4.4 Commit:

```
feat(final): v1.0 by Finalist — ready for verifier
```

### 4.5 Update `state.json`: `current_stage: "verifying"`, `latest_final: "final/v1.0.md"`.

---

## Step 5 — Verifier (mobile ChatGPT)

### 5.1 Mobile ChatGPT, paste the Verifier prompt from `agents/05_verifier.md`

### 5.2 Send:

> Verify `final/v1.0.md` against the canon and the artifact's own claims. Produce `verification/v1.0-check.md` with all checks A1–F3.

### 5.3 Paste in the following content (all of it — Verifier needs all of this in context):

- `final/v1.0.md`
- `Reverse Learning Framework One-Pager.md`
- `RLF-Checklist-AIOutputReview-v1.0.md`
- (If a prior `final/` exists) the prior final file

### 5.4 Receive the verifier report. Commit:

```
feat(verify): v1.0 verifier — <PASS|PASS_WITH_FLAGS|FAIL>
```

### 5.5 Update `state.json` based on verdict:

- **PASS / PASS_WITH_FLAGS** → `current_stage: "awaiting_human_approval"`
- **FAIL** → `current_stage: "remediation"`. Go back to Step 3 (Reviser fixes specific findings, then Critic re-reviews, then Finalist re-runs).

---

## Step 6 — Human approval and merge (mobile GitHub app)

### 6.1 Open a PR from `pipeline/<slug>` → `main`

Title: `RLF Pipeline — <slug> v1.0`

Body: paste a quick summary including final Critic score, verifier verdict, and any "items the human must personally verify" from the verification report.

### 6.2 Read the final file on mobile. Look specifically at:

- Ownership Statement (does it represent you accurately?)
- Open Items for Verifier (are the listed claims things you can confirm?)
- Known Quality Risks (if present — accept or block)

### 6.3 If everything checks out, **Approve** the PR and **Merge** to main.

### 6.4 If anything needs fixing, post a PR comment with what's wrong and route back to Reviser (Step 3) manually.

---

## Step 7 — Publisher (Cursor Desktop preferred)

### 7.1 Pull main on your Mac (or PC Cursor Desktop):

```bash
git checkout main && git pull
git checkout -b publish/<slug>-v1.0
```

### 7.2 Open Cursor Desktop chat. Paste the Publisher prompt from `agents/06_publisher.md`

### 7.3 Send:

> Produce `posts/brunch_v1.0_ko.md` and `posts/linkedin_v1.0_en.md` from `final/v1.0.md`, honoring `verification/v1.0-check.md`.

### 7.4 Review both drafts. **Especially** the Brunch personal hook — that paragraph is the one place where lived context matters most. Edit by hand.

### 7.5 Commit + PR + Merge (similar to Step 6).

### 7.6 Manually publish to Brunch and LinkedIn from each app, then come back to update each post's frontmatter:

- `status: published`
- `canonical_url: <the public URL>`

Final commit:

```
docs(posts): mark v1.0 posts published
```

---

## Recovering from common problems

### Critic produced an invalid JSON

Open `reviews/v{n}-review.json` in any editor, fix the syntax (often a trailing comma or missing field), commit. If the structure looks fundamentally off, re-run Step 2 — the Critic was likely confused about the rubric.

### `state.json` got out of sync

Refer to `agents/schema/state.example.json` for the structure. The state file is a convenience for the Orchestrator (when it's automated later); you can manually recalculate `current_stage` by looking at which files exist in `drafts/`, `reviews/`, `final/`, `verification/`.

### You committed to `main` directly by mistake

Don't panic. The pipeline doesn't break — but the audit trail is muddier. In the next run, start with a clean `pipeline/` branch.

### Reviser ignored a major issue from the Critic

Open `drafts/v{n+1}.md`, scroll to the Reviser Changelog at the end. Either there's a DISAGREEMENT entry explaining why (legitimate), or the issue was silently skipped (regression). If the latter, post a PR comment quoting the missed issue and re-run Reviser with explicit emphasis on that issue.

### Verifier flagged something you can't independently check (e.g., a citation)

That's exactly what "Items the human must personally verify" is for. Look it up yourself, then either:

- Confirm and write a one-line note in the PR description, OR
- If unconfirmable, ask Reviser to remove or hedge the claim.

---

## Quality gates summary

| Gate | Who decides | What it gates |
|---|---|---|
| Critic ≥ 90 | Critic agent | Whether you skip the Reviser loop or enter it |
| Iteration cap (3) | Pipeline rule | Whether you re-iterate or escalate |
| Verifier PASS | Verifier agent | Whether you can ask for human approval |
| Human Approval | You | Whether the final ships at all |
| Publisher publish authorization | You | Whether distribution drafts get written |
| Actual post button | You | Whether anything goes public |

There are six gates. Four are automated agent decisions. **Two are you** — and you can override any of the automated ones by editing `state.json` directly with an explicit reason logged in `state.history`.

---

## When to graduate to Phase 1b (automation)

You're ready when:

- You've run the full manual loop end-to-end at least twice without referring to this runbook constantly.
- The Critic's scores feel calibrated — i.e., a 92/100 actually means publishable-with-light-polish, not "this needs another full revision".
- The Verifier's checks are catching at least one thing the Critic missed (proving the cross-family verification is doing real work).

At that point, the next PR adds GitHub Actions (or Cursor Background Agent triggers) to automate Steps 2, 4, and 5 — the ones that read the repo and produce structured output. Steps 1, 3, 6, and 7 stay manual because they involve either human input (briefs, approval, posting) or creative judgment that benefits from human iteration.
