# RLF Pipeline Automation

Multi-agent automation for the Reverse Learning Framework content pipeline.  
**Orchestrator** = deterministic Python (no LLM). **Sub-agents** = OpenAI or Anthropic APIs via GitHub Actions.

---

## How it works

```
push to feature/* or pipeline/* branch
        │
        ▼
  scripts/orchestrate.py  ──► next_agent: drafter | critic | reviser | ...
        │
        ▼
  scripts/run_agent.py    ──► calls GPT or Claude per agents/0N_*.md
        │
        ▼
  git commit + push       ──► triggers next agent on following push
```

One workflow run = **one agent**. The chain continues on each push until `human` (approval needed) or `done`.

---

## Setup (required once)

### 1. GitHub repository secrets

Repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret | Used by |
|--------|---------|
| `OPENAI_API_KEY` | Drafter, Reviser, Verifier |
| `ANTHROPIC_API_KEY` | Critic, Finalist, Publisher |

Optional **Variables** (not secrets):

| Variable | Default |
|----------|---------|
| `OPENAI_MODEL` | `gpt-4o` |
| `ANTHROPIC_MODEL` | `claude-sonnet-4-20250514` |

Without secrets, the workflow still runs the **Orchestrator** and posts a commit comment telling you which agent to run manually.

### 2. Branch + state + brief

On a feature branch (e.g. `feature/rlf-verification-log-v1`):

- `briefs/<pipeline_id>.md` — filled brief
- `state.json` — copy from `state.json.template`, set `pipeline_id` to match brief filename

### 3. Start the pipeline

**Option A — GitHub Actions (recommended)**

Push `state.json` or run workflow manually:

Actions → **RLF Multi-Agent Pipeline** → **Run workflow** → branch → (optional) force_agent

**Option B — Local (company PC / Mac)**

```bash
pip install -r scripts/requirements.txt
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...

python scripts/orchestrate.py
python scripts/run_agent.py --agent drafter   # use printed next_agent
git add -A && git commit -m "pipeline: drafter output" && git push
```

Each push triggers the next agent in GitHub Actions.

**Option C — Cursor IDE**

Open repo on `feature/*` branch. Rules in `.cursor/rules/rlf-pipeline.mdc` inject pipeline context. You can run scripts from the integrated terminal or ask the agent to run `orchestrate.py` and `run_agent.py`.

---

## Human gates (not automated)

| Gate | How |
|------|-----|
| **Approve final for main** | Merge PR on GitHub |
| **Authorize Publisher** | Edit `state.json`: `"publish_authorized": true` and push |
| **Actual Brunch / LinkedIn post** | Human posts; update `posts/*` frontmatter |

Set approval in `state.json`:

```json
"human_gates": {
  "approved": true,
  "approved_at_utc": "2026-05-27T12:00:00Z",
  "approved_by": "Changhan Ryu",
  "publish_authorized": true
}
```

---

## Verification Log project (current)

| Item | Value |
|------|-------|
| Branch | `feature/rlf-verification-log-v1` |
| Brief | `briefs/rlf-log-verification-v1.md` |
| `pipeline_id` | `rlf-log-verification-v1` |
| Target file | `RLF-Log-Verification-v1.0.md` (Finalist writes under `final/v1.0.md` first; you may rename on release) |

**First automated step:** push `state.json` on the feature branch → Orchestrator routes to **drafter** → creates `drafts/v1.md`.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Workflow does nothing | Branch must match `feature/**`, `pipeline/**`, or `feat/**` |
| "Missing secrets" comment | Add API keys in repo secrets |
| Infinite workflow loops | Commits include `[skip ci]` for bot commits; if needed, disable Actions temporarily |
| Critic JSON invalid | Re-run workflow with `force_agent: critic` or fix JSON manually |
| Wrong next agent | Run `python scripts/orchestrate.py` locally and inspect `reason` |

---

## Files

| Path | Role |
|------|------|
| `scripts/orchestrate.py` | CLI router |
| `scripts/run_agent.py` | CLI agent runner |
| `scripts/rlf_lib/` | Library |
| `.github/workflows/rlf-pipeline.yml` | CI automation |
| `agents/RUNBOOK.md` | Manual fallback (always valid) |

Manual RUNBOOK remains the source of truth when APIs, secrets, or corporate policy block automation.
