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
   - **Report filename convention (single source of truth):** `report/<Code>-<Company>-<YYYY-MM-DD>-analysis.md` (e.g. `report/0700-Tencent-2026-09-06-analysis.md`). This name is fixed here in Phase 1; `task_state.json` and the saved note MUST use the identical filename. If a divergence is later found, the Phase-1 contract name wins and both are corrected.
4. Identify what the user already knows / holds, and any personal constraints (risk tolerance, position size, time horizon) — for context only; the recommendation is evidence-driven.
5. Surface assumptions, blind spots, and data-availability expectations.

## Public-Source Constraint

**Every source must be free and publicly accessible — NO paid API keys.** If a normally useful source requires a subscription/API key, mark it unavailable and substitute a free alternative. Document any closed sources in the report's methodology note.

## Environment Probe (run before Phase 2)

Before any script work, probe the local environment and print ONE environment line so the fallback is decided before scripts run:

- Python version and required libraries (`pandas`, `numpy`, `matplotlib`) — check import availability.
- Docker sandbox / container availability (for charting or isolated execution).
- Console encoding — if CJK/Unicode output is expected on Windows, confirm `sys.stdout.reconfigure(encoding='utf-8')` is in every script.
- Internet reachability for the primary price/source domain (e.g. `www1.hkexnews.hk`).

If a library or container is missing, decide now whether to (a) install it, (b) use local Python with no-pandas code, or (c) note the limitation. Record the environment line in `task_state.json`.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Stock code + exchange + reporting currency confirmed in writing
2. ✅ Investment horizon selected and documented (drives the whole analysis)
3. ✅ Output contract confirmed (detailed report + BUY/HOLD/SELL + price target + rationale)
4. ✅ Output language (e.g. English, Traditional Chinese) confirmed
5. ✅ Environment probe run and recorded in `task_state.json`
6. ✅ Decision made to proceed to Phase 2 (Source & Data Collection)
