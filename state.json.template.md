# `state.json.template` — How to Use

When starting a new pipeline run, copy `state.json.template` to `state.json` at the repo root, then fill in three fields:

1. **`pipeline_id`** — your slug (e.g., `student-checklist-v1`), lowercase-with-dashes. Same slug used for the pipeline branch (`pipeline/<slug>`).
2. **`artifact_type`** — one of: `paper | checklist | rubric | guide | one_pager | blog_source | education`.
3. **`target_version`** — start with `v1.0` for new artifacts; bump for revisions.

Optionally edit `score_threshold` (default 90) or `iteration_max` (default 3) if this particular run warrants different limits. Log the reason in your first `history` entry.

Everything else (latest_*, history, human_gates) gets filled in by the workflow as the pipeline progresses. See `agents/RUNBOOK.md` for which fields update at which step.

---

## First history entry (write this after your first real transition)

Once you complete Step 0 (brief committed) and Step 1 (first draft produced), add an entry like:

```json
{
  "at_utc": "2026-05-27T11:00:00Z",
  "from_stage": "kickoff",
  "to_stage": "drafting",
  "reason": "Brief committed. Drafter invoked manually per RUNBOOK Step 1.",
  "actor": "human",
  "rule_applied": null
}
```

Then update `current_stage` to match `to_stage`. The history array is append-only — never delete entries, even from failed runs. The failure log captures what went wrong; the history captures every transition. Together they form the audit trail.

---

## Quick validation

Before committing, you can sanity-check the JSON locally:

```powershell
Get-Content state.json | ConvertFrom-Json | Out-Null
```

(No output means valid JSON.) For full schema validation, paste the file into any JSON Schema validator with `agents/schema/state.schema.json`.
