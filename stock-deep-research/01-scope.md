# Phase 1: Scope — Define the Stock & Research Question

**Who drives:** LLM + Human (conversation)

**Purpose:** Fix the exact stock under analysis, its exchange/code, the investment horizon, the investor context, and the output requirements before any data is gathered.

## Procedure

1. Confirm the target security:
   - Full company name and **stock code** (e.g. `1810.HK` = Xiaomi Corporation)
   - Exchange (HKEX / SEHK) and listing board (Main Board / GEM)
   - Currency of reporting (default HKD) and financial year-end
2. Confirm the **investment horizon** (this drives which data matters):
   - Investment / long-term (>1 yr) — fundamentals, moat, valuation, SOTP
   - Trading / medium-term (weeks–months) — technicals, momentum, catalysts, regime
   - Short-term — technicals, news flow, liquidity
3. Confirm the **investor profile** (context only; the recommendation stays evidence-driven):
   - Risk tolerance, existing position (hold vs new), time horizon
   - Diversification constraints / ESG preferences
4. Confirm the **output contract**:
   - A detailed analyst note (markdown) following the Phase 9 structure
   - A final **BUY / HOLD / SELL / AVOID / WATCH** recommendation
   - Price target(s), horizon, **confidence (0–1)**, **conviction (HIGH/MEDIUM/LOW)**
   - Falsification criteria and action conditions
5. Confirm the **decision date** ("as-of") — required for anti-lookahead discipline (P9). All evidence must be dated on or before this date to justify the decision.
6. Surface assumptions, blind spots, and data-availability expectations.

## Public-Source Constraint

**Every source must be free and publicly accessible — NO paid API keys.** If a normally useful source requires a subscription/API key, mark it unavailable and substitute a free alternative. Document any closed sources in the methodology note of the report.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Stock code + exchange + reporting currency confirmed in writing
2. ✅ Investment horizon selected and documented (drives the whole analysis)
3. ✅ Investor profile captured (risk tolerance, position, constraints)
4. ✅ Output contract confirmed (analyst note + rating + target + confidence + conviction + falsification)
5. ✅ Decision ("as-of") date fixed for anti-lookahead discipline
6. ✅ Output language (e.g. English, Traditional Chinese) confirmed
7. ✅ Human approves proceeding to Phase 2
