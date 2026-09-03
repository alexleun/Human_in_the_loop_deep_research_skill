# Phase 7: Mid-Term Alignment & User Interactive Calibration

**Purpose:** Present all intermediate findings to the user and dynamically calibrate the research direction, report structure, and constraints to the user's real-world conditions before deep convergence.

**Core method:** User-Driven Constraint Modification.

**Execution pattern:** Conversational, run in the main session with the human. This is a **human sign-off gate** — mandatory before Phase 8.

---

## Procedure

1. **Assemble the intermediate picture.** Present to the user, concisely:
   - The systems map from Phase 1
   - The red-team findings from Phase 4
   - The stress-tested matrix + selected fork from Phase 5
   - The innovation hypotheses from Phase 6

2. **Surface the calibration choices.** Ask the user about real-world conditions that should shape the final report:
   - **Budget / cost constraints**
   - **Timeline / schedule**
   - **Engineering / technical preference** (e.g., preferred stack, risk tolerance, constraints)
   - **Target deliverable form** (full report, brief, decision memo, slide deck) and audience
   - **Special focus** areas to emphasize or de-emphasize

3. **Update `project-state.json` → `user_constraints`.** Fold the user's answers into `target_deliverable`, `special_focus`, and `accepted_sources` (and any new constraint fields).

4. **Redirect remaining analysis.** Adjust the Phase 8 convergence scope, the Phase 9 report chapter structure, and the Phase 10 audit criteria to reflect the calibrated direction.

5. **Record a human sign-off** that the direction is approved before proceeding to convergence.

---

## Output

- `project-state.json` with updated `user_constraints`
- A recorded calibration decision (in the project state or a short `evidence/07-calibration-note.md`)

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Intermediate findings (system map, red-team, stress-test matrix, innovations) are presented to the user
2. ✅ User's real-world constraints (budget/timeline/technical preference/deliverable) are captured
3. ✅ `project-state.json` → `user_constraints` is updated accordingly
4. ✅ Phase 8 / Phase 9 scope and chapter structure are adjusted to the calibrated direction
5. ✅ **Human sign-off recorded** — the direction is explicitly approved before Phase 8

---

## What NOT to Do

- Do NOT skip this gate — deep convergence without user calibration risks an off-target deliverable
- Do NOT proceed to Phase 8 without an explicit human sign-off
- Do NOT present micro-details; show the strategic picture (system map, forks, trade-offs)
- Do NOT let red-team or stress-test findings be overridden by the user's preference at the expense of evidence — surface conflicts explicitly
