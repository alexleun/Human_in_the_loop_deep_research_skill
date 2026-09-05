# Phase 7: Fragility Audit & Red-Team — Epistemic Stress-Test

**Who drives:** LLM (destructive verification pass) + Human (identifies non-obvious weaknesses).

**Purpose:** A deliberate, adversarial self-audit before any rating — to combat AI hallucination, confirmation bias, and premature convergence (P10, P9), and to decide whether each fragility finding is **disclosure only**, a **multiple haircut**, or a **scenario discount**.

## Procedure

1. **Fragility inventory (P10):** enumerate and classify the stock's structural fragilities:
   - Geographic concentration, channel/customer concentration
   - Policy / regulatory dependence, litigation / IP exposure
   - Supply-chain bottlenecks, inventory / delivery / warranty risk
   - Controlling-shareholder / related-party / governance exposure
   For each: impact, probability, and the **required treatment** (disclosure / haircut / scenario discount) feeding Phase 4.
2. **Axiomatic citation audit (P1):** every finding flowing to the report MUST carry a `data-source` ID and confidence level. Strip any finding lacking grounding or containing an unsupported leap. Any zero-source number is removed.
3. **Steelman counter-hypotheses (red-team):** construct the strongest counter-case to the emerging thesis that fits the SAME data. Identify edge cases and boundary conditions under which the thesis fails. Record these even if not adopted.
4. **Contested-signal detection (document-intelligence):** scan `documents/findings-index.json` for `#status/{contradicted,supported,gap}` tags. Any contradiction between an official document and a news/press source, or `gap` markers on thesis-critical claims, is flagged here. Unresolved contradictions temper the confidence score in Phase 8 — they are never resolved silently in favor of either side.
5. **Anti-lookahead audit (P9):** re-verify that no post-decision (post-cutoff) information was used to justify any position. Confirm every cited figure's as-of date ≤ decision date; cross-check the event timeline for post-cutoff entries used as justification.
6. **Systems / emergence check (lightweight):** if quantitative data supports it, note reinforcing vs balancing feedback loops (e.g. network effects, inventory cycles, circular financing) and any time delays that could invalidate the thesis horizon. Optional scripted **Cognitive-Complexity / contradiction scan** over the evidence log.
7. **Reflector-style lessons (optional):** record what over-optimism or over-pessimism risks are present, to calibrate confidence in Phase 8.

## Feeding the Gates

Fragility findings and red-team outcomes are direct inputs to the **Quality Gate** and **Critical-News Override** in Phase 8 (P6), and to the fragility section of the analyst note (Phase 9).

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Fragility inventory complete, each item classified (disclosure / haircut / scenario discount)
2. ✅ Axiomatic audit run — no unsupported finding survives to the report (P1)
3. ✅ Steelman counter-hypotheses documented (even if not adopted)
4. ✅ Contested-signal scan run over `documents/findings-index.json`; contradictions and gaps surfaced, not dropped
5. ✅ Anti-lookahead audit passed — no post-decision evidence used (P9)
6. ✅ Fragility treatments are queued as inputs to Phase 4 / Phase 8 valuation and gates
7. ✅ Human has reviewed the audit for blind spots before Phase 8