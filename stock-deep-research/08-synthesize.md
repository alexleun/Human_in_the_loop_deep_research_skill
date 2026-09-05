# Phase 8: Synthesize & Govern — Market View via Deterministic Gates

**Who drives:** LLM proposes; **Human disposes** (final call is the human's)

**Purpose:** Combine market fundamentals, valuation band, technicals/regime/breadth, and the Bull/Bear debate into a single market-outlook view — then run **deterministic governance gates** (P6) that cannot be talked out of position, and state confidence, conviction, and watchdog signals.

## View Scale

Map to a market-outlook view (avoids false binary):

| View | Meaning |
|---|---|
| **Bullish** | Attractive valuation + favorable regime + broadening earnings/breadth; target band implies upside |
| **Bullish-with-conditions** | Directionally positive but regime/economy not fully confirming; requires conditions to trigger |
| **Neutral** | Fairly valued or offsetting forces; range-bound expectation |
| **Bearish-with-conditions** | Directionally negative but not catastrophic; triggers needed to confirm |
| **Bearish** | Expensive + deteriorating regime; target band implies downside |

Support with an **index target band** (base/bull/bear from Phase 4), **horizon**, **confidence (0–10)**, **conviction (HIGH/MEDIUM/LOW)**, and **sector tilts**.

## Decision Flow (code-and-gate)

1. **Base view** from the qualitative weighting (fundamentals + valuation band primary for the horizon; regime/breadth refine).
2. **Run the governance gates in sequence (P6)** — deterministic, logged, non-negotiable:
   - **Regime Gate:** if regime AND market fundamentals are both bearish but the view is Bullish (e.g. overruled by news optimism), demote to Bullish-with-conditions or Neutral.
   - **Breadth Gate:** if the view is Bullish but breadth is deteriorating (declining advance/decline, falling %>MA200), demote to Neutral or Bullish-with-conditions.
   - **Sanity Override:** if every input signal points one way but the view is the opposite, flag the inconsistency and demote.
   - **Critical-News Override:** a CRITICAL negative event (policy shock, systemic credit stress, sovereign-type event) forces a Bearish-with-conditions or Bearish bias regardless of a cheap percentile — a low index P/E never overrides a critical event.
3. **Log each gate decision** with the reason.
4. **Check the debate asymmetry:** if the Bear's strongest case (Phase 6) was not refuted, reflect the added uncertainty in confidence.
5. **Fold in contested signals:** any unresolved document contradiction or structural `gap` (Phase 7) caps confidence at MEDIUM or below and is stated in the rationale.

## Honesty & Anti-Hallucination

- Distinguish **facts / derived facts / analysis** (P1) in the recommendation rationale.
- State **confidence** and **watchdog/falsification criteria** — if data is thin, say so; a transparent **Neutral-with-low-confidence** beats a fake confident Bullish.
- Always include a **regulatory/risk disclaimer**: research, not personalized investment advice.

## Confidence Scoring Rubric (six axes)

Score **0–10** across six axes and map to conviction (HIGH/MEDIUM/LOW):

| Axis | What it measures |
|---|---|
| Source quality & completeness | primary vs secondary sources, gaps found in Phase 2 |
| Data consistency | cross-aggregator agreement, freshness, reconstruction quality |
| Valuation spread | width of the fair-value band / percentile dispersion (Phase 4) |
| Technical & breadth alignment | regime/breadth confirming or contradicting the view (Phase 5) |
| Catalysts/risk clarity | how cleanly the watchdog signals can be tested (Phase 6) |
| Document/narrative evidence quality | access distribution, contradiction count, gap count in `documents/findings-index.json` (Phase 7) |

Average (or weight, documenting the weights) and map: **HIGH ≥7.5**, **MEDIUM 5.0–7.4**, **LOW <5.0**. A wide valuation spread, an unreconciled data gap, or unresolved document contradictions cap the score at MEDIUM or below. State the numeric score alongside the label in the note.

## Approval Gate (Gate 2, "STOP and ask")

**STOP.** Present the proposed market view — Bullish/Neutral/Bearish, index target band, sector tilts, horizon, confidence, conviction, and a 2–4 sentence thesis — to the user. Do NOT proceed to Phase 9 (market-outlook note) until the user explicitly approves the direction or asks for revisions.

- If the user asks for changes, adjust the relevant evidence/valuation and re-present.
- If the user overrides, respect their call — they own the final decision.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ A market view (Bullish / Neutral / Bearish, with -with-conditions qualifiers) is stated
2. ✅ Index target band, horizon, confidence, conviction, and sector tilts are stated
3. ✅ All four governance gates were run deliberately with logged reasons (P6)
4. ✅ The decision explicitly weighs fundamentals + valuation band + regime/breadth + debate
5. ✅ Confidence and watchdog/falsification criteria stated (with six-axis numeric rubric score); unresolved contested signals reflected
6. ✅ **STOP-and-ask Gate 2 executed** — recommendation presented to the user and the final call left to them before Phase 9