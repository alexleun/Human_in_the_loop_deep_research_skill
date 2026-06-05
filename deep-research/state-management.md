# Cross-Machine / Cross-Session State Management (v2.0)

Enables continuing work across sessions or on a different computer via git + `task_state.json` checkpoints.

**v2.0 update:** This pattern is now promoted from "optional technique" to **recommended practice** for any multi-session project. While a single session with continuous human guidance may not need it, any project spanning 2+ sessions benefits from structured state tracking.

## The Problem

When switching machines, git syncs **files** but the new LLM session has zero context about:
- What task was in progress
- What partial findings were discovered
- Why work was paused
- What decisions the human made

## The Solution: `task_state.json`

Each change directory gets a `task_state.json` read on session start and updated after each meaningful action.

**Location:** `openspec/changes/<change-name>/task_state.json`

```json
{
  "change_name": "<change-name>",
  "topic": "brief description",
  "last_updated": "2026-05-22T09:30:00Z",
  "current_phase": "data-collection",
  "current_task_id": "3.2",
  "status": "in_progress",
  "completed_tasks": ["1.1", "1.2", "1.3", "2.1", "2.2", "3.1"],
  "context_summary": "Free-text summary of what was done, learned, and where things stand. Write enough for a fresh LLM to reconstruct context.",
  "pending_decisions": [
    {
      "id": "pd-001",
      "question": "API returned 403. Use fallback?",
      "options": ["Use fallback (recommended)", "Wait", "Find alternative"],
      "decision": "Use fallback",
      "decided_by": "human",
      "date": "2026-05-21"
    }
  ],
  "last_action": "Completed task 3.1: description",
  "next_action": "Task 3.2: description",
  "key_findings_so_far": ["Notable discoveries to date"],
  "warnings": ["Data quality issues, access problems"],
  "next_session_instructions": "Where to pick up"
}
```

## Resume Workflow

**On session start (new machine):**
1. Load this skill
2. Read `task_state.json`
3. Read change artifacts for full context
4. Read last 10 git commits
5. Read output files from completed tasks
6. Present resume summary to human:
   ```
   ## Resume: <change-name>
   **Phase:** <phase> (task <current>/<total>)
   **Last:** ✓ <last_action>
   **Next:** <next_action>
   **Context:** <summary>
   **Pending:** <count> decisions
   Continue? [Y/n]
   ```
7. On confirmation, continue from `current_task_id`

**After each meaningful step:**
1. Update `task_state.json` — move task, update actions, log findings
2. Commit + push:
   ```bash
   git add openspec/changes/<name>/task_state.json
   git commit -m "feat(<name>): task <id> — <description>"
   git push
   ```

## Git Commit Convention

```
<type>(<change-name>): task <task-id> — <description>

Types: feat, fix, docs, data, web, chore

Examples:
feat(gba-flows): task 3.1 — fetched capital flow data
web(gba-flows): task 5.1 — generated landing page
fix(gba-flows): task 3.2 — corrected HAC standard errors
```

`git log --oneline` becomes a browsable task history any LLM can parse.
