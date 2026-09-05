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

### 5. Earnings Reconciliation (mandatory)
After extracting reported figures, force a reconciliation pass before writing the read:

- **Reported vs segment vs adjusted:** reconcile reported operating profit against the **sum of segment operating profits**, and reported net profit against **adjusted/non-HKFRS profit**.
- If they disagree, **hunt the non-operating / one-off items**: warrant revaluation, convertible-bond interest, impairments, FX, other gains/losses. Label the reconciler and state which line (reported or adjusted) **drives the final fundamental read**.
- Record the reconciliation table + outcome in the output (source IDs for each line). Do not carry a contradiction silently into valuation.

### 6. Currency Consistency (per source)
State the **reporting currency of every source** (most HK companies report in HKD — but some report in USD like Lenovo, or CNY). For each metric used downstream, note the currency basis. If mixed currencies enter one comparison (e.g. peer multiples or thresholds), state the exchange-rate assumption.

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
6. ✅ Earnings reconciliation performed (reported vs segment vs adjusted), one-off items labeled, driving line stated
7. ✅ Reporting currency stated per source; mixed-currency comparisons carry an FX assumption
8. ✅ Key documents appraised into `documents/appraisals/` with verbatim quotes + evidence/access tags; cross-appraisal consistency check run; findings indexed in `documents/findings-index.json`
