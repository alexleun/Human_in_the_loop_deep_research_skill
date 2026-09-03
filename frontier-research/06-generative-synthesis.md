# Phase 6: Generative Synthesis & Divergent Thinking

**Purpose:** Overcome premature convergence by forcing cross-domain abstraction and counterfactual reasoning, generating novel innovation candidates from the stress-tested evidence base.

**Core method:** Lateral Thinking & Cross-Domain Transfer.

**Execution pattern:** Sub-sessions per innovation direction (parallel). Output `evidence/06-innovative-synthesis.md`.

---

## Procedure

1. **Consume the stress-tested matrix.** Read `evidence/05-stress-tested-matrix.json`. Only claims with a `Verified_Axiom` or (flagged) `Inferred_Bridge` status may appear as premises. **Do NOT** present `Unsubstantiated_Speculation` claims as established fact.

2. **Force Cross-Domain Abstraction.** Actively borrow mechanisms from unrelated domains to break fixation:
   - Biology ↔ distributed computing
   - Fluid dynamics ↔ chip thermal management
   - Ecology/finance feedback models ↔ scalability dynamics
   - Label each such candidate as an `innovation_candidate` with its source domain.

3. **Run Counterfactual Reasoning.** Ask: *"If the current core assumption (e.g., Moore's Law, a scaling law) completely fails, how should the system be architected?"* Derive the fallback architecture and note what breaks.

4. **Generate innovation candidates.** For each candidate record: the mechanism, the borrowed source domain, the evidence anchor (must respect the stress-tested matrix), and the expected benefit/risk.

5. **Apply guardrails.** Any quantitative benefit claim must be **derived** (Calculations First), carry a citation (Citation Requirement), or be marked `[DATA DEFICIT: Requires Empirical Testing]` (Uncertainty Quantification).

6. **Write `evidence/06-innovative-synthesis.md`.**

---

## Output: evidence/06-innovative-synthesis.md

```text
Innovation Candidate 1:
  Mechanism: Latency-insensitive batching decouples throughput from per-step latency
  Source domain: distributed systems / queueing theory
  Evidence anchor: CLM-005 (Verified_Axiom); benefit derived: ~X% utilization gain (scripted)
  Risk: applies only where scheduling overhead is amortized

Counterfactual: if dense scaling floors,
  Fallback architecture: sparse + heterogeneous specialization
  What breaks: single-kernel performance assumptions, tooling maturity
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `evidence/06-innovative-synthesis.md` exists
2. ✅ At least one cross-domain abstraction/transfer candidate is captured with a named source domain
3. ✅ At least one counterfactual scenario ("core assumption fails → how to architect") is recorded
4. ✅ No `Unsubstantiated_Speculation` claim from the matrix is presented as established fact
5. ✅ Every quantitative benefit is derived, cited, or marked `[DATA DEFICIT]`
6. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT present excluded/unverified claims as fact — the stress-tested matrix gates this
- Do NOT stop at the dominant technical narrative; force at least one non-mainstream direction
- Do NOT assert a quantitative benefit without deriving, citing, or flagging it
- Do NOT proceed to Phase 7 before the innovation synthesis is complete
