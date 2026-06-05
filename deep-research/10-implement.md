# Phase 10: Implement — Research-to-Application Bridge

**Who drives:** LLM (writes code), Human (reviews, approves design decisions)

**Purpose:** Bridge the gap between research outputs and runnable application code. This phase is triggered when research findings are ready to be consumed by a dashboard, API, interactive visualization, or other software artifact.

## When to Use

Use this phase when:
- Research is complete (Phases 1-8 done) and you need to build an interactive system from it
- A dashboard, API, or visualization needs to consume the research data model
- The design.md includes a system architecture that must be implemented
- You're handing off from deep-research to openspec-apply-change

Do NOT use this phase for:
- Pure research output (HTML reports, static documents, PDFs) — use Phase 5-6 instead
- Data collection or analysis — use Phase 3-4 instead

## Procedure

### Step 1: Schema Validation

Before writing any application code, reconcile the data model:

1. **Read the model files** — identify every SQLAlchemy/Django/Pydantic model the app will use
2. **Read migration files** — cross-check column names, types, and relationships
3. **Compare against the actual database** (if running):
   ```bash
   python -c "
   from app.models import YourModel
   model_cols = set(c.name for c in YourModel.__table__.columns)
   print('Model columns:', sorted(model_cols))
   "
   ```
4. **Flag mismatches** — if model columns differ from migration columns or DB schema, fix the models (they are the source of truth) and regenerate migrations
5. **Log schema state** — note which columns exist, what types they have, which are nullable

### Step 2: Seed Data Check

Determine whether the database has data the application needs:

1. Check table row counts: `SELECT COUNT(*) FROM table;` or `Model.query.count()`
2. If tables are empty but the research produced sample/knowledge-base data:
   - Write a seed script (`app/seed.py` or `project/seed/populate.py`)
   - The seed script should load data from research outputs (CSV, JSON, knowledge base)
   - Run the seed and verify row counts
3. If no real data exists yet, implement **fallback sample data** in the application (see Principle 10)

### Step 3: Application Scaffold

Set up the minimal runnable application:

1. Create the main entry point (FastAPI app, Streamlit dashboard, Flask server, etc.)
2. Wire up database connection (SQLAlchemy engine + session)
3. Implement a single health-check or status endpoint that confirms connectivity
4. Verify the application starts without errors

### Step 4: Smoke Test

After the application runs, verify it works end-to-end:

1. Start the application
2. Hit the health-check endpoint or load the landing page
3. If the app depends on a database with seed data, verify data renders correctly
4. If using fallback data, verify the fallback path works
5. Fix any runtime errors before proceeding — do not defer

### Step 5: Handoff to openspec-apply-change (if applicable)

If implementation is complex enough to warrant task tracking:

1. Create or update tasks in the change directory
2. Note in the task file: what was scaffolded, what seed data was loaded, what fallbacks exist
3. Load the `openspec-apply-change` skill to continue with structured task execution

## Artifacts

| Artifact | Required | Purpose |
|---|---|---|
| Schema validation log | Yes | Records model vs migration vs DB state; prevents silent drift |
| Seed script | If DB-backed | Makes data loading reproducible |
| Application entry point | Yes | `app/main.py`, `app/dashboard.py`, etc. |
| Smoke test output | Yes | Evidence that the system runs |

## Verification Gate

Before leaving this phase, confirm:

- [ ] Model field names match what consuming code references
- [ ] Application starts without errors
- [ ] Health-check or landing page responds
- [ ] Seed data (or fallback data) is visible in the application
- [ ] No deferred runtime errors — everything that runs, runs cleanly

---

## End Conditions (NEW in v2.0)

This phase is **complete** when ALL of the following are true:

1. ✅ Schema validation log exists (model vs migration vs DB reconciled)
2. ✅ Seed script written and executed (if DB-backed application)
3. ✅ Application entry point exists and starts without errors
4. ✅ Smoke test passed — health-check or landing page responds
5. ✅ Seed data (or fallback data) visible in the application
6. ✅ Handoff to openspec-apply-change completed (if applicable)
7. ✅ `task_state.json` updated
