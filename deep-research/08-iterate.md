# Phase 8: Iterate — New Point of View

**Who drives:** LLM (identifies patterns), Human (validates intuition)

**Purpose:** Step back and ask: what's the bigger picture? What new framing emerges?

## Look For

- **Counterintuitive results** — X was expected to increase but decreased
- **Decoupling** — variables that should correlate don't
- **Timing asymmetries** — A leads B, not the reverse
- **Directional asymmetries** — two directions of a flow behave differently
- **Regime changes** — structural breaks in time series
- **Emerging trends** — not yet captured in existing analysis
- **Analogies** — other domains that illuminate this topic

**If new PoV needs more data/analysis → cycle to Phase 3 or 4.**
**If new PoV changes narrative → update Phase 5 and 6 outputs.**

## Backporting Iteration → Implementation Feedback

When iteration leads to a new openspec change (implementation), discoveries made during implementation must feed back into the research artifacts:

### What to backport
- **Implementation findings**: Did the implementation reveal a flawed assumption, a data gap, or a new insight? Update the research report (Phase 5) accordingly.
- **New data points**: Predictive thresholds, corrected values, or additional sources added during implementation → add to the research data files and note in the report.
- **Version bumps**: If implementation changes the research output version (e.g., added a new chapter section), bump the version string in hero meta lines and footers across all pages.

### How to backport
1. After completing each implementation task group, check: "Does this produce any data or insight that should exist in the research report?"
2. If yes, update the research artifact (Phase 5 report, Phase 6 web page, or knowledge base) before marking the implementation task complete.
3. Re-run the parity checker and date freshness audit after backporting.

**Experience note (global-heatwave):** Predictive threshold analysis (Group 4 of `research-integrity-and-forecasting`) produced computed data for three regions but no feedback loop updated the research report's version or acknowledged the new data in the research narrative. The data existed in `output/data/` and a new §9.0 was added to the integrated analysis chapter, but the synthesis page, final report executive summary, and methodology page all remained unchanged. A backport step in Phase 8 would have ensured the iteration's output was reflected in the broader research artifact set.

---

## End Conditions (NEW in v2.0)

This phase is **complete** when ALL of the following are true:

1. ✅ New point of view or reframing documented (if discovered)
2. ✅ Backporting complete — implementation findings reflected in research artifacts
3. ✅ Cross-artifact consistency re-verified after any backported changes
4. ✅ If new PoV requires more data/analysis — loop back to Phase 3 or 4
5. ✅ If new PoV changes narrative — Phase 5 and 6 outputs updated
6. ✅ `task_state.json` updated
