# Phase 3: Deep Reading & Critical Appraisal

**Purpose:** Read each paper thoroughly, extract grounded findings, assess quality — before any knowledge base entry.

**Execution pattern:** For >5 papers, run as **sub-sessions** (see `08-sub-session-orchestration.md`). For ≤5 papers, can run in one session with one sub-agent per paper.

---

## Per-Paper Extraction

For each paper, extract and capture in `papers/appraisals/{paper-id}.appraisal.md`:

```yaml
---
paper_id: {Author}_{Year}_{ShortTitle}
appraised_by: sub-session-SS{n}     # or "single-session"
appraisal_date: YYYY-MM-DD
evidence_status: full-text | open-repository | abstract-only
---

# Appraisal: {Author}_{Year}_{ShortTitle}

## Metadata
- Region: {region}
- Country focus: {list from search log}
- Discipline: {sociology / anthropology / psychology / urban-studies / etc.}
- Methodology type: {ethnography / time-diary / survey / mixed / review}
- Sample: {size, population, year}
- Professor affiliation: {name + institution}

## Research Question
{verbatim or close paraphrase}

## Theoretical Framework
{what theory, what lens guides this study?}

## Key Findings (verbatim quotes)
- Finding 1: "{exact verbatim quote from paper}" (page or section if known)
- Finding 2: "{exact verbatim quote from paper}"
- Finding 3: "{exact verbatim quote from paper}"

## Author's Own Limitations
{what limitations does the paper itself acknowledge?}

## Critical Appraisal

### Methodology Quality
- Sample representativeness: HIGH / MEDIUM / LOW — {rationale}
- Bias controls: HIGH / MEDIUM / LOW — {rationale}
- Study duration adequacy: HIGH / MEDIUM / LOW — {rationale}

### Cultural Positioning
- Emic (insider) / Etic (outsider) / Mixed
- Researcher positionality noted? Yes / No
- Cultural bias risk: HIGH / MEDIUM / LOW

### Evidence Strength per Claim
- Finding 1: direct-evidence / inferred / claimed — {rationale}
- Finding 2: direct-evidence / inferred / claimed — {rationale}
- Finding 3: direct-evidence / inferred / claimed — {rationale}

### Verbatim Quotes for Knowledge Base
{the 3-5 most important verbatim quotes that downstream analysis will rely on}

# SS{n} Batch Note
{appended only when run as a sub-session}
- {open issues for project manager}
- {papers to re-evaluate}
- {evidence_status distribution}
```

---

## Evidence Status Discipline (CRITICAL)

**Every finding must include a verbatim quote from the source** OR be marked as `[inferred from abstract — full text not accessed]`. Never paraphrase a finding without a quote. This is the anti-hallucination rule for the entire project.

For `abstract-only` papers:
- The appraisal can still be completed, but every finding must carry the `[inferred from abstract]` marker
- Author's limitations section is marked "[Cannot be assessed from abstract; full text not accessed]"
- The project manager must note that paywalled papers contribute less to synthesis

For `open-repository` papers:
- Use the author's accepted manuscript (often differs from published version in formatting but content is the same)
- Cite the repository URL in the appraisal
- Treat as `full-text` for content purposes

---

## Cross-Appraisal Consistency Check

After all parallel appraisals complete:

1. **Same criteria applied uniformly?** — compare appraisals side by side
2. **Any paper where methodology quality is so low it should be excluded?** — exclude from synthesis
3. **Flag any appraiser bias** (e.g., favoring certain methodologies over others, regional bias)
4. **Verbatim quote count consistent?** — each paper should have at least 3 quotes
5. **Evidence strength calibrated consistently?** — same study type should get similar ratings across appraisers

If inconsistency is found, the project manager re-runs the affected sub-session with explicit calibration guidance.

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ All papers in the candidate list have a `.appraisal.md` file in `papers/appraisals/`
2. ✅ Each file has YAML frontmatter with paper_id, appraised_by, evidence_status
3. ✅ Each file has the full section structure (Metadata, RQ, Theory, Findings, Limitations, Critical Appraisal with 3 quality sub-sections, Verbatim Quotes for KB)
4. ✅ Each file has at least 3 verbatim quotes (or explicit `[inferred]` markers)
5. ✅ Each file's methodology quality, cultural positioning, and evidence strength are assessed
6. ✅ A batch note is appended documenting evidence_status distribution and open issues
7. ✅ Cross-appraisal consistency check is complete and any inconsistencies are documented

---

## Output

One `.appraisal.md` per paper in `papers/appraisals/`. These serve as the grounding source for all knowledge base entities and synthesis claims.

---

## Common Failure Modes (Learned from Practice)

| Failure | Cause | Fix |
|---|---|---|
| Quotes are paraphrased, not verbatim | Sub-agent skipped quote extraction | Re-emphasize verbatim rule; require re-do |
| All papers marked `full-text` when many were paywalled | Sub-agent optimistic about access | Mandate evidence_status honesty; abstract-only is acceptable |
| Findings thin on paywalled papers | Sub-agent stopped after abstract | Document `[inferred from abstract]` markers; note the loss in batch note |
| Inconsistent criteria application | Multiple sub-sessions used slightly different rubrics | Project manager runs consistency check; specifies calibration guidance |
| Books read as journal articles | Sub-agent confused book vs article format | Distinguish in metadata: `venue_type: book` vs `journal` vs `report` |
