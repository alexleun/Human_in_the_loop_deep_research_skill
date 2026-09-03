# Cross-Session State Management (v1.0)

Enables continuing a frontier-research project across sessions via a `project-state.json` checkpoint read on session start and updated after each meaningful action.

## The Problem

A large engineering/science research project spans multiple LLM sessions. When a new session starts (or work resumes later), it has no context about:
- What phase is in progress
- What claims were verified / unverified / falsified
- What the user calibrated
- Whether the epistemic stress-test gate passed

## The Solution: `project-state.json`

Each project root gets a `project-state.json` read on session start and updated at every phase transition and calibration gate.

```json
{
  "project_id": "frontier-res-001",
  "topic": "frontier tech research topic",
  "domain": "Engineering/Physics/AI/BioTech",
  "current_phase": "03-epistemic-ledger.md",
  "user_constraints": {
    "target_deliverable": "Comprehensive Technical Report",
    "special_focus": ["Scaling Laws", "Thermal Management"],
    "accepted_sources": ["ArXiv", "Patents", "Code Repos", "Raw CSV", "Web"]
  },
  "epistemic_ledger": {
    "verified_facts": [],
    "unverified_claims": [],
    "falsified_hypotheses": []
  },
  "sub_sessions": []
}
```

### Key fields

| Field | Purpose | Updated By |
|---|---|---|
| `current_phase` | Which phase file is active; used to resume | Every phase transition |
| `user_constraints` | Deliverable form, special focus, accepted sources | **Phase 7 calibration gate** |
| `epistemic_ledger.verified_facts` | `[Fact]` claims | Phase 3 (ledger) |
| `epistemic_ledger.unverified_claims` | `[Hypothesis]` / `[Speculation]` / ambiguous claims | Phase 3 (ledger) |
| `epistemic_ledger.falsified_hypotheses` | Claims contradicted by evidence (feed Phase 4 red-team) | Phase 3 (ledger) |
| `sub_sessions` | Status + outputs of completed sub-sessions | PM after each sub-session |

## Resume Workflow

On session start (new machine or new session):
1. Load this skill
2. Read `project-state.json`
3. Read `current_phase` and load the corresponding phase file
4. Read `epistemic_ledger` — honor verified/falsified/unverified statuses
5. Read `user_constraints` — the deliverable must fit these
6. Read the key outputs produced so far (system map, ledger, red-team, stress-test matrix)
7. Present a resume summary to the human before continuing

## Status Change Discipline

- After each phase transition, update `current_phase` and append any new `sub_sessions` entry
- After Phase 3, sync `epistemic_ledger` with `evidence/03-epistemic-ledger.md`
- After Phase 7, update `user_constraints`
- After Phase 5, record that the stress-test gate passed and note the `evidence/05-stress-tested-matrix.json` path
- If a claim is later falsified (Phases 4–5), move it from `verified_facts`/`unverified_claims` to `falsified_hypotheses`
