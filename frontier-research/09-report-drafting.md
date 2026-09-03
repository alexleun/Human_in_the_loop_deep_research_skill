# Phase 9: Comprehensive Report Drafting

**Purpose:** Write the full technical report with a Discovery-First narrative and grounded citation, honoring the stress-tested matrix, the red-team analysis, and the calibration from earlier phases.

**Core method:** Discovery-First Narrative & Grounded Citation.

**Execution pattern:** Sub-sessions per chapter/part (parallel or sequential). Output `drafts/09-full-report-draft.md`.

---

## Procedure

1. **Gather authoritative inputs** — stress-tested matrix (Phase 5), convergence analysis (Phase 8), calibration (Phase 7), and the epistemic ledger (Phase 3).

2. **Structure the report.** The Draft MUST include these chapters:
   - **Executive Summary & System Architecture**
   - **First-Principles & Theoretical Foundation**
   - **State-of-the-Art (SOTA) & Multi-Source Triangulation**
   - **Red-Team Vulnerabilities & Trade-off Analysis**
   - **Cross-Domain Innovations & Future Trajectory**
   - **Implementation Roadmap & Engineering Recommendations**

3. **Adopt Discovery-First Framing.** Lead with claims about the technical world (what is true, what works, what will happen), not with the research process. Relegate methodology/limitations to an endnote. This is the engineering analogue of the shared Discovery-First principle.

4. **Enforce grounded citation.** Every key claim — especially performance metrics — MUST carry a source and an epistemic tag (e.g., `[Fact: SRC-001]`, `[Hypothesis: Lab Benchmark]`). Never cite an `Unsubstantiated_Speculation` claim from the matrix as established.

5. **Include an explicit "Epistemic Limitations & Systemic Blindspots" chapter** (mandated by the stress-test gate in Mode A, and generally good practice) so unverifiable claims are disclosed, not hidden.

6. **Write `drafts/09-full-report-draft.md`.**

---

## Output: drafts/09-full-report-draft.md

```text
# Executive Summary & System Architecture
Discovery-first: "The binding constraint is interconnect bandwidth, not compute."

# First-Principles & Theoretical Foundation
[derivation with citations]

# State-of-the-Art & Triangulation
[Fact: SRC-001], [Hypothesis: SRC-004]

# Red-Team Vulnerabilities & Trade-off Analysis
[from Phase 8 matrix + Phase 4 red-team]

# Cross-Domain Innovations & Future Trajectory
[from Phase 6]

# Implementation Roadmap & Engineering Recommendations
[calibrated by Phase 7]

# Epistemic Limitations & Systemic Blindspots (endnote)
[methodology, excluded claims]
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `drafts/09-full-report-draft.md` exists with all required chapters listed above
2. ✅ Discovery-First framing applied — claims about the technical world lead, methodology is in the endnote
3. ✅ Every key claim/performance metric is cited with a source and epistemic tag
4. ✅ No `Unsubstantiated_Speculation` claim is presented as established fact
5. ✅ The "Epistemic Limitations & Systemic Blindspots" chapter is present
6. ✅ The draft reflects the Phase 7 calibration (deliverable form, audience, focus)
7. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT write a methodology report or lit-review instead of a discovery-first technical narrative
- Do NOT present unverified claims as fact — respect the stress-tested matrix
- Do NOT omit the limitations/blindspots chapter to look more confident
- Do NOT proceed to Phase 10 before the complete draft exists
