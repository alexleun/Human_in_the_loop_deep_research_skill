# Phase 2: Collect — Gather Public Sources & Company Data

**Who drives:** LLM (executes searches/fetches) + Human

**Purpose:** Collect, verify, and preserve all public information about the company before any analysis. Source preservation is mandatory.

## Authoritative HK Public Sources (no API key)

Use these in priority order for company data:

| Data Need | Sources | Notes |
|---|---|---|
| Company profile / business | Company official website, Hong Kong Exchange listing page | Business description, segments, products |
| Announcements & disclosures | **HKEXnews** (`www1.hkexnews.hk`) — official filings | Use the `searchtitle` for company code; search by stock code; all filings (annual/interim results, circulars, notices, ESOP, buybacks) |
| Annual / interim reports | HKEXnews listed documents; company IR page (PDF) | Full financial statements, MD&A, segments, risks |
| Financial statements | From annual/interim reports (official) or aggregator sites | Revenue, net profit, EBITDA, cash flow, balance sheet |
| Key statistics & ratios | AAStocks (`aastocks.com`), Yahoo Finance HK (`hk.finance.yahoo.com`), Investing.com HK | P/E, P/B, market cap, dividend yield, EPS |
| Historical price / volumes | Yahoo Finance, Investing.com, TradingView free | For technical analysis |
| Analyst ratings / price targets | Public aggregators (MarketScreener, TipRanks, Investing.com) | Consensus BUY/HOLD/SELL + target prices |
| News & sentiment | Google News, Yahoo Finance HK news, official company press releases, reputable financial press (Reuters, HKEX announcements) | Recent developments, catalysts, risks |
| Peer comparison | Same-sector/peer HK or global listings on free aggregators | Relative valuation, growth |

## Collection Protocol

1. **Search-first:** Use web search (and browser if needed) to locate the canonical pages for the stock. Save a **search log** listing each query and its top results with URLs.
2. **Fetch & preserve (mandatory, "fetch first, extract after"):** For every source you extract from, save a **local copy** at the moment you fetch it, BEFORE extracting any findings:
   - Web page → `sources/YYYY-MM-DD-<description>.html` (or `.md`)
   - PDF report → `sources/YYYY-MM-DD-<description>.pdf`
   - Use the `write` tool to save the fetched content immediately; do not skip this even for large content.
   - Record the URL and the saved local filename in `sources_index.md` under a **Local Copy** column.
   - A source row that says "n/a (fetched)" / "n/a (web search)" without a real local file is a **gap, not done**.
3. **Extract with grounding:** Copy **exact quoted text** for any number/claim you will use, tagging each with its source ID and access level.
4. **Cover the minimum dataset** (see below). For stale/undated data, record the "as of" date — never present historical figures as current.
5. If a fetch is paywalled/blocked, use the fallback free source and note it. Do not invent numbers.
6. **Primary-filing extraction fallback (record-once):** HKEXnews annual/interim PDFs are generally **not machine-extractable** via plain text fetch. Record that limitation **once** in the repo/skill-level note (e.g. `SKILL.md` HK-specific notes or the run's `sources_index.md` header) — do NOT waste time re-attempting `pdftotext`/HTML/Python extraction on every submission. Go directly to the documented access ladder: HKEXnews PDF (known limitation) → aggregator substitute (logged) → news gateway last. If a filing IS machine-readable in a given run, say so; the substitution is always logged in `sources_index.md` with the reason (e.g. "not machine-readable → NewTimeSpace/S&P/stockanalysis"). A silent downgrade to aggregator-consensus is not acceptable; the fallback must be recorded.
7. **URL verification (mandatory):** For every recorded source URL, attempt a fetch and log `fetch_status` (ok / broken / paywalled) in `sources_index.md`. A broken URL is replaced with a real one via web search, or flagged `[Data Gap]` — a broken URL never becomes evidence.
8. **Non-ASCII filenames:** if a preserved source file has non-ASCII (CJK/diacritic) characters, save an ASCII-only filename and record the mapping in `_filename_map.json`.

## Document Intelligence Intake (Part B — market/official/press/news corpus)

Beyond financials, collect the **heterogeneous text corpus** the thesis depends on: market documents, official documents, press releases, and news.

1. **Search protocol (written before searching):** record at `documents/search-protocol.md` — document types in scope, inclusion/exclusion criteria, per-market source hierarchy (official/regulator > index/statistical agencies > market-research/broker summaries > press releases > news), languages, and stopping criteria.
2. **Candidate list & dedup:** gather candidates into `documents/candidate-list.md` (title, issuer, date, URL, type, language); deduplicate on title+issuer+date.
3. **Coverage report with honest gaps:** write `documents/coverage-report.md`. If an authoritative type cannot be found, mark that cell "data absent" — never pad with tangential sources.
4. **Evidence & access tags (dual model), recorded in `sources_index.md`:**
   - `evidence_status`: `full-text` / `partial` / `aggregator-only` / `unavailable`
   - `#access/{type}`: `full-text` / `aggregator` / `news-only` / `metadata-only`
5. **Verbatim-quote rule:** any document claim used downstream carries the **exact quoted text**; a paraphrase without a quote (and not marked `[inferred from {access type}]`) is rejected.
6. **Review manifest:** after the batch, append a manifest recording what was collected, the evidence chain per key claim, data gaps, and next action.

Phase 2 is complete only when **evidence** for each end condition below is stated — do not assert completion. Map each end condition to actual evidence in `sources_index.md` (a "Compliance" section listing file paths / index rows), and truthfully flag any unmet item as a gap. Ticking a box without evidence is not completion.

## Minimum Dataset to Collect

- **Profile:** name, code, exchange, sector, business description, main products/segments
- **Current market snapshot:** last price, market cap, 52-week high/low, average volume (as-of date)
- **Financial history (≥ 3 years if available):** revenue, gross/operating/net margin, net profit, EPS, ROE, operating cash flow, free cash flow, net cash/debt, dividend
- **Balance sheet:** total assets, total liabilities/equity, gearing, cash position
- **Recent developments:** last 2–4 quarters, guidance, major announcements, catalysts
- **Peer set:** 3–6 comparable companies with their key valuation ratios
- **Analyst view (public):** consensus rating, number of analysts, average/median price target, recent changes

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ **Real local file + index row** for every source used (`sources/…` saved with the `write` tool; `sources_index.md` has a Local Copy column). No "n/a (fetched)" rows
2. ✅ Minimum dataset captured with exact quoted text + source IDs + as-of dates
3. ✅ Each fact traceable to a real, verified public URL (no hallucinated sources)
4. ✅ A completeness/gap note exists: what is found, what is missing, and why
5. ✅ All sources are free/public (no API-key-dependent source was used)
6. ✅ Compatibility of primary filings checked; any aggregator substitution logged with the reason (source-preservation raised from advisory to operational)
7. ✅ Compliance check above performed: each end condition mapped to actual evidence, unmet items truthfully flagged as gaps
8. ✅ Part B: document corpus collected per written search protocol; `documents/coverage-report.md` flags gaps honestly; every source has `evidence_status` + `#access/` + `fetch_status`; verbatim quotes captured; review manifest written
