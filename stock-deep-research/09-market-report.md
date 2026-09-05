# Phase 9: Market-Outlook Note — Final Deliverable + Watchdog Signals

**Who drives:** LLM drafts; **Human approves** and owns the investment decision

**Purpose:** Deliver an institutional-style **market-outlook note** that reads like a strategist memo, with a clear valuation band, mechanism for the view, risks, sector tilts, and **watchdog/falsification signals** — computed, sourced, dated.

## Market-Outlook Structure (strategist-style chain)

Follow the chain: **macro backdrop → market fundamentals → valuation → regime/breadth → conclusion**.

1. **Executive summary & view** — Bullish / Neutral / Bearish (+ qualifiers), target band, horizon, confidence (label + numeric score), conviction, sector tilts, headline watchdog signal.
2. **Macro & policy backdrop** — the document corpus's economic/policy read (central-bank stance, rate path, policy statements), cited verbatim.
3. **Market fundamentals** (Phase 3) — composition, concentration, aggregate earnings/revision direction, structural risks.
4. **Market valuation** (Phase 4) — percentile position, ERP spread, yield band; the **computed** fair-value band and base/bull/bear scenario window (scenario table + Monte Carlo note if run).
5. **Technicals, regime & breadth** (Phase 5) — regime label, breadth, event-windowing note; chart reference.
6. **Bull case / Bear case** (Phase 6) — both at their strongest; refutation highlights.
7. **Fragility & risks** (Phase 7) — each risk with its treatment (disclosure / band-haircut / scenario-discount) and unresolved contested signals.
8. **Conclusion** — view, target band, confidence (label + numeric score), conviction, sector tilts; **watchdog/falsification criteria** and **action conditions**.
9. **Methodology & sources** — every source cited with URL, local copy, as-of date; document corpus cited (`documents/findings-index.json` entries, appraisal IDs, event-timeline); data boundaries, reconstructions, approximations, and data gaps noted. Include the risk/disclaimer statement.

## Report Artifacts

- Output as a **timestamped** markdown file: `report/<Market>-outlook-<YYYY-MM-DD>.md`. Keep prior dated versions for diffing under ongoing monitoring (never overwrite an older file).
- Reference the index chart at `report/charts/<market>-price-<asof>.png` and the series at `data/<market>-price-history-<asof>.csv`.
- Analytics notebooks live in `notebooks/` (the tuned copies of the skill `templates/`).
- Document appraisals and the event timeline live in `documents/` (created in Phases 2, 3, and 6).

## Action Conditions & Watchdog Signals (P8)

Deliver explicit, monitorable triggers, e.g.:
- *Confirm/invalidate the Bullish view:* breadth must expand / regime stay above MA200 / valuation band hold; if any trips, revisit.
- *Confirm/invalidate the Bearish view:* derating beyond the bear target / policy-shock trigger.
- *Watch:* earnings-revision direction, index recons, scheduled policy-rate days, the specific events logged in the timeline.

## Cross-Artifact Consistency (P12/P13)

The note must be consistent with the phase artifacts (data, valuation, debate, audit, gates, documents, timeline). Propagate any final-adjustment back to the relevant phase files before marking complete.

## Anti-Lookahead & Honesty

- Present **facts / derived facts / analysis** with citations (P1) and as-of dates.
- Never present post-decision outcomes as the basis for the decision (P9); post-cutoff events stay marked and excluded.
- End with the disclaimer.

## Approval Gate (Gate 3, "STOP and ask")

**STOP.** Present the completed market-outlook note to the user for review. Do NOT mark the analysis complete until the user accepts the note or explicitly approves it.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Market-outlook note follows the full chain (macro backdrop → fundamentals → valuation → regime/breadth → conclusion)
2. ✅ View + target band + horizon + confidence + conviction + sector tilts are stated
3. ✅ Computed fair-value band and scenario table are included (not transcribed)
4. ✅ Bull/Bear cases and fragility audit are integrated, not appended
5. ✅ Watchdog/falsification criteria and action conditions are explicit and monitorable
6. ✅ All sources cited (URL + local copy + as-of date), including document-corpus citations, with disclaimer
7. ✅ Cross-artifact consistency verified (Phase 8 gates reflected accurately)
8. ✅ **STOP-and-ask Gate 3 executed** — human accepted the final note; the investment decision is theirs
9. ✅ Note saved under a timestamped filename; chart + series artifacts referenced (or reason recorded)
10. ✅ Completion checklist in SKILL.md satisfied (task_state updated, archive/review date set)