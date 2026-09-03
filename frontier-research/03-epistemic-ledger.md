# Phase 3: Epistemic Fact-Checking & Triangulation

**Purpose:** Validate every technical claim against the sources from Phase 2 using the triangulation rule, and label each claim's epistemic status into an `epistemic_ledger`.

**Core method:** Epistemic First Principles & Triangulation.

**Execution pattern:** Sub-sessions per domain/claim cluster if large; otherwise inline. Output `evidence/03-epistemic-ledger.md`.

---

## Procedure

1. **Extract claims** from the harvested sources: every performance metric, capability assertion, feasibility statement, and technical mechanism.

2. **Enforce the Triangulation Rule:**
   - Any technical claim MUST be corroborated by **at least 2 independent sources** to be treated as verified.
   - "Independent" means different primary origins (a paper + its own code/reproduction, a patent + measured data, two unrelated papers) — not the same number recycled across web pages.

3. **Label each claim's epistemic status:**

   | Label | Meaning | Allowed in final report as fact? |
   |---|---|---|
   | **[Fact]** | Fully verified by experiment / math / code, and triangulated by ≥2 independent sources | Yes |
   | **[Hypothesis]** | Theoretical derivation but lacking scaled validation, or single-source corroboration | Only with explicit caveat |
   | **[Speculation]** | Industry/single-seller claim or no public data | No — must be flagged |

4. **Maintain the epistemic ledger.** Append each claim to the relevant bucket in `project-state.json` → `epistemic_ledger`:
   - `verified_facts` — [Fact] claims
   - `unverified_claims` — [Hypothesis] / [Speculation] / ambiguous claims awaiting validation
   - `falsified_hypotheses` — claims contradicted by evidence, noted for red-team use in Phase 4

5. **Write `evidence/03-epistemic-ledger.md`** as a readable ledger with full claim → source → status mappings.

---

## Output: evidence/03-epistemic-ledger.md

```text
CLM-001 | [Fact]        | "FP8 matmul is ~2x raw FLOPs throughput vs FP16 on this silicon"  | SRC-001 (benchmark) + SRC-003 (reproduction) | confidence: high
CLM-002 | [Hypothesis]  | "Contention collapses throughput non-linearly past 85% utilization" | SRC-004 | single-source, needs scaletc check
CLM-003 | [Speculation] | "<vendor> next-gen will fully replace alternatives by 2027"        | SRC-006 (vendor web) | ephemeral/low-trust
```

Your epistemic ledger MUST stay in sync with the `epistemic_ledger` in `project-state.json`.

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Every claim from Phase 2 sources is extracted and assigned `[Fact]` / `[Hypothesis]` / `[Speculation]`
2. ✅ The triangulation rule (≥2 independent sources for [Fact]) is applied and documented per claim
3. ✅ `evidence/03-epistemic-ledger.md` exists with full claim → source → status mappings
4. ✅ `project-state.json` → `epistemic_ledger` is updated (verified_facts / unverified_claims / falsified_hypotheses)
5. ✅ No [Fact] label is present without corroboration — any under-corroborated claim is labeled [Hypothesis] or [Speculation]
6. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT label a claim [Fact] with only one source — the triangulation rule is mandatory
- Do NOT invent sources or fabricate corroboration to upgrade a claim
- Do NOT drop contradictory evidence into the ledger silently — record it in `falsified_hypotheses` for Phase 4 red-teaming
- Do NOT proceed to Phase 4 before the ledger is complete and in sync with `project-state.json`
