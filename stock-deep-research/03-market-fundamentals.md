# Phase 3: Market Fundamentals — Structure, Earnings, Valuation Position

**Who drives:** LLM (computation on collected data) + Human

**Purpose:** Establish the market's structural position: what the index IS (composition), what it EARNED (aggregate earnings and revisions), where it TRADES (valuation percentile vs history), and what the document corpus says about the economy/policy behind it. This is the "quality & growth" analog for a whole market.

**Code-first discipline:** For any computation (aggregate earnings, percentiles, composition weights), **write and run Python** from the collected figures — do not compute from memory. Use `sys.stdout.reconfigure(encoding='utf-8')` on Windows for safety.

## Dimensions

### 1. Composition & Concentration (structure)
- Sector weights in the index; top-10 constituent concentration (compute the % of index market cap held by the largest 10).
- Style tilt — growth vs value, cyclicals vs defensives — from sector weights.
- Note any structural concentration risk (single-sector dominance, e.g. financials/tech) that the fragility audit (Phase 7) will weigh.

### 2. Aggregate Earnings & Revisions
- Aggregate index earnings and forward EPS: level, growth trend, and recent **earnings-revision direction** (upgrades minus downgrades) from free sources.
- Earnings-season drivers: which sectors/periods dominate moves; reconciliation posture (reported vs adjusted where market-level data distinguishes them).

### 3. Valuation Position (percentile, not level)
- Index P/E and P/B vs **its own multi-year history** — compute the current percentile rank (e.g. daily P/E series vs 10-yr range) with `04_market_valuation.py`.
- Earnings-yield minus bond-yield spread (equity risk premium proxy) and its percentile.
- Dividend-yield support band (the yield level historically associated with market bottoms).
- Cross-check against 1–2 aggregator percentiles as a sanity read, but compute the percentile from your own series (Sanity note, Phase 2).

### 4. Deep-Read Appraisal of Key Documents (document-intelligence)
Appraise the top policy/regulator/market documents from the Phase 2 corpus into `documents/appraisals/{doc-id}.md`:

- YAML frontmatter: `doc_id`, `evidence_status`, `#access/{type}`, `#evidence/{level}`
- Key findings (**verbatim quotes only**), issuer caveats, quality assessment, the 3–5 quotes most important to the overview
- Cross-appraisal consistency check across key documents on uniform criteria before the phase is complete
- Record findings in `documents/findings-index.json` (id, source_doc, quote, evidence/access/status tags) for machine-readable reuse in Phases 6–9

## Output

A **market-fundamentals summary** with computed metric table (source IDs + as-of dates for every number), an earnings-revision read, and a short prose assessment: is this market expensive-healthy, cheap-stressed, or mid-quality? What are the top 2–3 fundamental risks?

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Composition (sector weights, top-10 concentration) and style tilt computed by script
2. ✅ Aggregate earnings + revision direction assessed with sources
3. ✅ Valuation percentiles (P/E, P/B, ERP, yield band) computed by script from own series, cross-checked
4. ✅ Key documents appraised into `documents/appraisals/` with verbatim quotes + evidence/access tags; cross-appraisal check done; findings indexed
5. ✅ Every number has a source ID and as-of date ≤ decision date (P9)
6. ✅ A one-paragraph market-fundamentals verdict (bull/neutral/bear) is written
7. ✅ Top fundamental risks listed