# Phase 7: Synthesis Document

**Purpose:** Integrate all 5 analysis rounds and the checkpoint review into a final synthesis document.

**Execution pattern:** Run as the final sub-session (SS15). This is the terminal deliverable.

---

## Before Starting: Input Strategy (NEW in v3.0)

Reading all 6 analysis files (~2,000+ lines) consumes significant context budget. Use this strategy:

1. Read `findings-index.json` first — it provides machine-readable finding data
2. Read the checkpoint review (`checkpoint-review.md`) — it summarizes all rounds
3. Read the batch notes of each round (SS9-SS13) for concise summaries
4. Read the full output of only the rounds that need deeper understanding
5. Use a Task sub-agent to extract structured data (patterns, contradictions, gaps, questions) into a working scratchpad

Prefer reading `knowledge-base/synthesis-input.json` if it exists (a pre-compiled aggregation of key data from all rounds).

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
   - Resolvable vs genuine vs partially resolvable
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
   - Classify each as **evidence-derived**, **gap-derived**, or **speculative**

6. **Boundaries and Caveats** (from Checkpoint)
   - Critical missing dimensions
   - Underrepresented dimensions
   - Access distribution: X% of corpus is abstract-only
   - Language bias, methodology bias, etc.
   - How access distribution affects confidence in cross-region patterns and research questions

7. **Appendix** (links only, not full content)
   - List of all papers with `[[wikilink]]` to appraisals
   - Link to all analysis round outputs
   - Link to knowledge base summary

---

## Wikilink Verification (CRITICAL)

Every `[[wikilink]]` in the synthesis document MUST point to an actual file in the vault. Before saving:

1. Extract all `[[wikilink]]` references from the document using a script or tool
2. Verify each target file exists:
   - `[[PaperID]]` → must have `papers/appraisals/PaperID.appraisal.md`
   - `[[round1-thematic-map]]` → must have `knowledge-base/analysis/round1-thematic-map.md`
3. If any wikilink points to a non-existent file, either:
   - Fix the file (create it) if it's a minor miss
   - Remove the wikilink if it was speculative
4. Document any fixes in a `# SS{n} Wikilink Verification Note` at the end

**Use a script if possible:** `verify-wikilinks.ps1` that scans the markdown file, extracts `[[wikilink]]` refs, and reports which targets exist vs missing.

---

## Paywall-Weighted Honesty (REFINED in v3.0)

The synthesis should use the **dual evidence model** throughout:
- **Evidence-derived claims** — grounded in full-text or open-repository papers (access/full-text)
- **Inferred claims** — grounded only in abstract-only papers (access/abstract-only)

The synthesis document's "Boundaries and Caveats" section should note:
- What proportion of the corpus is `abstract-only`
- How this affects confidence in cross-region patterns
- Which research directions are grounded in evidence vs speculation vs gaps
- Use the 3-tier classification from the checkpoint: evidence-derived / gap-derived / speculative

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `knowledge-base/synthesis.md` exists
2. ✅ All 7 sections present (executive summary, patterns, contradictions, gaps, novel directions, boundaries, appendix)
3. ✅ At least 5 novel research directions documented with full assessment
4. ✅ All `[[wikilink]]` references point to actual files (verification done)
5. ✅ Wikilink verification note documents any fixes
6. ✅ Boundaries section includes access distribution stats (X% abstract-only)
7. ✅ Research directions classified as evidence-derived / gap-derived / speculative
8. ✅ Batch note documents: section completion, top 5 research questions, missing dimensions flagged, Director Observations
9. ✅ The document opens cleanly (no broken `[[wikilink]]` blocks, no formatting issues)

---

## Tag Annotations

Use Obsidian tags throughout:
- `#synthesis/executive-summary`
- `#synthesis/patterns`
- `#synthesis/contradictions`
- `#synthesis/gaps`
- `#synthesis/research-directions`
- `#synthesis/boundaries`

These are frontmatter tags (in the YAML `tags:` field) or inline `#synthesis/...` markers per Obsidian convention.

---

## What NOT to Do

- Do NOT introduce findings not present in the analysis rounds
- Do NOT break the section structure
- Do NOT leave broken `[[wikilink]]` references
- Do NOT fabricate quotes
- Do NOT skip the wikilink verification step
- Do NOT skip the access-distribution note in boundaries
- Do NOT use binary speculation classification — use 3 tiers

---

## After Synthesis: Archiving the Change

Once `synthesis.md` is verified and approved by the human:

1. Update `project-state.json` with final deliverable paths
2. The project directory is the persistent record; Obsidian vault can be opened from `knowledge-base/`
3. Produce a `skill-evolution-log.md` entry documenting lessons for the skill
