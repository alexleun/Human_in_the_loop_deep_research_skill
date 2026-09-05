# Phase 5: Technical & Market Regime — Trend, Momentum, Support/Resistance

**Who drives:** LLM (calculates and drafts) + Human (validates timing context).

**Purpose:** Provide timing and risk context and a **market-regime read** that feed the governance gates (P6). Technicals refine and time; the fundamental thesis leads for long horizons.

## Procedure

1. **Compute technicals by script (P3)** from a stated primary price source:
   - **Trend:** moving averages (20/50/200-day), trend structure.
   - **Momentum:** RSI, MACD, rates-of-change; alignment across timeframes.
   - **Support/resistance:** recent swing levels, volume profile, gaps.
   - **Breadth/volume:** volume confirmation, average turnover; note any trading suspension/halt (HK-specific).
2. **Market regime read** (top-down context):
   - Classify broad market environment (Bull / Bear / Sideways / Volatile) for the relevant index (e.g. Hang Seng, HSCEI).
   - Note Stock Connect / northbound flows where they are a material catalyst.
3. **Synthesize a technical stance:** bullish / bearish / neutral, with confidence, and reconcile with the fundamental bias.
4. **Anti-lookahead:** only use price/volume data with an as-of date ≤ the decision date (P9). Do not use post-decision price action to justify the call.

## Technical-Data Fallback (mandatory when direct OHLC is unavailable)

If a clean daily OHLC series cannot be fetched directly (e.g. robot-blocked or only reconstructed data available):

1. **Document the limitation** — state exactly what could not be fetched or was reconstructed.
2. Use **authoritative trend/momentum values from at least 2 independent aggregators** (e.g. stockanalysis.com MAs/RSI cross-referenced with a second source) and record which values came from where.
3. **Note explicitly which indicators were independently computed vs. read from third-party sources**, and mark the technical confidence accordingly. This is a residual limitation — do not present third-party readings as your own computation.

## Feeding the Gates

The technical stance and regime read are **inputs to the Regime Gate** and **Sanity Override** in Phase 8 (P6):
- If both technical AND fundamental are bearish but the synthesized call is BUY → **Regime Gate** demotes to HOLD.
- If all input signals point one way but the call is the opposite → **Sanity Override** flags and demotes.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Trend, momentum, and support/resistance computed by executed scripts (P3)
2. ✅ Market regime classified for the relevant index, with source + as-of date
3. ✅ Trading halts / liquidity notes recorded where relevant (HK)
4. ✅ Technical stance + confidence stated (bullish/bearish/neutral)
5. ✅ No post-decision (lookahead) data used to justify any position (P9)
6. ✅ Technical + regime inputs are exported for the Phase 8 governance gates
7. ✅ If OHLC was not directly fetched: limitation documented, ≥2 aggregators cross-referenced, computed-vs-third-party noted
