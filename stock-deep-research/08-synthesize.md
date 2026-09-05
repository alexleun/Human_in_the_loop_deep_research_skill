# Phase 8: Synthesize & Govern — Rating via Deterministic Gates

**Who drives:** LLM proposes; **Human disposes** (final call is the human's).

**Purpose:** Combine fundamentals, valuation, technicals/regime, and the Bull/Bear debate into a single recommendation — then run **deterministic governance gates** (P6) that cannot be talked out of position, and state confidence, conviction, and falsification.

## Rating Scale

Map to a 7-state analyst rating (avoids false binary):

| Rating | Meaning |
|---|---|
| **STRONG_BUY / BUY** | Attractive fundamentals + valuation offers meaningful upside vs price target; risk/reward favorable |
| **HOLD** | Fairly valued; or good fundamentals but valuation offers insufficient margin-of-safety; wait for price/catalyst |
| **WATCH** | Low conviction, no material risk yet — monitor; do not force HOLD |
| **AVOID** | Material risk (fraud / bankruptcy / sanctions / major litigation) — do not engage |
| **SELL** | Hold an existing position and exit; fundamentals deteriorating or materially overpriced |

Support with a **price target (HKD)**, **horizon**, **confidence (0–1)**, and **conviction (HIGH/MEDIUM/LOW)**.

## Decision Flow (code-and-gate)

1. **Base call** from the qualitative weighting (fundamentals + valuation upside primary for long horizon; technicals/regime refine).
2. **Run the governance gates in sequence (P6)** — deterministic, logged, non-negotiable:
   - **Quality Gate:** if BUY/STRONG_BUY but the company is low quality (not profitable / weak balance sheet / no growth), demote to HOLD with reduced confidence.
   - **Regime Gate:** if BOTH technical AND fundamental are bearish but the call is BUY (e.g. overruled by news optimism), demote to HOLD.
   - **Sanity Override:** if every input signal is bearish but the call is BUY (or vice-versa), flag inconsistency and demote to HOLD.
   - **Critical-News Override:** a CRITICAL negative event (fraud / bankruptcy / sanctions / major lawsuit) forces **SELL** (if holding) or **AVOID** (if not engaged) with high confidence — regardless of a cheap valuation. A low P/E never overrides a critical event.
3. **Log each gate decision** with the reason (as in the DataPai pattern).
4. **Check the debate asymmetry:** if the Bear's strongest case (Phase 6) was not refuted, reflect the added uncertainty in confidence.

## Honesty & Anti-Hallucination

- Distinguish **facts / derived facts / analysis** (P1) in the recommendation rationale.
- State **confidence** and **falsification criteria** — if data is thin, say so; a transparent **HOLD / WATCH with low confidence** beats a fake confident BUY.
- Always include a **regulatory/risk disclaimer**: research, not personalized advice.

## Approval Gate (Gate 2, "STOP and ask")

**STOP.** Present the proposed recommendation — rating, price target (HKD), horizon, confidence, conviction, and the 2–4 sentence thesis — to the user. Do NOT proceed to Phase 9 (analyst note) until the user explicitly approves the direction or asks for revisions.

- If the user asks for changes, adjust the relevant evidence/valuation and re-present.
- If the user overrides, respect their call — they own the final decision.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ A rating (BUY / HOLD / SELL / AVOID / WATCH) is stated
2. ✅ Price target (HKD), horizon, confidence, and conviction are stated
3. ✅ All four governance gates were run deliberately with logged reasons (P6)
4. ✅ The decision explicitly weighs fundamentals + valuation + technicals/regime + debate
5. ✅ Confidence and falsification criteria are stated
6. ✅ **STOP-and-ask Gate 2 executed** — recommendation presented to the user and the final call left to them before Phase 9
