# Phase 4: Valuation — Relative + DCF + Reverse-DCF + SOTP

**Who drives:** LLM writes and runs the valuation scripts; Human reviews assumptions.

**Purpose:** Establish **fair value range** and a **price target** by triangulating independent valuation methods — and invert the market's implied assumption to stress-test the thesis (P5 / P9).

## Procedure

1. **Route valuation to business structure (P10 / P1):**
   - Simple core business → core **PE / EV-EBITDA**.
   - Mixed-quality businesses → **SOTP (Sum-of-the-Parts)**: value each segment with the metric it deserves (PE for profit-mature, PS for scaling) and sum to implied equity value.
   - Profit-mature + scaling blend → **hybrid PE/PS**.
   - Use added complexity only where it is not false precision.

2. **Relative valuation (code-first):**
   - Compute trailing & forward P/E, P/B, P/S, EV/EBITDA vs peers and own history.
   - State primary price source used (P2) and as-of timestamp.

3. **Intrinsic valuation (DCF, code-first):**
   - Build a DCF from cited FCF figures, explicit assumptions (terminal growth, WACC, margins).
   - Run **N-scenario** DCF (base / bull / bear) and record each fair value.
   - **Monte Carlo** (optional, when data is sufficient): sample key drivers, report a distribution of fair values.

4. **Reverse-DCF (what is the market pricing in?) — P5:**
   - Given the current market price, solve for the **implied growth rate or margin** the market is assuming.
   - Compare the implied assumption against the fundamental thesis (Phase 3). If the market implies an implausible growth rate, that is evidence for downside — a core insight for the debate.

5. **Fragility haircuts in the valuation (P10):**
   - Decide whether each fragility finding (Phase 7 inputs, or pre-screened here) warrants **disclosure only**, a **multiple haircut**, or a **scenario discount** — and apply it explicitly in the model, not as a footnote.

6. **Synthesize a fair-value range + point price target (HKD):**
   - Triangulate relative, DCF, reverse-DCF sanity, and SOTP into a range and a target.
   - State the price target with horizon, and the upside/downside to current price.

## Output

Writings + scripts: valuation model(s), a table of the band from each method (with assumptions + data-source IDs), the reverse-DCF implied-growth reading, and the derived fair-value range + price target. Any assumption-change sensitivities recorded.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Valuation routed to business structure (SOTP / hybrid / core PE chosen deliberately)
2. ✅ Relative + intrinsic (DCF, scenario) computed by executed scripts (P3)
3. ✅ Reverse-DCF run to expose the market's implied assumption (P5)
4. ✅ Fragility findings are reflected as explicit haircuts/discounts, not footnotes (P10)
5. ✅ Fair-value range + point price target (HKD) and horizon stated with assumptions
6. ✅ All inputs carry citations + data-source IDs + as-of dates
