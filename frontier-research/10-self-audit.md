# Phase 10: Self-Correction Audit & Deliverable Finalization

**Purpose:** Perform an adversarial proofreading pass of the draft, scan for speculation mislabeled as fact, align the deliverable with the user's latest constraints, and produce the final report.

**Core method:** Adversarial Proofreading.

**Execution pattern:** Conversational/sub-session with the human. Output `FINAL_DELIVERABLE_REPORT.md`.

---

## Procedure

1. **Gather audit inputs** — the draft (`drafts/09-full-report-draft.md`), the stress-tested matrix (`evidence/05-stress-tested-matrix.json`), the epistemic ledger (`evidence/03-epistemic-ledger.md` + `project-state.json`).

2. **Hallucination & bias scan.**
   - Check whether any `[Speculation]` / `Unsubstantiated_Speculation` claim was written as `[Fact]`
   - Verify every performance metric carries a citation + epistemic tag
   - Verify no inference bridge was silently upgraded without the required flag
   - Verify the limitations/blindspots chapter is present and honest

3. **Constraint alignment.**
   - Re-read the user's latest description and `project-state.json` → `user_constraints`
   - Ensure the deliverable fully fits the real-world conditions (deliverable form, audience, focus, budget/timeline constraints)
   - Adjust chapters, emphasis, or scope as needed

4. **Adversarial re-read.**
   - Read the report as a hostile expert: hunt for overclaims, hidden assumptions, and ungrounded numbers
   - Apply the same steel-man/red-team discipline used in Phases 4–5 to the report's own conclusions

5. **Finalize.**
   - Incorporate corrections
   - Produce `FINAL_DELIVERABLE_REPORT.md` (in the form calibrated in Phase 7)
   - Append a final batch note documenting the audit findings and any residual `[DATA DEFICIT]` items

---

## Output

- `FINAL_DELIVERABLE_REPORT.md` (the published deliverable)
- Optional: `evidence/10-audit-log.md` recording the audit findings and corrections

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `FINAL_DELIVERABLE_REPORT.md` exists in the calibrated deliverable form
2. ✅ Hallucination scan passed — no `[Speculation]` / `Unsubstantiated_Speculation` claim presented as `[Fact]`
3. ✅ Every performance metric carries a citation + epistemic tag
4. ✅ The limitations/blindspots chapter is present and honest
5. ✅ The deliverable is aligned with the user's latest constraints and `user_constraints`
6. ✅ Adversarial re-read completed without an actionable unfixed overclaim
7. ✅ Final batch note appended documenting audit findings and residual `[DATA DEFICIT]` items

---

## What NOT to Do

- Do NOT skip the hallucination scan — this is the last line of defense before delivery
- Do NOT deliver a form other than the one calibrated in Phase 7 without flagging it
- Do NOT hide residual `[DATA DEFICIT]` items — disclose them honestly
- Do NOT present the skill as done until `FINAL_DELIVERABLE_REPORT.md` passes the audit
