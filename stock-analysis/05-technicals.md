# Phase 5: Technicals — Price Trend, Momentum, & Levels

**Who drives:** LLM (computation on historical price/volume)

**Purpose:** Determine the **timing** context — trend direction, momentum, overbought/oversold, and key support/resistance. Technicals refine *when*/risk, not the fundamental *whether*.

**Code-first discipline:** If historical OHLC data is obtainable from a free source, compute indicators in Python (pandas). If only limited snapshots exist, base levels on clear documented values (recent high/low) and say so.

## Indicators to Assess (use a focused set — avoid analysis paralysis)

- **Trend:** price vs moving averages (e.g. 20/50/200-day MA); higher-highs/higher-lows vs lower structure. On HK stocks, note trading halts/closing auctions.
- **Momentum:** RSI (14) — >70 overbought, <30 oversold; MACD vs signal line.
- **Support/Resistance:** recent swing highs/lows, psychological round numbers; volume at key levels.
- **Volume:** average turnover vs recent; unusual volume spikes on news.
- **Volatility:** ATR or daily range for stop placement (optional).

## Data Limitations (HK context)

- Free sources may not expose full tick history — record the **date range** actually analyzed.
- Split/dividend adjustments matter if long history is used; if only adjusted data is unavailable, note the limitation.
- **Price-freshness check (mandatory):** compare the primary close against 1–2 secondary quotes. Flag any source as stale if its quoted price differs from the live reference by >1% or is >2 trading days old. If a source fails freshness, exclude it as a primary price source and record the exclusion (as-of lag: delayed quotes are often T−1 — note it in technicals).
- **OHLC fetch fallback (mandatory when direct data is unavailable):** If full OHLC data cannot be fetched directly (e.g. Yahoo Finance blocks automated access):
  1. **Document the limitation** — state exactly what could not be fetched.
  2. Use **documented values from at least 2 independent aggregators** (e.g. StockAnalysis, investing.com, Meyka) for MA/RSI/levels.
  3. **Note which indicators were independently computed vs. read from third-party sources** in the outputs and report, and mark the phase's confidence accordingly.

## Standard Chart Output

Produce a **price + MA20/MA50/MA200 + volume** chart by default (matplotlib) and persist it under `report/charts/` (e.g. `report/charts/<code>-price-<asof>.png`). Persist the daily OHLC series used for the chart to `data/<code>-price-history-<asof>.csv` as the baseline for future technical diffs. If the chart library/container is unavailable, record the environment probe result (Phase 1) and state why the chart was not produced.

## Outputs

- Trend read (up / down / range) with the evidence (MA alignment, structure).
- Momentum read (from RSI/MACD).
- Key support and resistance levels (HKD).
- Suggested entry/risk context only — **not** a standalone trigger.
- **Confidence** in the technical picture given data quality.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Trend direction determined and justified with specific levels/indicators
2. ✅ Momentum (RSI/MACD) assessed
3. ✅ Support and resistance levels identified
4. ✅ Volume context noted
5. ✅ Data range and any adjustment limitations documented
6. ✅ Computations (if scripted) recorded with inputs
7. ✅ Price-freshness check run (stale sources excluded or flagged)
8. ✅ Standard chart produced under `report/charts/` and price series persisted to `data/` (or reason recorded)
