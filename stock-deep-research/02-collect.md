# Phase 2: Collect & Preserve — Numeric Base + Document Corpus

**Who drives:** LLM (gathers, extracts, validates, computes) + Human (provides access, flags bias)

**Purpose:** Build the two-layer evidence base for a whole-market view: **Part A** the numeric intake (index price series, valuation, breadth) that every computation runs on, and **Part B** the document corpus (market, official, press-release, and news sources) that narrative claims quote verbatim. Every source is preserved, verified, and access-tagged.

## Part A — Numeric Intake (computation-native)

1. **Index price history:** fetch a clean daily OHLC series for the index (Yahoo Finance free / Investing.com / HKEX EOD data), record the as-of date, and persist to `data/<market>-price-history-<asof>.csv`. If a direct fetch fails, reconstruct from 2+ independent aggregators and document the reconstruction in the methodology.
2. **Valuation & ratio base:** index P/E, P/B, dividend yield, earnings yield, index level, market cap — each as a dated artifact (CSV/JSON), never a transcribed aggregator reading (see Sanity note below).
3. **Breadth inputs:** % constituents above MA200, advance/decline counts, new highs/lows, cross-sectional dispersion. If member-level data is unavailable, use a documented approximation (e.g. a broad liquid subset ETF or index constituents from a free list) and state the approximation in `data/README.md`.
4. **Auxiliary series:** bond yields (for earnings-yield spread), sector index levels (for relative strength), policy/event calendar (for event-windowing).
5. **Raw before processed:** store raw downloads unaltered under `data/raw/`; processed series under `data/` with a provenance note (source, fetch date, transformations, as-of cutoff).

## Part B — Document Corpus (document-intelligence)

1. **Search protocol (written before searching):** write `documents/search-protocol.md` — document types in scope (market overviews, official/policy statements, regulator/statistical-agency releases, index-authority communications, broker/research summaries, press releases, news), inclusion/exclusion criteria, per-market source hierarchy (official/regulator > index/statistical agencies > market-research/broker summaries > press releases > news), languages, stopping criteria.
2. **Candidate list & dedup:** gather candidates into `documents/candidate-list.md` (title, issuer, date, URL, type, language); deduplicate on title+issuer+date.
3. **Coverage report with honest gaps:** write `documents/coverage-report.md` per document type. Mark any cell "data absent" where an authoritative type cannot be located — never pad with tangential sources.
4. **Preserve & verify every source:** save a local copy under `sources/` BEFORE extracting findings (P11); verify every URL and log `fetch_status` (ok / broken / paywalled); broken URLs are replaced via real search or flagged `[Data Gap]` — a broken URL never becomes evidence. Non-ASCII (CJK) filenames → ASCII-only names + `_filename_map.json`.
5. **Evidence & access tags (dual model) in `sources_index.md`:**
   - `evidence_status`: `full-text` / `partial` / `aggregator-only` / `unavailable`
   - `#access/{type}`: `full-text` / `aggregator` / `news-only` / `metadata-only`
6. **Access ladder (timeboxed, ~5 min/source):** primary PDF (HKEXnews / regulator) → `pdftotext` / HTML-text / Python extraction → aggregator substitute (logged with reason) → news gateway last. If none succeeds, mark `unavailable` and record the gap.
7. **Verbatim-quote rule:** every document claim carries the **exact quoted text**; a paraphrase without a quote (not marked `[inferred from {access type}]`) is rejected.
8. **Review manifest:** after the batch, append a manifest recording what was collected, the evidence chain per key claim, data gaps, and next action (deep-research pattern).

## Sanity Note (computation-native over transcription)

Index indicators published by aggregators (e.g. index RSI, index P/E, breadth ratios) are **references to verify against**, never numbers to copy. The analytics suite in Phases 3–5 recomputes every signal from collected series/raw values. Where reconstruction is impossible, the published reading is used **only** as a third-party reading with lower confidence, explicitly labeled.

## Anti-Lookahead Note (P9)

Label every source with an as-of date. Separate **pre-cutoff evidence** (the only admissible basis, dated ≤ decision date) from **post-cutoff reasoning** (recorded separately, never used to justify the view).

## End-Condition Compliance Check

Phase 2 is complete only when **evidence** for each end condition below is stated — do not assert completion. Map each end condition to actual evidence in `sources_index.md` and `data/README.md`, and truthfully flag any unmet item as a gap.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Part A: index price series persisted to `data/<market>-price-history-<asof>.csv`; valuation/breadth inputs present as dated artifacts; raw files unaltered
2. ✅ Part B: `documents/search-protocol.md` written before searching; candidate list deduplicated; coverage report flags gaps honestly (data-absent, not padded)
3. ✅ A **real local file + index row** exists for every source used (P11), with `fetch_status`, `evidence_status`, and `#access/` tags
4. ✅ Every figure and document claim carries a citation + as-of date; verbatim quotes captured (or `[inferred]` markers)
5. ✅ Pre-cutoff vs post-cutoff evidence separated and labeled
6. ✅ Store of primary filings' machine-readability checked; aggregator substitutions logged with the reason
7. ✅ Where a preferred source is paywalled/closed, a free substitute is documented or the cell is flagged data-absent
8. ✅ Review manifest appended (collected, evidence chain, data gaps, next action)
9. ✅ Human has signed off on the evidence base (or delegated it)