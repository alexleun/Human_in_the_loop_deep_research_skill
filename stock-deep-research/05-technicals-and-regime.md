# Phase 5: Technicals, Regime & Breadth — Timing, State, and Event Window

**Who drives:** LLM (calculates and drafts) + Human (validates timing context)

**Purpose:** Classify the market's **technical regime** (trend, momentum, volatility), its **breadth** (how widely the move is shared), and window the events that legitimately bear on the outlook. This is the timing/risk context that feeds the governance gates (P6) and refinement of the scenario band.

## Procedure

1. **Regime notebook** `templates/02_regime.py`:
   - Trend: index vs MA200, trend structure of MA20/50/200.
   - Momentum: 12M−1M momentum, RSI, rates-of-change; alignment across timeframes.
   - Volatility state: realized vol percentile -> high/normal/low; rolling Sharpe (`01_index_stats.py`).
   - Composite regime label: Bull / Neutral / Bear / Volatile-with-trend.
2. **Breadth notebook** `templates/03_breadth.py`:
   - % constituents above MA200, advance/decline, new highs/lows, cross-sectional dispersion.
   - If member-level data is unavailable, use the documented approximation from Phase 2 and label the approximation in the output and the report.
3. **Event-windowing (anti-lookahead, mandatory):**
   - Build `documents/event-timeline.md` and window events to **as-of ≤ decision date** (policy-rate days, earnings season, index recons, press triggers).
   - Events dated **after** the decision date are excluded and marked `post-cutoff` — they never justify the view (P9). This rule holds even when they appear to confirm the current narrative.
4. **Price-freshness check (mandatory):** compare the primary index close against 1–2 secondary quotes. Flag any source stale by >1% or >2 trading days; exclude it as primary and record the exclusion.
5. **Standard chart output:** produce the index **price + MA20/50/200 + volume** chart (`templates/chart.py`), persist to `report/charts/<market>-price-<asof>.png`, and keep the series baseline at `data/<market>-price-history-<asof>.csv`.
6. **Synthesize a technical stance:** bullish / bearish / neutral with confidence, and reconcile with the fundamental bias (Phase 3) and valuation band (Phase 4).

## Feeding the Gates

The regime + breadth + stance are **inputs to the Regime Gate** and **Sanity Override** in Phase 8 (P6):
- If regime AND market fundamentals are both bearish but the synthesized view is Bullish → **Regime Gate** demotes to Bullish-with-conditions or Neutral.
- If all input signals point one way but the view is the opposite → **Sanity Override** flags and demotes.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Regime and breadth notebooks executed with zero errors; composite regime classified
2. ✅ Event-windowing done — `documents/event-timeline.md` has only in-window events as admissible evidence; post-cutoff events marked and excluded
3. ✅ Breadth documented with approximation noted where member data was unavailable
4. ✅ Technical stance + confidence stated (bullish/bearish/neutral)
5. ✅ Price-freshness check run (stale sources excluded or flagged)
6. ✅ Standard chart produced under `report/charts/` and series persisted to `data/` (or reason recorded)
7. ✅ Regime/breadth/technical inputs exported for the Phase 8 governance gates