# Phase 1: Scope — Define the Market & Research Question

**Who drives:** LLM + Human (conversation)

**Purpose:** Fix the exact market or index under analysis, the evaluation horizon, the investor context, and the output requirements before any data is gathered. The **unit of analysis is a market or an index**, never an individual stock.

## Procedure

1. **Route the request** — confirm the unit of analysis is a market, index, or index group:
   - Whole-market outlook for one market or index (e.g. `HSI` = Hang Seng Index, HK market; `HSCEI`; `NKY`; `SPX`; or a named market).
   - If the request is for a **single stock**, refuse this skill and route to the single-stock skill (`stock-analysis`).
2. Confirm the **market/index identity**:
   - Index name + code, its publication authority and free home (e.g. HSI via HKEX/free aggregators).
   - Valuation universe (e.g. HSI constituents, or "HK market" = listed universe proxy).
3. Confirm the **evaluation horizon** (drives which data matters):
   - Structural / long-term (1+ yrs) — composition, aggregate earnings, valuation percentiles, secular forces.
   - Medium-term (weeks–months) — regime, breadth, momentum, catalysts, policy events.
   - Short-term — regime, breadth, technicals, news flow, liquidity.
4. Confirm the **investor context** (context only; the outlook stays evidence-driven): benchmark relative to which the view is expressed, plain-vanilla index exposure vs sector tilts, existing positioning.
5. Confirm the **output contract**:
   - A **market-outlook note** (markdown) following the Phase 9 structure.
   - A final **Bullish / Neutral / Bearish** view with an **index target band**, sector tilts, conviction (HIGH/MEDIUM/LOW), confidence (0–10), and watchdog signals.
6. Confirm the **decision date** ("as-of") — required for anti-lookahead discipline (P9). All evidence and every event must be dated on or before this date to justify the view.
7. **Document-Intelligence brief (set up in Phase 1):** note which document types anchor the outlook (policy/regulator statements, central-bank/rate calendars, index recons, earnings-season press, market-sentiment summaries) so the Phase 2 corpus is scoped before searching.
8. Surface assumptions, blind spots, and data-availability expectations for index membership/breadth.

## Public-Source Constraint

**Every source must be free and publicly accessible — NO paid API keys.** If a normally useful source requires a subscription/API key, mark it unavailable and substitute a free alternative. Document any closed sources in the methodology note of the report.

## Environment Probe (run before Phase 2)

Before any script work, probe the local environment and print ONE environment line so the fallback is decided before scripts run:

- Python version and required libraries (`pandas`, `numpy`, `matplotlib`) — check import availability.
- Docker sandbox / container availability (for charting or isolated execution).
- Console encoding — if CJK/Unicode output is expected on Windows, confirm `sys.stdout.reconfigure(encoding='utf-8')` is in every script (try/except wrapped).
- Internet reachability for the primary index-data/market domain.

If a library or container is missing, decide now whether to (a) install it, (b) use local Python with no-pandas pure-Python code, or (c) note the limitation. Record the environment line in `task_state.json`.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Market/index + authority + valuation universe confirmed in writing; single-stock requests rejected and routed
2. ✅ Evaluation horizon selected and documented (drives the whole analysis)
3. ✅ Investor context captured (benchmark, exposure shape, positioning)
4. ✅ Output contract confirmed (market-outlook note + view + target band + tilts + confidence + conviction + watchdog)
5. ✅ Decision ("as-of") date fixed for anti-lookahead discipline
6. ✅ Output language (e.g. English, Traditional Chinese) confirmed
7. ✅ Document-intelligence brief scoped (which document types anchor the outlook)
8. ✅ Environment probe run and recorded in `task_state.json`
9. ✅ Human approves proceeding to Phase 2