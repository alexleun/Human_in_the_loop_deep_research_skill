# Phase 6: Market Debate — Bull Case vs Bear Case from Document Evidence

**Who drives:** LLM runs two independent, strongest-standard cases; Human referees.

**Purpose:** Argue the **bullish** and **bearish** market theses each at their strongest, grounded in the document corpus and the computed signals, and build the **event timeline** that dates every catalyst — before any view is reached (P5, P8).

## Procedure

1. **Generate inputs independently, in order:**
   - Feed the Bull the combined output of Phases 3–5 plus the document corpus. The Bull builds the strongest case: the re-rating story, earnings upgrade cycle, breadth expansion, what the market is missing.
   - Separately, feed the Bear the SAME inputs (independent, unbiased). The Bear leads with the strongest material risk (policy shift, earnings cut, crowded positioning, valuation derating, event risk).
   - Record each side as a standalone note (`debate/bull.md`, `debate/bear.md`) before any synthesis.
2. **Document grounding:** translate each side's claims into **document evidence** — policy statements, regulator releases, index-authority communications, press releases, news — cited with verbatim quotes or `[inferred from {access type}]` markers pointing into `documents/findings-index.json`. A claim without a document or a computed number is flagged, not asserted.
3. **Event timeline build:** run `templates/08_event_timeline.py` on the dated findings to render `documents/event-timeline.md`, then annotate it with the Bull's and Bear's interpretation of each event. Enforce the as-of window (≤ decision date); mark later events `post-cutoff` (P9).
4. **Refutation pass:** cross-read the two notes; identify which Bull points the Bear refutes and vice-versa. Flag any claim that does not survive the strongest opposing argument.
5. **Catalysts & risks ledger:** map each catalyst/risk to an event in the timeline, with timing, probability, and link to the valuation band (Phase 4). Draft the falsification criteria (P8).
6. **Stay objective-driven (P1/P5):** frame "generate the strongest bull case" / "generate the strongest bear case" — do not assign personas or role-play.

## Output

`debate/bull.md`, `debate/bear.md`, an annotated `documents/event-timeline.md`, a refutation matrix, and a catalysts/risks ledger cross-linked to the timeline. These are primary inputs to Phase 7 (fragility audit) and Phase 8 (synthesis + gates).

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Bull and Bear cases are each written at their strongest, before any synthesis
2. ✅ Every debate claim carries a computed number or a document quote (`[inferred]` allowed with marker) — no unsupported assertions
3. ✅ `documents/event-timeline.md` built/annotated with as-of windowing; post-cutoff events excluded and marked
4. ✅ A refutation matrix exists (each side's points tested against the strongest opposition)
5. ✅ Catalysts/risks ledger cross-linked to timeline entries with timing/probability/source
6. ✅ Falsification criteria are drafted (what would invalidate the market view)
7. ✅ No view is yet stated — this phase produces inputs only