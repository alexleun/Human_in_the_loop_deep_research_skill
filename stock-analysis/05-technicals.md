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
- **OHLC fetch fallback (mandatory when direct data is unavailable):** If full OHLC data cannot be fetched directly (e.g. Yahoo Finance blocks automated access):
  1. **Document the limitation** — state exactly what could not be fetched.
  2. Use **documented values from at least 2 independent aggregators** (e.g. StockAnalysis, investing.com, Meyka) for MA/RSI/levels.
  3. **Note which indicators were independently computed vs. read from third-party sources** in the outputs and report, and mark the phase's confidence accordingly.

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
