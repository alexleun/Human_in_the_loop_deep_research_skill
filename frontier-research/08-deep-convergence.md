# Phase 8: Deep Analytical Convergence

**Purpose:** Apply first-principles derivation and quantified trade-off analysis to converge on the best technical path, honoring the calibration from Phase 7 and the stress-tested matrix from Phase 5.

**Core method:** First Principles & Trade-off Quantification.

**Execution pattern:** Sub-sessions per trade-off axis if large; otherwise inline. Output `evidence/08-deep-convergence.md`.

---

## Procedure

1. **Read calibration + matrix.** Load `project-state.json` → `user_constraints` (from Phase 7) and `evidence/05-stress-tested-matrix.json` (from Phase 5). Only matrix-verified claims may underpin the analysis.

2. **First-principles derivation.** For the selected technical paths, derive the relevant behavior from first principles:
   - **Physical / mathematical** — scaling laws, conservation constraints, information-theoretic bounds, complexity analysis
   - **Economic** — cost models, amortization, TCO
   - **Engineering** — feasibility, implementation complexity, reliability
   - Enforce **Calculations First**: build the derivation explicitly, do not assert results.

3. **Build the quantified trade-off matrix.** Compare candidate paths across dimensions:
   - **Performance** (throughput, latency, efficiency, quality)
   - **Complexity** (implementation, maintenance, integration risk)
   - **Cost** (capex, opex, energy, licensing)
   
   Each cell must cite its evidence anchor or derivation. Cells without a defensible value must be marked `[DATA DEFICIT: Requires Empirical Testing]` rather than guessed.

4. **Weight by user constraints.** Fold in the Phase 7 calibration (budget, timeline, preference) to rank options.

5. **Write `evidence/08-deep-convergence.md`** with the first-principles derivations and the trade-off matrix.

---

## Output: evidence/08-deep-convergence.md

```text
Research Question: which scaling path to recommend?
Trade-off Matrix (per path):
| Path            | Performance          | Complexity | Cost        | Anchor |
|-----------------|----------------------|------------|-------------|--------|
| Dense parallel  | X TF (derived)       | Med        | $Y/TF       | CLM-001 |
| Sparse/alg      | ~Z gain (derived)    | High       | [DATA DEFICIT] | CLM-002 |
Weighting: user budget-sensitive → favors sparse path if Z holds
Recommendation: pursue sparse/alg path subject to empirical validation of CLM-002
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `evidence/08-deep-convergence.md` exists
2. ✅ First-principles derivations are explicit (no asserted numerical results)
3. ✅ A multi-dimensional trade-off matrix (Performance / Complexity / Cost) is built and populated
4. ✅ Every trade-off value is derived, cited, or marked `[DATA DEFICIT]`
5. ✅ User constraints from the Phase 7 calibration are applied to the ranking
6. ✅ The stress-tested matrix is honored (no excluded claim underpins the analysis)
7. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT assert a trade-off value without derivation, citation, or `[DATA DEFICIT]` — the guardrails are mandatory
- Do NOT ignore the Phase 7 calibration when ranking options
- Do NOT reverse a stress-test verdict for convenience
- Do NOT proceed to Phase 9 before the convergence analysis is complete
