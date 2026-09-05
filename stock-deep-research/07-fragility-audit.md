# Phase 7: Fragility Audit & Red-Team — Market-Level Epistemic Stress-Test

**Who drives:** LLM (destructive verification pass) + Human (identifies non-obvious weaknesses)

**Purpose:** A deliberate, adversarial self-audit before any market view — to combat AI hallucination, confirmation bias, and premature convergence (P10, P9), and to decide whether each fragility finding is **disclosure only**, a **target-band haircut**, or a **scenario discount**.

## Procedure

1. **Market fragility inventory (P10):** enumerate and classify the market's structural fragilities:
   - **Concentration/crowding:** top-10 concentration (from Phase 3), single-sector dominance, crowded trades (from breadth/dispersion and positioning notes).
   - **Policy/event dependence:** rate-path and policy dependence, event risk on the timeline whose outcome is binary.
   - **Valuation fragility:** how far the current percentile is from cycle extremes and how fast a derating can overshoot.
   - **Liquidity/closing risk:** thin breadth regimes, index-suspension/closing-auction mechanics where relevant.
   For each: impact, probability, and the **required treatment** (disclosure / band-haircut / scenario-discount) feeding Phase 4 and Phase 8.
2. **Axiomatic citation audit (P1):** every finding flowing to the report MUST carry a `data-source` ID and confidence level. Strip any finding lacking grounding or containing an unsupported leap. Any zero-source number is removed.
3. **Contested-signal detection (document-intelligence):** scan `documents/findings-index.json` for `#status/{contradicted,supported,gap}` tags. A contradiction between an official document and a news/press source, or a `gap` marker on a thesis-critical claim, is flagged here. Unresolved contradictions temper the confidence score in Phase 8 — never resolved silently in favor of either side.
4. **Steelman counter-hypotheses (red-team):** construct the strongest counter-case to the emerging market view that fits the SAME data. Identify edge cases and boundary conditions under which the view fails. Record these even if not adopted.
5. **Anti-lookahead audit (P9):** re-verify that no post-decision (post-cutoff) information was used to justify any position. Re-scan `documents/event-timeline.md` — any event dated after the decision date must be excluded and marked `post-cutoff`. Confirm every cited figure's as-of date ≤ decision date.
6. **Systems / feedback check (lightweight):** note reinforcing vs balancing feedback (funding/margin spirals, index-inclusion feedback, earnings revision cycles) and time delays that could invalidate the view horizon.
7. **Reflector-style lessons (optional):** record over-optimism/over-pessimism risks to calibrate confidence in Phase 8.

## Feeding the Gates

Fragility findings and red-team outcomes are direct inputs to the **Regime Gate**, **Sanity Override**, and the **sixth confidence axis** in Phase 8, and to the fragility section of the market-outlook note (Phase 9).

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Market fragility inventory complete; each item classified (disclosure / band-haircut / scenario discount)
2. ✅ Axiomatic audit run — no unsupported finding survives to the report (P1)
3. ✅ Contested-signal scan run over `documents/findings-index.json`; contradictions and gaps surfaced, not dropped
4. ✅ Steelman counter-hypotheses documented (even if not adopted)
5. ✅ Anti-lookahead audit passed — event timeline re-scanned; no post-cutoff event or data used (P9)
6. ✅ Fragility treatments are queued as inputs to Phase 4 / Phase 8 valuation, band, and gates
7. ✅ Human has reviewed the audit for blind spots before Phase 8