# Phase 4: Valuation — Intrinsic Worth & Price Target

**Who drives:** LLM (computation)

**Purpose:** Determine whether the current price is cheap, fair, or expensive relative to the business's worth and its peers — and derive a price target and upside/downside.

**Code-first discipline:** Write and run Python for all valuation math. Never estimate ratios from memory.

## Methods (use at least two, prefer three)

### 1. Relative Valuation (vs peers)
- Compare the stock's P/E (trailing and forward), P/B, P/S, EV/EBITDA, or sector-appropriate multiple against a defined peer set.
- Compute the **relative discount/premium** to sector median.
- Only meaningful vs genuinely comparable businesses — adjust for growth/quality differences.

### 2. Intrinsic / DCF (if cash-flow data permits)
- Build a simple DCF: project free cash flow, apply a discount rate reflecting risk, terminal value with a sober growth rate.
- **Never** over-lean on a single DCF assumption — run a small **sensitivity table** (growth × discount rate) and give a range, not a false precision point.
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
