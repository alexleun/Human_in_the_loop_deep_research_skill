# Phase 2: Collect & Preserve — Public Evidence

**Who drives:** LLM (gathers, extracts, validates) + Human (provides access, flags bias)

**Purpose:** Gather and **preserve local copies** of every public source, and build a validated evidence log — the foundation for all later phases (citation-first, P1).

## Procedure

1. **Identify the evidence plane** (all free/public):
   - **HKEXnews** (`www1.hkexnews.hk`) — annual/interim reports, announcements (authoritative)
   - Company IR pages, annual report / prospectus PDFs
   - Free aggregators: Yahoo Finance HK, AAStocks, Investing.com, Google Finance
   - Financial statements / segment disclosures
   - Search engine results (DuckDuckGo / Bing) for news, ratings, government data
   - Official statistics / policy sites where relevant (e.g. Stock Connect flows)
2. **Preserve a local copy of every source BEFORE extracting findings** (P11, "fetch first, extract after"):
   - Web page → `sources/YYYY-MM-DD-<desc>.html`
   - PDF → `sources/YYYY-MM-DD-<desc>.pdf`
   - API response / dataset → `sources/YYYY-MM-DD-<desc>.json`
   - Use the `write` tool to save the fetched content immediately; do not skip this even for large content.
   Record `local_copy` next to each URL in `sources_index.md` (a Local Copy column). A source row that says "n/a (fetched)" / "n/a (web search)" without a real local file is a **gap, not done**.
3. **Validate each source**:
   - Does the URL resolve? Is it primary or secondary?
   - Record the **publication / as-of date** (critical for P9 anti-lookahead).
   - Prefer primary sources for critical facts (filings over blogs).
4. **Extract figures as derived facts** — record numbers with exact citation, as-of date, and the formula that turns raw inputs into metrics. A number without a source is **not** admitted to the evidence pool.
5. **Log all sources** in `sources/sources_index.md` (URL + local copy + access date + data-source ID). Every downstream finding references these IDs (P1 / P5 citation-first).

## Anti-Lookahead Note (P9)

Label every source with an as-of date. When collecting, separate:
- **Pre-cutoff evidence** (findable before the decision date) — the only admissible basis for the recommendation.
- **Post-cutoff reasoning** (outcome anticipation / later developments) — recorded separately, NOT used to justify the decision.

## End-Condition Compliance Check

Phase 2 is complete only when **evidence** for each end condition below is stated — do not assert completion. Map each end condition to actual evidence in `sources_index.md` (a "Compliance" section listing file paths / index rows), and truthfully flag any unmet item as a gap. Ticking a box without evidence is not completion.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ A **real local file + index row** exists for every source used (P11), saved with the `write` tool and indexed in `sources_index.md` (Local Copy column). No "n/a (fetched)" rows
2. ✅ Every figure carries a citation + data-source ID + as-of date
3. ✅ Sources are validated (resolvable, primary-preferred) and gaps documented
4. ✅ Pre-cutoff vs post-cutoff evidence is separated and labeled
5. ✅ Where a preferred source is paywalled/closed, a free substitute is documented
6. ✅ Human has signed off on the evidence base (or delegated it)
7. ✅ Compliance check above performed: each end condition mapped to actual evidence, unmet items truthfully flagged as gaps
