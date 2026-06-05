# Phase 2: Search Design & Paper Collection

**Purpose:** Design systematic search strategy, execute parallel region searches, acquire papers.

**Execution pattern:** For projects spanning 4+ regions (global scope), run region searches as parallel sub-agents. For local scope, run depth-first search within the target region. For >20 candidate papers, plan for sub-session-based deep reading in Phase 3.

---

## 2a. Search Strategy Design

Before any search, produce a written protocol at `papers/search-protocol.md`:

- **Discipline search templates** — tailored query terms per discipline
- **Inclusion/exclusion criteria** — author type, study type, population, date range, language
- **Professor-led definition (NEW in v3.0):** A paper is professor-led if ANY co-author holds a full-professor (or equivalent senior-researcher) position at the time of publication, OR if the senior/corresponding author holds a professorial position. PhD-candidate-led papers with a professor as senior author count as professor-led. Document the professor's name and institution.
- **Region-specific source hierarchy** — primary and secondary databases per region
- **Per-region working languages** — for non-English sources
- **Search log conventions** — what to record per query
- **Per-paper metadata schema** — JSON fields required
- **Quality tier classification** — Tier A (peer-reviewed, full text), Tier B (peer-reviewed but access restricted OR non-peer-reviewed report with full text), Tier C (working paper, preprint, secondary)
- **Stopping criteria** — per-region paper count target
- **Generational/cohort dimension (NEW in v3.1):** If generational comparison is in scope, add `"generational OR cohort OR longitudinal time-use"` to region query templates. Note expected cohort labels per region in `search-protocol.md`.

---

## 2b. Region-Parallel Search (Global Scope)

Run searches organized by geographic region, **each as a parallel sub-agent**:

| Region | Typical Search Focus |
|--------|---------------------|
| East Asia | China, Japan, South Korea, Taiwan — collectivism, work culture, filial piety |
| South & Southeast Asia | India, Indonesia, Thailand, Vietnam — family structure, rural/urban divide |
| Europe | UK, Germany, France, Nordic, Eastern — welfare state, individualism, work-life |
| Americas | US, Canada, Brazil, Mexico — immigration, diversity, inequality |
| Middle East & Africa | Egypt, Nigeria, South Africa, Turkey, Iran — religion, community, tradition |
| Oceania & Pacific | Australia, New Zealand, Pacific Islands — indigenous practices, island life |

**Per-region sub-agent task:** search, identify candidates, return list with title, author, affiliation, year, URL, DOI, abstract, search query, methodology, and tier estimate.

**For local scope:** Run the same pattern but with one region. Adjust sub-regions and queries to focus depth.

---

## 2c. Collation & Deduplication

- Merge all region results into a unified candidate list at `papers/unified-candidate-list.md`
- Deduplicate (same paper found by multiple region agents)
- Note region balance and discipline balance
- Flag the borderline cases for project-manager review
- **Search-log cross-check (NEW in v3.0):** Before finalizing, verify that search-log DOIs resolve correctly, abstract figures match the source, and author affiliations/professor status are independently confirmed

---

## 2d. Paper Acquisition (Optional, often deferred to Phase 3)

- Downloading full PDFs to `papers/raw/` is optional; for paywalled papers, accept abstract-only status
- File naming: `{FirstAuthor}_{Year}_{ShortTitle}.pdf`
- Classification: discipline, methodology, population, sample size
- **Non-ASCII filename check (NEW in v3.0):** If author surnames contain diacritics (é, ü, ñ, ç, ï), create ASCII-only filenames and record the mapping in `_filename_map.json`

---

## 2e. Coverage Report

Produce at `papers/coverage-report.md`:

- Papers per region, discipline, decade, methodology, population type
- **Explicit coverage gaps flagged** — regions, disciplines, or behavior domains with zero hits
- **Regional coverage fail-safe (NEW in v3.0):** If exhaustive search yields fewer than the target N papers for a region, this is a valid finding — do NOT pad the candidate list. Document in a "regional-coverage-note": total papers found, total included, known gaps (specific countries, populations, behaviors absent). Flag empty cells as "data absent for this region" — some gaps are structural (no academic infrastructure) and cannot be filled without ex-novo primary research.
- Language bias note — what languages were searched vs what exists
- Recommendations for follow-up searches (if any)

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `papers/search-protocol.md` exists with all sections (discipline templates, criteria, sources, languages, schema, tier classification, stopping criteria, professor-led definition)
2. ✅ All region sub-agent searches have returned search logs to `papers/raw/search-log-{region}.md`
3. ✅ Search-log cross-check completed: DOIs verified, abstract figures cross-checked, affiliations confirmed
4. ✅ `papers/unified-candidate-list.md` exists with deduplicated final roster
5. ✅ Each paper has at minimum: title, authors, year, URL/DOI, abstract, search query, region, methodology, tier estimate
6. ✅ `papers/coverage-report.md` exists with explicit gap flagging including regional coverage fail-safe note
7. ✅ Non-ASCII filenames mapped in `_filename_map.json` if applicable
8. ✅ A batch note documents: total candidate count by region, tier distribution, key gaps

---

## What NOT to Do

- Do NOT execute deep reading in this phase — that is Phase 3
- Do NOT create entity files or build the knowledge graph
- Do NOT skip the protocol document — every region sub-agent needs it

---

## Common Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| Region sub-agent over-includes borderline papers | Criteria too loose | Tighten inclusion criteria in protocol |
| Same paper found by 3+ region agents | Search queries too broad | Add unique regional qualifiers |
| Sub-Saharan Africa under-represented | English-only search | Add non-English query templates |
| No Tier A papers from a region | Region has weaker English-indexed output | Accept Tier B with annotation |
| Search logs missing key fields | Sub-agent didn't follow schema | Re-run with explicit schema reminder |
| DOI from search log returns 404 (NEW) | Search log has stale DOI | Cross-check via Google Scholar before including |
