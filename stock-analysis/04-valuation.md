# Phase 4: Valuation — Intrinsic Worth & Price Target

**Who drives:** LLM (computation)

**Purpose:** Determine whether the current price is cheap, fair, or expensive relative to the business's worth and its peers — and derive a price target and upside/downside.

**Code-first discipline:** Write and run Python for all valuation math. Never estimate ratios from memory.

## Methods (use at least two, prefer three)

### 1. Relative Valuation (vs peers)
- Compare the stock's P/E (trailing and forward), P/B, P/S, EV/EBITDA, or sector-appropriate multiple against a defined **peer set of 3–6 real listed comparables**.
- Build the peer table with **each peer's own multiples** (not a single aggregator's composite) and compute the **relative discount/premium** of the target vs each peer and vs the set median.
- Only meaningful vs genuinely comparable businesses — adjust for growth/quality differences.
- **Forward-EPS dispersion check (before applying a forward P/E):** sample 2+ estimate sources (e.g. forward P/E-implied EPS vs a named broker's estimate). If max/min differ by more than ~20%, prefer a **scenario-weighted valuation** and disclose the implied EPS range in the report — do not apply a single forward P/E blindly.
- **Peer FX treatment:** state each peer's reporting currency (USD vs HKD vs CNY). Either adjust peers to a common earnings basis or disclose the FX assumption in the report methodology. Never compare raw multiples across currencies without a note.

### 2. Intrinsic / DCF (if cash-flow data permits)
- Build a simple DCF: project free cash flow, apply a discount rate reflecting risk, terminal value with a sober growth rate.
- **Freeze the assumption block FIRST** — write down the full set of DCF inputs (revenue growth, margins, WACC, terminal growth) in the script before the first run. Write the **sensitivity table (growth × discount rate)** alongside.
- **Never re-tune inputs to hit a target after seeing the output.** If the first result is undesirable, that is information — not a signal to change assumptions. If a change is genuinely warranted, flag it to the user as a **revision** (e.g. a new `dcf2.py`), not a silent edit.
- Report a **fair-value range from the sensitivity grid**, not a single tuned point; the price target is chosen from that range with stated reasoning (use the median or scenario-weighted band).
- State the key assumptions explicitly so the human can challenge them.
- **Units & currency sanity gate:** after each script run, assert the output is plausible. A per-share value must lie in a sane band (e.g. `0 < price-target < 100 × reported EPS`, per-share ≥ 0, currency labels correct). If a run prints nonsense (e.g. `HK$37,084` from a /1000 or USD→HKD bug), fix the script and re-run before accepting the number — never enter a suspect figure into the report. Add a `check_units()` helper or `--sanity` flag to the notebook template.

### 2b. Reverse-DCF (implied growth) — required
Invert the current market price to read what the market is pricing in, and compare it to your fundamental thesis:
- Given price + model (WACC, terminal growth), solve for the **implied revenue growth or margin**.
- Report the implied assumption vs your Phase 3 growth view. If the market implies an implausible growth rate, that is evidence for the downside case.
- Concrete script sketch: root-solve `Price(DCF(g)) − market price = 0` over a grid of `g`, print the implied `g`. Do not skip this and do not leave it as an aspirational task — it is part of the valuation phase.
- If data genuinely prevents reverse-DCF, say so explicitly in the report and record the gap, rather than silently omitting it.

### 3. Yield / Dividend Model (if dividend payer)
- Dividend yield vs peers and vs risk-free rate; payout sustainability from FCF.
- Sanity-check the payout ratio printout (a 0% payout from a dividend payer is a red flag — usually a script bug, not a fact).

## Outputs

- **Fair-value range** for the stock (HKD).
- **Price target** (mid-point or scenario-weighted).
- **Implied upside/downside** vs current price = (Target − Price) / Price.
- The **valuation scenario table** showing bull / base / bear cases and their probabilities/weights.
- A **Reverse-DCF implied-growth** reading.
- Script outputs that passed the **units/currency sanity gate** (or the fix that made them pass).

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ At least two valuation methods applied (relative + one of DCF/dividend)
2. ✅ All math run by script with explicit inputs/assumptions recorded
3. ✅ A fair-value range and price target derived with upside/downside expressed
4. ✅ Sensitivity/scenario table produced (bull/base/bear)
5. ✅ Assumptions stated clearly enough for a human to challenge
6. ✅ DCF assumption block frozen before the first compute; any recalibration flagged as a revision to the user
7. ✅ Peer table uses real comparables with own multiples and computed discount/premium, not an opaque aggregate
8. ✅ Units/currency sanity gate passed for every script output (or the fix is recorded)
9. ✅ Reverse-DCF run (or explicitly recorded as a gap with reason)
10. ✅ Forward-EPS dispersion checked (range disclosed if > ~20% across sources)
11. ✅ Peer reporting currencies stated with FX treatment or disclosed assumption
