# Phase 7: Synthesis Document

**Purpose:** Integrate all 5 analysis rounds and the checkpoint review into a final synthesis document.

**Execution pattern:** Run as the final sub-session (SS15). This is the terminal deliverable.

---

## Document Structure (Follow EXACTLY)

1. **Executive Summary** (1-2 pages)
   - What was studied, scope (paper count, regions, disciplines, time span)
   - Key cross-cultural findings
   - Top 3-5 novel research directions

2. **Cross-Cultural Patterns** (from Round 2)
   - Universal behaviors
   - Culture-specific behaviors
   - Reference Round 2 matrix with `[[wikilink]]`

3. **Contradictions and Methodological Insights** (from Round 3)
   - Major contradictions
   - Resolvable vs genuine
   - Methodology patterns
   - Reference Round 3 with `[[wikilink]]`

4. **Research Gaps and Blind Spots** (from Round 4)
   - Region × domain gaps
   - Under-studied populations
   - Methodological, temporal, disciplinary gaps
   - Reference Round 4 with `[[wikilink]]`

5. **Novel Research Directions** (from Round 5)
   - Top 5-10 questions
   - Each with rationale, methodology, novelty, feasibility, impact
   - Reference Round 5 with `[[wikilink]]`

6. **Boundaries and Caveats** (from Checkpoint)
   - Critical missing dimensions
   - Underrepresented dimensions
   - Language bias, methodology bias, etc.

7. **Appendix** (links only, not full content)
   - List of all papers with `[[wikilink]]` to appraisals
   - Link to all analysis round outputs
   - Link to knowledge base summary

---

## Wikilink Verification (CRITICAL)

Every `[[wikilink]]` in the synthesis document MUST point to an actual file in the vault. Before saving:

1. List all `[[wikilink]]` references in the document
2. Verify each target file exists:
   - `[[PaperID]]` → must have `papers/appraisals/PaperID.appraisal.md`
   - `[[round1-thematic-map]]` → must have `knowledge-base/analysis/round1-thematic-map.md`
   - etc.
3. If any wikilink points to a non-existent file, either:
   - Fix the file (create it) if it's a minor miss
   - Remove the wikilink if it was speculative
4. Document any fixes in a `# SS15 Wikilink Verification Note` at the end

---

## Tag Annotations

Use Obsidian tags throughout:
- `#synthesis/executive-summary`
- `#synthesis/patterns`
- `#synthesis/contradictions`
- `#synthesis/gaps`
- `#synthesis/research-directions`
- `#synthesis/boundaries`

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `knowledge-base/synthesis.md` exists
2. ✅ All 7 sections present (executive summary, patterns, contradictions, gaps, novel directions, boundaries, appendix)
3. ✅ At least 5 novel research directions documented with full assessment
4. ✅ All `[[wikilink]]` references point to actual files (verification done)
5. ✅ Tag annotations follow Obsidian convention
6. ✅ `# SS15 Wikilink Verification Note` documents any fixes
7. ✅ `# SS15 Batch Note` documents: section completion, top 5 research questions, missing dimensions flagged
8. ✅ The document opens cleanly (no broken `[[wikilink]]` blocks, no formatting issues)

---

## Paywall-Weighted Honesty (NEW in v2.0)

The synthesis should distinguish:
- **Evidence-derived claims** — grounded in full-text or open-repository papers
- **Inferred claims** — grounded only in abstract-only papers (lower confidence)

The synthesis document's "Boundaries and Caveats" section should note what proportion of the corpus is `abstract-only` and how this affects confidence in cross-region patterns and research questions.

---

## What NOT to Do

- Do NOT introduce findings not present in the analysis rounds
- Do NOT break the section structure
- Do NOT leave broken `[[wikilink]]` references
- Do NOT fabricate quotes
- Do NOT skip the wikilink verification step

---

## After Synthesis: Archiving the Change

Once `synthesis.md` is verified and approved by the human:

1. Mark all `tasks.md` checkboxes complete
2. Run `openspec status --change {name}` to confirm 4/4 artifacts done
3. The openspec change can be archived via the `openspec-archive-change` skill
4. The project directory is the persistent record; Obsidian vault can be opened from `knowledge-base/`
