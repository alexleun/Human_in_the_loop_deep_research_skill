# Phase 2: Propose — Research Design

**Who drives:** LLM (writes artifacts), Human (approves/redirects)

**Purpose:** Formalize the research plan as an OpenSpec change.

## Artifacts

Created via `/opsx-propose`:
- `proposal.md` — Research questions, scope, non-goals
- `design.md` — Methodology, data sources, analytical approach, web output plan
- `tasks.md` — Implementation steps broken into phases (~2hr per task)
- `specs/<capability>/spec.md` — Detailed requirements per capability

## Key Decisions to Capture

- Which data sources are authoritative vs secondary?
- How will sources be cached for fact-checking?
- What analytical methods fit the data type?
- What output languages are needed?
- What visual assets are needed? (maps, charts, diagrams)
- What would cause conclusions to change?
- **What data-source IDs will findings carry?** Specify in the proposal, not retrofitted in Phase 7. Each finding should be pre-assigned a source ID so that `data-source` attributes are written during Phase 5, not added after.
- **What confidence levels apply?** Define the threshold for HIGH/MEDIUM/LOW per dimension — prevents inconsistency across reports.
- **What verification points are needed?** For quantitative research, specify which CSV values will be cross-checked against authoritative sources.
- **What is the fallback strategy?** If the system depends on a database or live API, define sample/fallback data so the system is always demonstrable even when the data store is empty.
- **How will code be validated before delivery?** Specify the run command, smoke test, or `--check` flag that confirms the system works (e.g., `uvicorn app.main:app`, `streamlit run dashboard.py`, `pytest`).
- **What is the scope boundary?** Estimate total tasks. If the estimate exceeds 15-20, the proposal likely spans multiple changes. Split by output type (data pipeline vs knowledge base vs web pages) and make the first change focused and shippable.
- **What would trigger a spin-off?** Define the event horizon: "If we find more than X facts in phase 3, spin off KB pages to a new change." Decide this before collection begins.

---

## End Conditions (NEW in v2.0)

This phase is **complete** when ALL of the following are true:

1. ✅ `proposal.md` exists with research questions, scope, non-goals
2. ✅ `design.md` exists with methodology, data sources, analytical approach, output plan
3. ✅ `tasks.md` exists with implementation steps (~2hr per task)
4. ✅ `specs/<capability>/spec.md` exists with detailed requirements
5. ✅ Data-source IDs and confidence levels are pre-assigned (not retrofitted)
6. ✅ Fallback strategy and code validation plan are defined
7. ✅ Scope boundary determined (task count ≤ 20 or spin-off plan documented)
8. ✅ Human has approved the proposal
