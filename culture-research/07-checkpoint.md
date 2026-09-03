# Phase 7: Iteration Checkpoint (renumbered in v3.3)

**Purpose:** Review all 5 analysis rounds as a coherent arc and decide if synthesis can proceed or if loops are needed.

**Execution pattern:** Run as a sub-session (SS13 after the Phase 5 Audit Sub-session). Output is a verdict with accountable artifact.

**Input gate (NEW in v3.3):** Verify the Phase 5 stress-test completed — `stress-tested-matrix.json` exists and contains a valid `phase_meta` before the checkpoint can render a PROCEED verdict. The checkpoint SHALL NOT bypass the Epistemic Stress-Test Completion Gate.

---

## Procedure

### 1. Coherence Check
Do the research questions (Round 5) logically follow from the gaps (Round 4), contradictions (Round 3), and patterns (Rounds 1-2)? For each Round 5 question, trace the evidence chain back to source papers.

### 2. Grounding Audit (REFINED in v3.0)
For each research question in Round 5, use **three tiers** (not two):
- **Evidence-derived** — grounded in verified findings from full-text papers
- **Gap-derived** — grounded in documented gaps (legitimate, not speculative)
- **Speculative** — grounded in neither findings nor gaps (pure extrapolation)

For each question, verify that at least 2 source papers named in its motivation chain exist in the unified candidate list. Flag questions that cite non-existent papers.

### 3. Missing Dimension Scan (REFINED in v3.0)
Check systematically for dimensions that may have been overlooked across all rounds. Classify each by severity:
- **CRITICAL ABSENCE:** The dimension affects >10% of global population and has zero Tier A coverage (e.g., disability, informal economy)
- **UNDERREPRESENTED:** Only 1-2 papers touch it (e.g., technology, seasonality)
- **IMPLICIT ONLY:** Papers mention it but don't study it as a primary category (e.g., SES, life-stage transitions)

Standard dimensions:
- Gender
- Age / generation
- Socioeconomic class
- Technology penetration / digital divide
- Climate / geography
- Urban vs rural
- Seasonality
- Life stage transitions
- Disability / accessibility

If any are systematically absent, flag for Round 4 supplementation or accept and document.

### 4. Loop Decision (REFINED in v3.0)
If weak links, missing dimensions, or insufficient grounding found:
- Identify which round(s) need revisiting (Round 1-5)
- Specify what needs to be added
- **LOOP only if the identified gap can be closed within the existing paper set.** If the gap reflects a dimension with zero papers in the unified candidate list, flag it for the synthesis boundary section instead of looping. This prevents infinite loops.

If checkpoint passes, document "proceed to synthesis" decision.

### 5. Synthesis Readiness Assessment
Final verdict:
- **PROCEED:** all rounds coherent, questions grounded, no critical gaps
- **PROCEED WITH NOTES:** minor gaps that can be addressed in synthesis itself
- **LOOP:** one or more rounds need revisiting before synthesis

Provide a recommendation for synthesis structure (which sections, which questions to prioritize, which gaps to caveat).

---

## Output Format (REFINED to Match End Conditions)

```markdown
---
type: iteration-checkpoint
title: Iteration Checkpoint Review
created: YYYY-MM-DD
tags:
  - analysis/checkpoint
---

# Iteration Checkpoint — Round 6

## 1. Coherence Check
[For each Round 5 question, trace the evidence chain]

## 2. Grounding Audit
- Evidence-derived questions: {count and list}
- Gap-derived questions: {count and list}
- Speculative questions: {count and list}
- Paper existence verification: {passed/failed}

## 3. Missing Dimension Scan
- Gender: {CRITICAL / UNDERREPRESENTED / IMPLICIT / OK}
- Age: {severity}
- [All 9 dimensions with severity classification]

## 4. Loop Decision
**Verdict: PROCEED / PROCEED WITH NOTES / LOOP**
[Justification]
[If LOOP: specifies which round(s), what to add, and confirmation that looping is actionable]

## 5. Synthesis Readiness
[Verdict]
[Recommended synthesis structure: executive summary → cross-cultural patterns → contradictions → gaps → questions → missing dimensions → top directions]
[Recommendation for synthesis structure]

# SS{n} Batch Note
- Verdict
- Speculative question count
- Critical missing dimensions
- Recommendation for synthesis
- File path to the checkpoint review
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `knowledge-base/analysis/checkpoint-review.md` exists
2. ✅ Coherence check section traces all Round 5 questions back to source
3. ✅ Grounding audit uses 3-tier classification (evidence-derived / gap-derived / speculative)
4. ✅ Paper existence verification completed for all Round 5 questions
5. ✅ Missing dimension scan covers all 9 standard dimensions with severity classification
6. ✅ Loop decision is clearly stated (PROCEED / PROCEED WITH NOTES / LOOP) with justification
7. ✅ If LOOP, specifies which round(s) need revisiting AND confirms the loop is actionable
8. ✅ Recommendation for synthesis structure is provided
9. ✅ Batch note appended documenting verdict, critical gaps, and synthesis recommendations

---

## Common Checkpoint Outcomes

| Outcome | Meaning | Action |
|---|---|---|
| All questions grounded, no critical missing dimensions | PROCEED | Launch SS14 synthesis |
| Well-grounded but 1-2 dimensions underrepresented | PROCEED WITH NOTES | Note limitations in synthesis |
| 3+ speculative questions with no clear chain | LOOP back to Round 5 | Refine Round 5 to strengthen grounding |
| Critical dimension absent but no papers exist | PROCEED WITH NOTES (not LOOP) | Flag in boundaries; looping won't add data |
| Critical dimension absent AND papers exist in candidate list | LOOP back to Round 4 | Add dimension to gap analysis |
| Round 1-2 matrix has gaps affecting Round 3-4 | LOOP back to Round 1 or 2 | Refine thematic or comparison matrix |

---

## What NOT to Do

- Do NOT proceed to synthesis without explicit PROCEED or PROCEED WITH NOTES verdict
- Do NOT silently ignore missing dimensions — document them with severity
- Do NOT use LOOP as a default or for unactionable gaps
- Do NOT skip the coherence check — disconnected questions will weaken the synthesis
- Do NOT use binary speculation classification — use 3 tiers
