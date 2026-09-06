# Phase 9: Analyst Note — Final Deliverable + Action Conditions

**Who drives:** LLM drafts; **Human approves** and owns the investment decision.

**Purpose:** Deliver an institutional-style analyst note that reads like a research memo, with a clear valuation bridge, thesis, risks, recommendation, and **action conditions** — not a loose blog post or spreadsheet with a target multiple pasted on top.

## Analyst-Note Structure (Goldman-style chain)

Follow the chain: **narrative → fundamentals → valuation → fragility → conclusion**.

1. **Executive summary & rating** — the call, price target, horizon, confidence, conviction, falsification criterion.
2. **Company framing & variant view** — what the market thinks the company is vs what it economically is; what is actually new in the story.
3. **Business model & segment decomposition** (Phase 3) — revenue pools, segment economics, capital allocation.
4. **Fundamental analysis** — quality, growth, profitability, financial health, with computed metrics table + data-source IDs.
5. **Valuation** (Phase 4) — relative + DCF + SOTP + reverse-DCF reading; a **structured valuation bridge** (not a slogan) from fair value to price target; scenario table (base/bull/bear) + Monte Carlo range if run.
6. **Technicals & regime** (Phase 5) — trend, momentum, support/resistance, regime, with as-of notes.
7. **Bull case / Bear case** (Phase 6) — both at their strongest; refutation matrix highlights.
8. **Fragility & risks** (Phase 7) — each risk with its treatment (disclosure / haircut / scenario discount), key downside scenarios, and any unresolved contested signals.
9. **Conclusion** — rating, target, confidence (label + numeric score), conviction; **falsification criteria** and **action conditions** (what to monitor, and confirm/invalidate triggers).
10. **Sources & methodology** — every source cited with URL, local copy, as-of date; document corpus cited (`documents/findings-index.json` entries, appraisal IDs); data boundaries, earnings-reconciliation outcome, reverse-DCF reading, and peer FX assumptions noted. **Earnings/FCF definitions labeled** (reported vs adjusted/non-IFRS; official vs aggregator-standard FCF) — report **both** official and aggregator FCF with their definitions when they differ; revenue/turnover scope stated. Include the risk/disclaimer statement.

## Report Artifacts

- Output as a **timestamped** markdown file: `report/<Code>-<Company>-<YYYY-MM-DD>-analysis.md` — the **single source of truth** fixed in the Phase 1 output contract. `task_state.json` and the note MUST use the identical filename. If a divergence is found (e.g. `0700-Tencent-analysis-2026-09-06.md` vs `0700-Tencent-2026-09-06-analysis.md`), the Phase-1 contract name wins and both are corrected. Keep prior dated versions for diffing under ongoing monitoring (never overwrite an older file).
- Reference the chart at `report/charts/<code>-price-<asof>.png` and the daily price history at `data/<code>-price-history-<asof>.csv` (technical baseline).
- Valuation scripts (incl. reverse-DCF and sensitivity grid) live in `notebooks/`.
- Document appraisals and the event timeline live in `documents/` (created in Phases 2, 3, and 6).

## Action Conditions (P8)

Deliver explicit, monitorable conditions, e.g.:
- *Confirm:* if the key catalyst materializes / valuation pulls back to fair value → escalate toward BUY.
- *Invalidate:* if the falsification trigger trips / fragility tipping point hits → downgrade or exit.
- *Watch:* what to monitor (earnings, margins, cash flow, sector/regime, Stock Connect flows).

## Cross-Artifact Consistency (P12/P13)

The note must be consistent with the phase artifacts (data, valuation, debate, audit, gates, documents). Propagate any final-adjustment back to the relevant phase files before marking complete.

## Anti-Lookahead & Honesty

- Present **facts / derived facts / analysis** with citations (P1) and as-of dates.
- Never present post-decision outcomes as the basis for the decision (P9).
- End with the disclaimer.

## Approval Gate (Gate 3, "STOP and ask")

**STOP.** Present the completed analyst note to the user for review. Do NOT mark the analysis complete until the user accepts the note or explicitly approves it.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Analyst note follows the full chain (narrative → fundamentals → valuation → fragility → conclusion)
2. ✅ Rating + price target + horizon + confidence + conviction are stated
3. ✅ A structured valuation bridge and scenario table are included
4. ✅ Bull/Bear cases and fragility audit are integrated, not appended
5. ✅ Falsification criteria and action conditions are explicit and monitorable
6. ✅ All sources cited (URL + local copy + as-of date), including document-corpus citations, with disclaimer
7. ✅ Cross-artifact consistency verified (Phase 8 gates reflected accurately)
8. ✅ **STOP-and-ask Gate 3 executed** — human accepted the final note; the investment decision is theirs
9. ✅ Note saved under a timestamped filename; chart + price-history artifacts referenced (or reason recorded)
10. ✅ Completion checklist in SKILL.md satisfied (task_state updated, archive/review date set)