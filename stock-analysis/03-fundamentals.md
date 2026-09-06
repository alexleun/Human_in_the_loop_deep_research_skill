# Phase 3: Fundamentals — Quality, Growth, Profitability, Balance Sheet

**Who drives:** LLM (computation on collected data)

**Purpose:** Assess the company's **quality and growth** — the core of "what is this business worth, and how risky is it?"

**Code-first discipline:** For any computation (growth rates, margins, ratios), **write and run Python** from the collected figures — do not compute from memory. Use `sys.stdout.reconfigure(encoding='utf-8')` on Windows for safety.

## Dimensions

### 1. Business Quality & Moat
- Business model: how does it make money? Per segment.
- Competitive advantage / moat: brand, scale, network effects, switching costs, IP, cost advantage, regulatory barriers.
- Management & governance: reputation, track record, alignment (insider ownership, buybacks), related-party risk.
- Earnings **quality**: is profit backed by cash flow? Any aggressive accounting, one-off gains/losses, capex intensity?

### 2. Growth
- Revenue growth (YoY, trend over ≥3 years).
- Profit / EPS growth (YoY, trend).
- Growth **sustainability**: organic vs one-off; market expansion, new products, TAM.
- Segment growth breakdown if available.
- Compute CAGR for revenue and EPS.

### 3. Profitability
- Gross margin, operating margin, net margin (trend over ≥3 years).
- ROE, ROIC/ROCE (trend).
- Compare margins/returns to peers.

### 4. Balance Sheet & Financial Health
- Net cash / net debt; gearing (D/E).
- Liquidity: current ratio, quick ratio.
- Operating cash flow vs net income (quality check).
- Free cash flow + FCF yield.
- Dividend policy & payout ratio (coverability).
- Capex intensity and any signs of balance-sheet stress.

### 5. Earnings Reconciliation & Definition Labeling (mandatory)
After extracting reported figures, force a reconciliation + labeling pass before writing the read:

- **Reported vs segment vs adjusted:** reconcile reported operating profit against the **sum of segment operating profits**, and reported net profit against **adjusted/non-HKFRS profit**.
- **Non-IFRS ↔ IFRS bridge (first-class step):** when a company reports non-IFRS/adjusted figures, build the explicit bridge item by item (e.g. SBC, investee/associate contributions, intangible amortization, one-offs) and label which line **(reported, IFRS, or non-IFRS) drives the fundamental read**. A headline like "non-IFRS +9% but IFRS flat" must be legible, not a mystery.
- **FCF definitions labeled:** every free-cash-flow figure carries its definition — **official company figure vs aggregator-standard (DB-style) FCF** — stated explicitly. When the two differ (e.g. 182.6B official vs 215.6B aggregator), **report both with definitions**; never pick one silently.
- If lines disagree, **hunt the non-operating / one-off items**: warrant revaluation, convertible-bond interest, impairments, FX, other gains/losses. Label the reconciler.
- **Contested signals (feed Phase 7):** conflicting earnings/FCF definitions or values across sources are surfaced in the fragility audit's contested-signal scan and temper the Phase 8 confidence score — they are never resolved silently in favor of either side.
- Record the reconciliation/labeling table + outcome in the output (source IDs for each line). Do not carry a contradiction silently into valuation.

### 6. Currency & Scope Consistency (per source)
State the **reporting currency of every source** (most HK companies report in HKD — but some report in USD like Lenovo, or CNY). For each metric used downstream, note the currency basis. If mixed currencies enter one comparison (e.g. peer multiples or thresholds), state the exchange-rate assumption.
Also label the **revenue/turnover scope per source**: consolidated company revenue vs total turnover *including associates* can differ materially (e.g. ~HK$280B consolidated vs HK$507B incl. associates) — both are real, but the report must state which scope each figure uses to avoid a false "revenue jump". Flag the scope in `sources_index.md`, Phase 3, and the report.

### 7. Key-Document Deep-Read Appraisal (document-intelligence)
For the documents that drive the fundamental read (annual/interim reports, official guidance, key press releases), appraise each into `documents/appraisals/{doc-id}.md`:

- YAML frontmatter: `doc_id`, `evidence_status` (full-text / partial / aggregator-only / unavailable), `#access/{type}`, `#evidence/{level}` (high/medium/low)
- Sections: metadata, key findings (**verbatim quotes only**), author's own caveats, quality assessment, the 3–5 quotes most important to the thesis
- Run a **cross-appraisal consistency check** across key documents on uniform criteria before the phase is complete; re-appraise any document judged on different criteria
- Record each finding in `documents/findings-index.json` (id, source_doc, quote, evidence/access/status tags) for machine-readable reuse in Phases 6–9

## Output

Produce a **fundamentals summary table** with the source ID for each number, plus a short prose assessment: is this a quality, growing, financially sound business? What are the top 2–3 fundamental risks?

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Growth, profitability, and financial-health metrics computed by script (not memory)
2. ✅ Every number has a source ID and as-of date
3. ✅ Quality & moat assessed against a defined competition set
4. ✅ A one-paragraph fundamental verdict (bull/bear/neutral) is written
5. ✅ Top fundamental risks are listed
6. ✅ Earnings reconciliation + definition labeling performed (reported vs segment vs adjusted; IFRS vs non-IFRS bridge), one-off items labeled, driving line stated; every profit/FCF number carries its definition (official vs aggregator-standard FCF); conflicting definitions surfaced as contested signals
7. ✅ Reporting currency + revenue/turnover scope stated per source; mixed-currency or mixed-scope comparisons carry the stated basis
8. ✅ Key documents appraised into `documents/appraisals/` with verbatim quotes + evidence/access tags; cross-appraisal consistency check run; findings indexed in `documents/findings-index.json`
