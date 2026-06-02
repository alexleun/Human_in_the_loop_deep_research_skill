# Phase 2: Search Design & Paper Collection

**Purpose:** Design systematic search strategy, execute parallel region searches, acquire papers.

**Execution pattern:** For projects spanning 4+ regions, run region searches as parallel sub-agents in the main session. For >20 candidate papers, plan for sub-session-based deep reading in Phase 3.

---

## 2a. Search Strategy Design

Before any search, produce a written protocol at `papers/search-protocol.md`:

- **Discipline search templates** — tailored query terms per discipline
- **Inclusion/exclusion criteria** — author type, study type, population, date range, language
- **Region-specific source hierarchy** — primary and secondary databases per region
- **Per-region working languages** — for non-English sources
- **Search log conventions** — what to record per query
- **Per-paper metadata schema** — JSON fields required
- **Quality tier classification** — Tier A (peer-reviewed, full text), Tier B (peer-reviewed but access restricted OR non-peer-reviewed report with full text), Tier C (working paper, preprint, secondary)
- **Stopping criteria** — per-region paper count target

---

## 2b. Region-Parallel Search

Run searches organized by geographic region, **each as a parallel sub-agent**:

| Region | Typical Search Focus |
|--------|---------------------|
| East Asia | China, Japan, South Korea, Taiwan — collectivism, work culture, filial piety |
| South & Southeast Asia | India, Indonesia, Thailand, Vietnam — family structure, rural/urban divide |
| Europe | UK, Germany, France, Nordic, Eastern — welfare state, individualism, work-life |
| Americas | US, Canada, Brazil, Mexico — immigration, diversity, inequality |
| Middle East & Africa | Egypt, Nigeria, South Africa, Turkey, Iran — religion, community, tradition |
| Oceania & Pacific | Australia, New Zealand, Pacific Islands — indigenous practices, island life |

**Per-region sub-agent task:** search, identify candidates, return list with title, author, affiliation, year, URL, abstract, search query, methodology, and tier estimate.

---

## 2c. Collation & Deduplication

- Merge all region results into a unified candidate list at `papers/unified-candidate-list.md`
- Deduplicate (same paper found by multiple region agents)
- Note region balance and discipline balance
- Flag the borderline cases for project-manager review

---

## 2d. Paper Acquisition (Optional, often deferred to Phase 3)

- Downloading full PDFs to `papers/raw/` is optional; for paywalled papers, accept abstract-only status
- Create metadata at `papers/meta/{id}.meta.json` if not already in search logs
- File naming: `{FirstAuthor}_{Year}_{ShortTitle}.pdf`
- Classification: discipline, methodology, population, sample size

---

## 2e. Coverage Report

Produce at `papers/coverage-report.md`:

- Papers per region, discipline, decade, methodology, population type
- **Explicit coverage gaps flagged** — regions, disciplines, or behavior domains with zero hits
- Language bias note — what languages were searched vs what exists
- Recommendations for follow-up searches (if any)

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `papers/search-protocol.md` exists with all sections (discipline templates, criteria, sources, languages, schema, tier classification, stopping criteria)
2. ✅ All region sub-agent searches have returned search logs to `papers/raw/search-log-{region}.md`
3. ✅ `papers/unified-candidate-list.md` exists with deduplicated final roster
4. ✅ Each paper in the roster has at minimum: title, authors, year, URL/DOI, abstract, search query, region, methodology, tier estimate
5. ✅ `papers/coverage-report.md` exists with explicit gap flagging
6. ✅ A batch note documents: total candidate count by region, tier distribution, key gaps

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
| Same paper found by 3+ region agents | Search queries too broad | Add unique regional qualifiers to query templates |
| Sub-Saharan Africa under-represented | English-only search | Add non-English query templates; partner with regional expert if possible |
| No Tier A papers from a region | Region has weaker English-indexed output | Accept Tier B with annotation; note gap for synthesis |
| Search logs missing key fields | Sub-agent didn't follow schema | Re-run with explicit schema reminder |
