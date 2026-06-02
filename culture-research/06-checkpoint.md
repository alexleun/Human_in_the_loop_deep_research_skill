# Phase 6: Iteration Checkpoint

**Purpose:** Review all 5 analysis rounds as a coherent arc and decide if synthesis can proceed or if loops are needed.

**Execution pattern:** Run as a sub-session (SS14). Output is a verdict, not a new round.

---

## Procedure

### 1. Coherence Check
Do the research questions (Round 5) logically follow from the gaps (Round 4), contradictions (Round 3), and patterns (Rounds 1-2)? For each Round 5 question, trace the evidence chain.

### 2. Grounding Audit
For each research question in Round 5:
- Is there a clear evidence chain from collected papers → entity → Round 1-2 finding → Round 3-4 gap/contradiction → Round 5 question?
- Flag questions with insufficient grounding as **speculative** (not evidence-derived)
- Separate **evidence-derived** (grounded in verified findings) from **speculative** (grounded only in inferred findings from `abstract-only` papers)

### 3. Missing Dimension Scan
Check systematically for dimensions that may have been overlooked across all rounds:
- Gender
- Age / generation
- Socioeconomic class
- Technology penetration / digital divide
- Climate / geography
- Urban vs rural
- Seasonality
- Life stage transitions
- Disability / accessibility

If any of these are systematically absent, flag for Round 4 supplementation or accept and document.

### 4. Loop Decision
If weak links, missing dimensions, or insufficient grounding found:
- Identify which round(s) need revisiting (Round 1-5)
- Specify what needs to be added
- Document the decision

If checkpoint passes, document "proceed to synthesis" decision.

### 5. Synthesis Readiness Assessment
Final verdict:
- **PROCEED:** all rounds coherent, questions grounded, no critical gaps
- **PROCEED WITH NOTES:** minor gaps that can be addressed in synthesis itself
- **LOOP:** one or more rounds need revisiting before synthesis

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `knowledge-base/analysis/checkpoint-review.md` exists
2. ✅ Coherence check section traces all Round 5 questions back to source
3. ✅ Grounding audit identifies any speculative questions (count documented)
4. ✅ Missing dimension scan covers all 9 standard dimensions
5. ✅ Loop decision is clearly stated (PROCEED / PROCEED WITH NOTES / LOOP)
6. ✅ If LOOP, specifies which round(s) need revisiting
7. ✅ Recommendation for synthesis structure is provided
8. ✅ Batch note appended documenting verdict, critical gaps, and synthesis recommendations

---

## Output Format

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
[Speculative questions: count and list]
[Well-grounded questions: count and list]

## 3. Missing Dimension Scan
- Gender: ...
- Age: ...
- [9 dimensions total]

## 4. Loop Decision
**Verdict: PROCEED / PROCEED WITH NOTES / LOOP**
[Justification]

## 5. Synthesis Readiness
[Verdict and synthesis structure recommendation]

# SS{n} Batch Note
- Verdict
- Critical missing dimensions
- Recommendation for synthesis
```

---

## Common Checkpoint Outcomes

| Outcome | Meaning | Action |
|---|---|---|
| All questions well-grounded, no missing dimensions | PROCEED | Launch SS15 synthesis |
| Well-grounded but 1-2 dimensions underrepresented | PROCEED WITH NOTES | Note limitations in synthesis; document as future work |
| 3+ speculative questions with no clear chain | LOOP back to Round 5 | Refine Round 5 to strengthen grounding |
| Critical dimension (e.g., disability) absent from all rounds | LOOP back to Round 4 | Add disability dimension to gap analysis, regenerate |
| Round 1-2 matrix has gaps that affect Round 3-4 | LOOP back to Round 1 or 2 | Refine thematic categorization or comparison matrix |

---

## What NOT to Do

- Do NOT proceed to synthesis without explicit PROCEED or PROCEED WITH NOTES verdict
- Do NOT silently ignore missing dimensions — document them
- Do NOT use LOOP as a default — be honest about whether loops add value
- Do NOT skip the coherence check — disconnected questions will weaken the synthesis
