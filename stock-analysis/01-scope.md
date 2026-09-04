# Phase 1: Scope — Define the Stock & Research Question

**Who drives:** LLM + Human (conversation)

**Purpose:** Fix the exact stock under analysis, its exchange/code, the investment horizon, and the output requirements before any data is gathered.

## Procedure

1. Confirm the target security:
   - Full company name and **stock code** (e.g. `1810.HK` = Xiaomi Corporation)
   - Exchange (HKEX / SEHK) and listing board (Main Board / GEM)
   - Currency of reporting (HKD) and financial year-end
2. Confirm the **investment horizon** being analyzed (this drives which data matters):
   - Investment / long-term (>1 yr) — emphasize fundamentals, moat, valuation
   - Trading / medium-term (weeks–months) — emphasize technicals, momentum, catalysts
   - Short-term — emphasize technicals, news flow, liquidity
3. Confirm the **output contract**:
   - A detailed written report (markdown) covering all required sections
   - A final **BUY / HOLD / SELL** recommendation with price target(s) and rationale
   - Explicit confidence level and key risk disclosure
4. Identify what the user already knows / holds, and any personal constraints (risk tolerance, position size, time horizon) — for context only; the recommendation is evidence-driven.
5. Surface assumptions, blind spots, and data-availability expectations.

## Public-Source Constraint

**Every source must be free and publicly accessible — NO paid API keys.** If a normally useful source requires a subscription/API key, mark it unavailable and substitute a free alternative. Document any closed sources in the report's methodology note.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Stock code + exchange + reporting currency confirmed in writing
2. ✅ Investment horizon selected and documented (drives the whole analysis)
3. ✅ Output contract confirmed (detailed report + BUY/HOLD/SELL + price target + rationale)
4. ✅ Output language (e.g. English, Traditional Chinese) confirmed
5. ✅ Decision made to proceed to Phase 2 (Source & Data Collection)
