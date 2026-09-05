# Phase 4: Market Valuation — Fair-Value Band & Scenario Window

**Who drives:** LLM (scenario computation) + Human (validates assumptions)

**Purpose:** Derive an **index fair-value band** and a scenario window (base/bull/bear) that anchors the market-outlook view and the target band in Phase 9 — computed, never transcribed (P3, Sanity note).

## Procedure

1. **Load the numeric base** from `data/` (index level, P/E and P/B series, earnings-yield spread, yield band inputs from Phase 3).
2. **Run the scenario notebook** `templates/06_scenarios.py` (copied to `notebooks/` and tuned):
   - **Base:** fair value from the central valuation percentile + earnings-with-mean-reversion assumption → expected index level at horizon.
   - **Bull:** multiple re-rating to a high-but-historical percentile + above-trend earnings → upside target.
   - **Bear:** derating to a low-historical percentile + earnings hit/cut → downside target.
   - Optional **Monte Carlo** on valuation percentile + earnings paths → a distribution/band (document the number of simulations and seed).
3. **Sector valuation dispersion:** compute cross-sector P/E dispersion and top-10 concentration (feeds sector tilts and the fragility audit's crowding check). Use `05_sector_rs.py`.
4. **Sanity gates (non-negotiable, run on every script output):**
   - Units/currency assert — a nonsense index level or negative P/E is a script bug to fix and re-run, never entered into the report.
   - Plausibility band for the output targets: base/bull/bear targets must be monotonic and within ±50% of the current level (or the assumption set is wrong — revisit).
   - Cross-check the band against 1–2 aggregator fair-value/percentile reads as a third-party reference only; the computed band is what the report uses.
5. **Export JSON metric snapshot** for each run (`data/<market>-valuation-<asof>.json`) so review cycles diff cleanly.

## Anti-Lookahead Note (P9)

Scenario assumptions use only pre-cutoff data and pre-cutoff knowledge of events (see event-windowing in Phase 5). No post-decision index moves are used as "validation" of any scenario.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Base/Bull/Bear scenario notebook executed with zero errors; Monte Carlo option documented if run
2. ✅ Fair-value band + scenario targets are monotonic and sanity-checked (units/currency asserts passed)
3. ✅ Computed band cross-checked against third-party percentiles (labeled as reference)
4. ✅ Sector valuation dispersion + top-10 concentration computed (feeds tilts/audit)
5. ✅ JSON metric snapshot exported for diffing
6. ✅ No post-cutoff data used in assumptions (P9)