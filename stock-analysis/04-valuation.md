# Phase 4: Valuation — Intrinsic Worth & Price Target

**Who drives:** LLM (computation)

**Purpose:** Determine whether the current price is cheap, fair, or expensive relative to the business's worth and its peers — and derive a price target and upside/downside.

**Code-first discipline:** Write and run Python for all valuation math. Never estimate ratios from memory.

## Methods (use at least two, prefer three)

### 1. Relative Valuation (vs peers)
- Compare the stock's P/E (trailing and forward), P/B, P/S, EV/EBITDA, or sector-appropriate multiple against a defined **peer set of 3–6 real listed comparables**.
- Build the peer table with **each peer's own multiples** (not a single aggregator's composite) and compute the **relative discount/premium** of the target vs each peer and vs the set median.
- Only meaningful vs genuinely comparable businesses — adjust for growth/quality differences.

### 2. Intrinsic / DCF (if cash-flow data permits)
- Build a simple DCF: project free cash flow, apply a discount rate reflecting risk, terminal value with a sober growth rate.
- **Freeze the assumption block FIRST** — write down the full set of DCF inputs (revenue growth, margins, WACC, terminal growth) in the script before the first run. Write the **sensitivity table (growth × discount rate)** alongside.
- **Never re-tune inputs to hit a target after seeing the output.** If the first result is undesirable, that is information — not a signal to change assumptions. If a change is genuinely warranted, flag it to the user as a **revision** (e.g. a new `dcf2.py`), not a silent edit.
- Report a **fair-value range from the sensitivity grid**, not a single tuned point; the price target is chosen from that range with stated reasoning (use the median or scenario-weighted band).
- State the key assumptions explicitly so the human can challenge them.

### 3. Yield / Dividend Model (if dividend payer)
- Dividend yield vs peers and vs risk-free rate; payout sustainability from FCF.

## Outputs

- **Fair-value range** for the stock (HKD).
- **Price target** (mid-point or scenario-weighted).
- **Implied upside/downside** vs current price = (Target − Price) / Price.
- The **valuation scenario table** showing bull / base / bear cases and their probabilities/weights.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ At least two valuation methods applied (relative + one of DCF/dividend)
2. ✅ All math run by script with explicit inputs/assumptions recorded
3. ✅ A fair-value range and price target derived with upside/downside expressed
4. ✅ Sensitivity/scenario table produced (bull/base/bear)
5. ✅ Assumptions stated clearly enough for a human to challenge
6. ✅ DCF assumption block frozen before the first compute; any recalibration flagged as a revision to the user
7. ✅ Peer table uses real comparables with own multiples and computed discount/premium, not an opaque aggregate
