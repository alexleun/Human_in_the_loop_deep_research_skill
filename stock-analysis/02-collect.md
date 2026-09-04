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
2. **Fetch & preserve (mandatory):** For every source you extract from, save a **local copy**:
   - Web page → `sources/YYYY-MM-DD-<description>.html` (or `.md`)
   - PDF report → `sources/YYYY-MM-DD-<description>.pdf`
   - Record the URL and the saved local filename in the `sources_index.md`.
3. **Extract with grounding:** Copy **exact quoted text** for any number/claim you will use, tagging each with its source ID and access level.
4. **Cover the minimum dataset** (see below). For stale/undated data, record the "as of" date — never present historical figures as current.
5. If a fetch is paywalled/blocked, use the fallback free source and note it. Do not invent numbers.

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

1. ✅ Local copy of every source saved in `sources/` and listed in `sources_index.md`
2. ✅ Minimum dataset captured with exact quoted text + source IDs + as-of dates
3. ✅ Each fact traceable to a real, verified public URL (no hallucinated sources)
4. ✅ A completeness/gap note exists: what is found, what is missing, and why
5. ✅ All sources are free/public (no API-key-dependent source was used)
