# Phase 7: Synthesize & Decide — BUY / HOLD / SELL

**Who drives:** LLM proposes, **Human disposes** (final call is the human's)

**Purpose:** Combine fundamentals, valuation, technicals, and catalysts/risks into a single recommendation with an explicit decision boundary.

## Recommendation Framework

Map to an analyst-style rating scale (avoid false binary):

| Rating | Meaning |
|---|---|
| **BUY** | Attractive fundamentals + valuation offers meaningful upside vs price target and risk; risk/reward favorable |
| **HOLD** | Fairly valued currently, or fundamentals good but valuation offers insufficient margin-of-safety; wait for a better price/catalyst |
| **SELL** | Fundamentals deteriorating or valuation materially overpriced relative to risk; risk/reward unfavorable |

Support with a **price target** (HKD) and horizon.

## Decision Rule (suggested scoring approach)

Weight the evidence; do not rely on a single pillar:
- **Fundamentals** (quality/growth/financial health) — weight by horizon (heavier for long-term)
- **Valuation** (upside to fair value) — core driver of BUY/SELL
- **Technicals** (trend/timing) — refining, not primary for long-term
- **Catalysts & risks** (net balance + falsification)

A biased but transparent approach to reach a starting call:
- Positive fundamentals + positive upside → lean BUY
- Positive fundamentals + no/negative upside → HOLD
- Negative fundamentals or negative upside → SELL
- Then overlay technicals and catalysts to **confirm or override** — document why.

## Anti-Hallucination & Honesty

- Distinguish **facts** (source-quoted), **claims** (third-party, name the source), and **analyst inference** (your reasoning — label it).
- State the **confidence level** of the recommendation (high/medium/low) and what would change it (falsification criteria).
- If underlying data is thin or contradictory, say so — a **HOLD with low confidence** is more honest than a fake confident BUY.
- Always include a **regulatory/risk disclaimer**: this is research, not personalized investment advice.

## Approval Gate (Gate 2, "STOP and ask")

**STOP.** Present the proposed recommendation — rating, price target (HKD), confidence, and the 2–4 sentence thesis — to the user. Do NOT proceed to Phase 8 (report writing) until the user explicitly approves the direction or asks for revisions.

- If the user asks for changes, adjust the relevant evidence/valuation and re-present.
- If the user overrides, respect their call — they own the final decision.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ A clear BUY / HOLD / SELL recommendation is stated
2. ✅ A price target (HKD) and horizon are given
3. ✅ The decision explicitly weighs fundamentals + valuation + technicals + catalysts/risks
4. ✅ Confidence level and falsification criteria are stated
5. ✅ Facts / claims / inference are distinguished
6. ✅ **STOP-and-ask Gate 2 executed** — recommendation presented to the user and the final call left to them before Phase 8
