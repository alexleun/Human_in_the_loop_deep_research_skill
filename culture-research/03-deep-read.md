# Phase 3: Deep Reading & Critical Appraisal

**Purpose:** Read each paper thoroughly, extract grounded findings, assess quality — before any knowledge base entry.

**Execution pattern:** For >5 papers, run as **sub-sessions** (see `08-sub-session-orchestration.md`). For ≤5 papers, can run in one session with one sub-agent per paper.

---

## Preliminary: Check for Truncation & Encoding (NEW in v3.0)

Before reading any paper:
1. Verify the file is fully readable (check for truncation markers after each fetch)
2. If the filename contains non-ASCII characters (ï, é, ü, ñ, ç), use the `_filename_map.json` mapping or the cmd /c copy workaround
3. For open-access papers >50KB, read in 2-3 offset segments to guarantee the Limitations section is captured

---

## Paywall Access Protocol (NEW in v3.0)

For each paper, attempt to fetch full text in this priority order:

1. **Priority 1:** DOI landing page — check for open-access or abstract text
2. **Priority 2:** PubMed abstract (if paper is indexed — requires PMID)
3. **Priority 3:** Google Scholar search with exact title and author — GS abstracts are often more detailed than publisher abstracts and include cited-by counts. This is the most reliable second-level source for paywalled papers.
4. **Priority 4:** Search-log abstract from `papers/raw/search-log-{region}.md`
5. **Priority 5:** Mark as `no-abstract-available`

After each attempt, check for truncation. If the page returned is truncated, read offset segments.

---

## Search-Log Cross-Check (NEW in v3.0)

Before writing the appraisal, cross-check against the search log:

1. Verify that the DOI from the search log resolves to the correct paper (if not, note the discrepancy)
2. Cross-check key numerical claims between the search-log abstract and the publisher/GS abstract — if they differ, note the discrepancy in the Metadata section
3. Verify author affiliations and professor status independently (do not rely on search-log classification)

---

## Per-Paper Extraction

For each paper, extract and capture in `papers/appraisals/{paper-id}.appraisal.md`:

```yaml
---
paper_id: {Author}_{Year}_{ShortTitle}
appraised_by: sub-session-SS{n}
appraisal_date: YYYY-MM-DD
evidence_status: full-text | open-repository | abstract-only | no-abstract-available
---
```

Sections:
- **Metadata** — region, country focus, discipline, methodology type, sample, professor affiliation
- **Research Question** — verbatim or close paraphrase
- **Theoretical Framework** — what theory/lens guides this study
- **Key Findings (verbatim quotes)** — each with exact quote and section reference
- **Author's Own Limitations** — what the paper itself acknowledges
- **Critical Appraisal:**
  - Methodology Quality (sample, bias controls, study duration — each HIGH/MEDIUM/LOW)
  - Cultural Positioning (emic/etic/mixed, positionality noted, cultural bias risk)
  - Evidence Strength per Claim (direct-evidence / inferred / claimed)
- **Verbatim Quotes for Knowledge Base** — the 3-5 most important quotes
- **# SS{n} Batch Note** — open issues, papers to re-evaluate, evidence_status distribution
- **## Director Observations** — quality variance, scope discipline, prompt clarity, coordination overhead, generalizable lessons

---

## Unfindable Paper Protocol (NEW in v3.2)

Papers may be unfindable — DOI returns 404, title yields no results, publisher site is down. Handle systematically:

1. **Attempt order:** DOI landing page → PubMed (if PMID known) → Google Scholar exact-title search → search-log abstract → mark unfindable
2. **Timebox:** 5 minutes total per paper. If not accessible after 5 minutes, move on.
3. **Document:** Create a minimal `papers/appraisals/{paper-id}.appraisal.md` with:
   - YAML frontmatter: `paper_id`, `evidence_status: no-abstract-available`
   - Metadata section: title, authors, year, attempted URLs, reason unfindable (404 / no GS result / paywall with no alternative)
   - No findings (contributes 0 to knowledge base)
4. **Do NOT replace:** Do not substitute a different paper. Document the gap. The cross-appraisal consistency check will note the empty slot.
5. **Coverage impact:** This paper contributes 0 findings. Affected cells in the cross-region matrix are marked as "data absent."

This prevents time sinks while maintaining honest coverage reporting.

## Mid-Phase Calibration (NEW in v3.2)

Do not write all appraisals before checking quality. After the first 3–5 appraisals (or the smallest region batch), pause and review:

1. Read 2 appraisals from that batch
2. Check: verbatim quotes present? evidence_status honest? methodology quality calibrated correctly?
3. If quality is acceptable, proceed with remaining appraisals
4. If quality is off, write calibration guidance to the next sub-session prompt (e.g., "Be more conservative with evidence/high tags"; "Extract 5+ verbatim quotes per paper")

