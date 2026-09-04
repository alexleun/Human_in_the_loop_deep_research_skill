# Phase 3: Fundamentals — Quality, Growth, Profitability, Financial Health

**Who drives:** LLM writes the analysis code; Human interprets and redirects.

**Purpose:** Establish what the company **economically is** — its business quality, growth trajectory, profitability, and financial health — before valuing it.

## Procedure

1. **Business model & narrative → economics (P1):**
   - Decompose into real business segments; map revenue pools, profit-pool quality, segment economics, business mix, capital allocation logic.
   - Distinguish **mature profit pools** from **scaling/optionality** segments (this drives valuation routing in Phase 4).
2. **Compute fundamentals by script (P3)** — write and run Python on collected figures:
   - **Growth:** revenue / EPS / operating profit CAGR over 3–5 yr; recent YoY.
   - **Profitability:** gross margin, operating margin, net margin, ROE, ROIC; trend over time.
   - **Financial health:** net debt / EBITDA, current ratio, interest coverage, operating cash flow vs net income quality; free cash flow trend.
   - **Quality metrics:** earnings stability, cash conversion, moat proxies (margin persistence, ROIC vs WACC).
3. **Benchmark vs peers** where data allows (margins, ROE, growth relative to sector), using industry-relative figures. Note sector context and any comparability caveats (reporting currency / fiscal year).
4. **Flag governance & setup risks:** related-party transactions, controlling shareholder structure, auditor opinion, litigation, dilution history.
5. **Code, don't memorize:** any ratio or growth rate must come from an executed script over cited inputs; save the script in `notebooks/`.

## Output

A written fundamental summary: business decomposition, key computed metrics table (with formula + data-source IDs), quality assessment, and open questions. Feed this to Phase 4 (valuation) and Phase 6 (debate).

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Business is decomposed into segments with economic rationale (P1)
2. ✅ All quantitative metrics are produced by executed Python scripts (P3), not LLM memory
3. ✅ Every figure carries a citation + data-source ID + as-of date
4. ✅ Quality / growth / profitability / financial health are each addressed
5. ✅ Peer comparison and comparability caveats are documented
6. ✅ Open questions and data gaps are recorded for later phases