This catches the common failure of uniform quality drift across an entire region batch.

## Source Preservation Requirement (NEW in v3.1)

After fetching any paper content, save a local copy BEFORE extracting findings:
- Full-text PDF or HTML → `papers/raw/{paper-id}.pdf` or `.html`
- Abstract page → `papers/raw/{paper-id}-abstract.html`
- Google Scholar abstract → `papers/raw/{paper-id}-gs-abstract.html`
- Search log snippet → already exists in `papers/raw/search-log-{region}.md`

Add the saved filename to the appraisal's Metadata section as `local_copy: papers/raw/{filename}`. This ensures findings remain verifiable if publisher URLs change or go offline.

---

## Evidence Status Rules

| Status | Meaning |
|---|---|
| `full-text` | Paper fully read; verbatim quotes verified |
| `open-repository` | Author's accepted manuscript retrieved; treat as full-text |
| `abstract-only` | Only abstract accessible; all findings marked `[inferred from abstract]` |
| `no-abstract-available` | No text accessible at all; minimal appraisal only |

**Verbatim quote rule:** Every finding must include a verbatim quote from the source OR be marked as `[inferred from abstract]`. Never paraphrase a finding without a quote. This is the anti-hallucination rule for the entire project.

**For abstract-only papers:** The abstract IS the source. Quote the relevant sentence(s) verbatim. If a single sentence contains 2+ findings, you may quote it once and cross-reference it across findings, or quote it separately per finding. Either approach is acceptable as long as each finding has at least one attached verbatim source string.

**Expected information density:**
- `full-text` paper: 6-15 claims with supporting detail
- `abstract-only` paper: 2-4 directional claims (no effect sizes, no subgroup details)
- `no-abstract-available`: 0-1 metadata-only claims

---

## Cross-Appraisal Consistency Check (REFINED in v3.0)

After ALL parallel appraisals complete, produce a **required artifact** at `papers/appraisals/_cross-appraisal-check.md`:

1. **Same criteria applied uniformly?** — compare appraisals side by side across regions
2. **Any paper so methodologically weak it should be excluded?** — document decision
3. **Flag any appraiser bias** (e.g., favoring certain methodologies, regional bias)
4. **Verbatim quote count consistent?** — each paper should have at least 3 quotes
5. **Evidence strength calibrated consistently?** — same study type should get similar ratings across appraisers

This file must exist before the deep-read phase is marked complete. If inconsistencies are found, the project manager re-runs affected sub-sessions with explicit calibration guidance.

---

## Regional Coverage Fail-Safe (NEW in v3.0)

If a region has objectively few papers:
- Do NOT pad the candidate list with methodologically weak or tangential papers
- Document in a "regional-coverage-note" in the batch note: total papers found, total included, known gaps
- Flag empty cells in the cross-region matrix as "data absent for this region" — some gaps are structural and cannot be filled without ex-novo primary research

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ All papers in the candidate list have a `.appraisal.md` file in `papers/appraisals/`
2. ✅ Each file has YAML frontmatter with paper_id, appraised_by, evidence_status
3. ✅ Each file has the full section structure (Metadata, RQ, Theory, Findings, Limitations, Critical Appraisal, Verbatim Quotes for KB)
4. ✅ Each file has at least 3 verbatim quotes (or explicit `[inferred from abstract]` markers)
5. ✅ Evidence_status is honest — no `full-text` claims for paywalled papers
6. ✅ **Source preservation:** Every fetched source has a local copy saved to `papers/raw/` with the filename recorded in the appraisal Metadata (NEW in v3.1)
7. ✅ `papers/appraisals/_cross-appraisal-check.md` exists with 5-point checklist completed
8. ✅ A batch note is appended documenting evidence_status distribution and open issues
9. ✅ Director Observations section included in each batch note

---

## Output

One `.appraisal.md` per paper in `papers/appraisals/`. These serve as the grounding source for all knowledge base entities and synthesis claims.

---

## What NOT to Do

- Do NOT fabricate quotes — if paywalled, use `[inferred from abstract]` markers
- Do NOT mark paywalled papers as `full-text`
- Do NOT skip the cross-appraisal consistency check
- Do NOT create entities or run analysis — that is Phase 4+

---

## Common Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| Quotes are paraphrased, not verbatim | Sub-agent skipped quote extraction | Re-emphasize verbatim rule |
| All papers marked `full-text` when many were paywalled | Optimistic about access | Mandate evidence_status honesty |
| Findings thin on paywalled papers | Sub-agent stopped after abstract | Use GS enriched abstract; document `[inferred]` |
| Inconsistent criteria across regions | Multiple SS used different rubrics | Run consistency check; specify calibration guidance |
| Truncation hides limitations section | 50KB file cap | Read in 2-3 offset segments |
| DOI returns 403/cookie-wall | Paywall blocks publisher page | Use GS enriched abstract (Priority 3) |
