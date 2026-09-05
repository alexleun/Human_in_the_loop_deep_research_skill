---
name: stock-deep-research
description: "A whole-market, computation-native deep-research workflow for producing a Bullish / Neutral / Bearish market outlook with an index target band, sector tilts, confidence, and conviction. Computes every quantitative signal by executed code from fetched or reconstructed series (index statistics, regime, breadth, valuation percentiles, sector relative strength, scenarios) and embeds a document-intelligence layer (search protocol, coverage report, deep-read appraisals, findings index, event timeline). Optimal for HK / HSI / HSCEI and generalizes to other indices. NOT for single stocks."
---

# Stock Deep-Research Skill (v2.0) — Whole-Market Outlook

A **whole-market, computation-native analytics skill** for producing an **index-level market outlook** — optimized for **Hong Kong / HSI / HSCEI** and generalizing to other indices. **The unit of analysis is a market or an index, never an individual stock.** Every quantitative signal is **computed by executed code** from fetched or reconstructed series, not transcribed from aggregators. Produces an **institutional-grade market-outlook note** with a **Bullish / Neutral / Bearish** view, an **index target band**, **sector tilts**, **confidence (0–10)**, **conviction**, and **watchdog/falsification signals**.

**v2.0 — repurposed from single-stock to whole-market:** This skill was formerly the second single-stock skill (v1.1/v1.2). In v2.0 it is repurposed so that the two stock skills are cleanly complementary: **`stock-analysis`** is now the single canonical single-stock skill (it absorbed the single-stock institutional methodology: debate, fragility audit, governance gates, SOTP/reverse-DCF, AVOID/WATCH), and **`stock-deep-research`** is the whole-market, index-level skill. This version is computation-native (starter Python templates shipped under `templates/`) with a document-intelligence layer (search protocol, coverage report, deep-read appraisals, `documents/findings-index.json`, event timeline). The prior single-stock content was folded into `stock-analysis`; see the CHANGELOG and its README row.

The final investment call always belongs to the **human**. This skill proposes; the user disposes.

This skill adapts best-practice patterns from the public literature and the in-repo deep-research/culture-research skills:

| Source | Pattern adopted |
|---|---|
| FinanceHarness (arXiv 2607.27853) / quant frameworks | Layered finance tool surface; evidence-first; **pre/post-cutoff anti-lookahead** discipline |
| DataPai Stock Intelligence | **Governance gates** (Regime / Breadth / Sanity / Critical-News), multi-state view, confidence + conviction |
| Macbeth-style scenario planning / quant practice | Base/Bull/Bear + Monte Carlo target band; sector relative strength; **computation-native** signals |
| Culture-research skill (in-repo) | Document intelligence: search protocol, coverage report, deep-read appraisals, dual `#access/#evidence` tags, verbatim-quote rule, findings index |
| deep-research skill (in-repo) | Source hierarchy + URL verification + review manifest; code-first analysis |

---

## When to Use This Skill

- Forming a whole-market or index-level outlook (Bullish / Neutral / Bearish) — e.g. Hang Seng Index, HK market, HSCEI, or a named global index/market.
- Data must come from **free, public sources** — no paid API key.
- Output is a **market-outlook note + index target band + sector tilts**, not a live dashboard or a single-stock recommendation.

**Not for:** analyzing a **single stock** — that is `stock-analysis`. Also not for executing trades, portfolio rebalancing, backtesting strategies, or building a factor model.

---

## Core Principles

### P1. Evidence Before Narrative (anti-hallucination)
Narrative must be **translated into economics** and every factual output must carry an **exact quote** (document corpus) or **citation + as-of date** (numeric series). Use the **Fact / Derived-Fact / Analysis** taxonomy:
- **Fact** — directly supported by a cited or frozen source.
- **Derived fact** — calculated from supported inputs with an explicit formula and matching time boundary (e.g. index P/E from level × index earnings proxy).
- **Analysis** — interpretation, scenario, or valuation-model conclusion (labeled as such).

A model may complete an analysis chain; it may **never invent a missing fact**. Any zero-source number is stripped from the report.

### P2. Public-Source Only (No API Keys)
All data from free, public sources. If a source is paywalled/API-gated, substitute a free alternative and document it. **Never fabricate data.**

### P3. Computation-Native Analysis (code first)
Every quantitative signal — index statistics, regime, breadth, valuation percentile, sector relative strength, scenarios — is **computed by running Python** on fetched or reconstructed series, never transcribed from an aggregator. On Windows, prefix scripts with `sys.stdout.reconfigure(encoding='utf-8')` (try/except wrapped) to avoid cp950 console crashes. Scripts are tuned copies of the skill `templates/`.

### P4. Blended Analysis (Fundamentals + Valuation + Technicals + Debate + Documents)
A defensible market view requires all of:
- **Market fundamentals** — composition, concentration, aggregate earnings/revisions, valuation position
- **Market valuation** — computed fair-value band, ERP spread, scenario window
- **Technicals, regime & breadth** — trend, momentum, volatility state, breadth
- **Adversarial debate** — the Bull and Bear market cases argued at their strongest, plus catalysts and risks
- **Document intelligence** — policy/regulator/market/press/news evidence, quoted verbatim

### P5. Adversarial Bull/Bear Debate
Run the Bull and Bear cases **independently and at their strongest**. Do not let one side see the other's conclusion first. The synthesis weighs both strongest cases rather than a one-sided narrative.

### P6. Governance Gates (deterministic guardrails)
Before publishing a view, run **rule-based, non-negotiable gates**:
- **Regime Gate** — if regime AND fundamentals are both bearish but the view is Bullish, demote to Bullish-with-conditions or Neutral.
- **Breadth Gate** — a Bullish view with deteriorating breadth is demoted to Neutral or Bullish-with-conditions.
- **Sanity Override** — if all signals point one way but the view is the opposite, flag and demote.
- **Critical-News Override** — a CRITICAL negative event (policy shock, systemic credit stress) forces a bearish bias regardless of a cheap percentile.

### P7. Integrity of Recommendation
Give a **view (Bullish / Neutral / Bearish, with optional qualifiers)**, **index target band**, **horizon**, **confidence (0–10)**, **conviction (HIGH/MEDIUM/LOW)**, and **sector tilts**. If data is thin or contradictory, say so. Always end with a risk/disclaimer statement: research, not personalized advice.

### P8. Falsification / Watchdog Discipline
Every market view must carry an explicit **watchdog/falsification criterion** and **action conditions** (signals that confirm/invalidate the view). If one trips, the view is revisited immediately.

### P9. Anti-Lookahead / Event-Windowing Discipline
Distinguish **pre-cutoff evidence** (findable facts, as-of ≤ decision date) from **post-cutoff reasoning**. Window events (policy-rate days, earnings season, index recons, press triggers) to ≤ decision date; events dated after the decision date are excluded and marked `post-cutoff` — they never justify the view, even when they appear to confirm it.

### P10. Fragility Audit (not just a disclaimer)
Treat market fragility as a **valuation input**, not an appendix. Assess concentration/crowding, policy/event dependence, valuation fragility, liquidity/breadth risk. Decide whether each warrants **disclosure only**, a **target-band haircut**, or a **scenario discount**.

### P11. Source Preservation (P20 deep-research)
Save a **local copy** of every source before extracting findings (`sources/…`, `documents/…`) and index them in `sources_index.md`. Without local copies, findings are unrecoverable if URLs change.

### P12. End-Conditions Discipline
Every phase defines **end conditions as a checklist**. The LLM exits a phase only when all end conditions are true, and the human verifies at gates.

### P13. Human-Approval Gates (explicit "STOP and ask")
- **Gate 1 (Phase 1 → 2):** STOP — present the proposed market scope, horizon, investor context, and output contract; do NOT proceed to Phase 2 until the human confirms.
- **Gate 2 (Phase 8 → 9):** STOP — present the proposed market view (Bullish/Neutral/Bearish, target band, tilts, confidence, conviction, thesis) produced in Phase 8; do NOT proceed to the market-outlook note (Phase 9) until the human approves.
- **Gate 3 (Phase 9):** STOP — present the final market-outlook note; do NOT mark the analysis complete until the human accepts it.
Gates are implemented as explicit "stop and ask" mechanisms, not conceptual checkpoints. The LLM proposes, the human disposes.

---

## Workflow Overview

```
Phase 1: Scope ── market/index, horizon, investor context, output contract, doc-intel brief
   │  (human approval gate 1; single-stock requests rejected/routed)
   ▼
Phase 2: Collect & Preserve ── numeric base (Part A) + document corpus (Part B)
   │
   ▼
Phase 3: Market Fundamentals ── composition, concentration, earnings/revisions, valuation position
   │
   ▼
Phase 4: Market Valuation ── computed fair-value band + base/bull/bear scenario window
   │
   ▼
Phase 5: Technicals, Regime & Breadth ── regime, breadth, event-windowing, standard chart
   │
   ▼
Phase 6: Market Debate ── Bull vs Bear from document evidence + event timeline
   │
   ▼
Phase 7: Fragility Audit & Red-Team ── concentration/crowding, contested signals, anti-lookahead
   │
   ▼
Phase 8: Synthesize & Govern ── governance gates → view + target band + tilts + confidence
   │  (human approval gate 2)
   ▼
Phase 9: Market-Outlook Note ── macro → fundamentals → valuation → regime → conclusion + watchdog
   │  (human approval gate 3)
```

**Phase revisiting is normal.** A fragility surprise in Phase 7 may send you back to Phases 3–4. Do not force a single pass.

**Phase revisiting triggers (proactive, not reactive):**
- A new source or policy event changes a core input → revisit **Phase 2–3** and recompute the affected metrics.
- Phase 4 valuation band contradicts a Phase 3 earnings assumption → revisit **Phase 3** before finalizing valuation.
- Phase 6 reveals a risk that changes an assumption → revisit **Phase 3–4** before synthesis.
- Phase 7 fragility audit finds a concentration/anti-lookahead issue → revisit the affected phase.

Each revisit must be recorded in `task_state.json` (updated phases + reason) before moving on.

---

## Phase Router

**Before each phase, load its phase file with the `read` tool** — e.g. before Phase 4, read `04-market-valuation.md` and follow its procedure and end conditions. Do not work from this overview alone.

| Current Task | Load This File |
|---|---|
| Defining market/index, horizon, investor context, output contract | `01-scope.md` |
| Collecting numeric base + document corpus | `02-collect.md` |
| Analyzing market fundamentals (composition, earnings, valuation position) | `03-market-fundamentals.md` |
| Valuing the market (fair-value band + scenarios) | `04-market-valuation.md` |
| Reading regime, breadth, event window, chart | `05-technicals-and-regime.md` |
| Running the Bull/Bear market debate + event timeline | `06-market-debate.md` |
| Auditing market fragility, contested signals, anti-lookahead | `07-fragility-audit.md` |
| Synthesizing + running governance gates to set the view | `08-synthesize.md` |
| Writing the final market-outlook note with watchdog signals | `09-market-report.md` |

---

## Suggested File Layout

```
{project_root}/
├── stock-deep-research-{market}/  # one suffixed dir per market/run
│   ├── task_state.json            # multi-session state (phase, progress, decisions, environment line)
│   ├── sources/
│   │   ├── sources_index.md       # every source: URL + local copy + access date + evidence_status/access tags
│   │   └── YYYY-MM-DD-<desc>.{html,pdf,md,json}   # preserved local copies (mandatory)
│   ├── documents/                 # document-intelligence layer
│   │   ├── search-protocol.md     # written before searching (types, hierarchy, criteria)
│   │   ├── coverage-report.md     # honest gap flagging (never padded)
│   │   ├── candidate-list.md      # deduplicated candidate documents
│   │   ├── appraisals/            # {doc-id}.md deep-read appraisals (verbatim quotes)
│   │   ├── findings-index.json    # machine-readable finding index (id, source_doc, quote, tags)
│   │   └── event-timeline.md      # dated market events (anti-lookahead window)
│   ├── data/                      # computation-native numeric base
│   │   ├── raw/                   # unaltered downloads
│   │   ├── <market>-price-history-<asof>.csv   # index price series (baseline)
│   │   ├── <market>-valuation-<asof>.json      # per-run metric snapshot
│   │   └── README.md              # provenance: sources, dates, approximations, as-of cutoff
│   ├── notebooks/                 # tuned copies of the skill templates + analysis scripts
│   ├── debate/                    # bull.md, bear.md, judge_notes.md
│   ├── report/
│   │   ├── <Market>-outlook-<YYYY-MM-DD>.md    # timestamped final deliverable
│   │   └── charts/
│   │       └── <market>-price-<asof>.png      # index price + MA + volume chart
│   └── skill-evolution-log.md     # lessons learned (mandatory)
└── (skill home)/templates/        # starter Python notebooks shipped with the skill
    ├── 01_index_stats.py
    ├── 02_regime.py
    ├── 03_breadth.py
    ├── 04_market_valuation.py
    ├── 05_sector_rs.py
    ├── 06_scenarios.py
    ├── 08_event_timeline.py
    └── chart.py
```

## Computation-Native Templates

Copy the matching starter from `templates/` into the run's `notebooks/`, tune the market code / data paths / as-of cutoff, and **run it**. Every signal used in the report is produced by one of these scripts (or an equivalent written for the run); it is never copied from an aggregator. Sanity gates in each template protect against nonsense output.

## Task Ticking Discipline

Running inside an OpenSpec change, tick tasks **at the end of each phase**, not at archive time. When a phase's end conditions pass, mark its `- [ ]` rows complete in `tasks.md` before starting the next phase. A single end-of-run sweep hides where each phase actually finished.

---

## HK-Specific Data Notes

- **Market data:** HSI/HSCEI values, P/E, P/B, and dividend yield via free aggregators (HKEX EOD data, Yahoo Finance HK, AAStocks, Investing.com); always record as-of dates and cross-check primary/secondary.
- **Official/regulator:** HKEX and SFC communications, Census & Statistics Department releases, HKMA monetary-policy and rate statements — the authoritative document layer for an HK market outlook.
- **Policy calendar:** HKMA interest-rate decisions (linked to Fed actions), government budget, Market Development Council / Stock Connect policy statements — log on the event timeline.
- **Breadth data:** full constituent membership can be licensed; for a free basis use a documented approximation (a liquid subset / ETF constituents) and label it (Phase 2/5).
- **Liquidity/closing:** HK closing auction and index-suspension mechanics can distort EOD series — note any day that affects the technical picture.

---

## Post-Report Lifecycle

The analysis does not end at note approval. After Gate 3:

1. **Archive the OpenSpec change** (if the analysis ran inside one): `openspec archive <change-name> --yes`.
2. **Preserve the spec** for future diffing — the archived change keeps the baseline for comparison.
3. **Set a review reminder date** (e.g. next scheduled policy-rate day, or the horizon) and record it in `task_state.json`.
4. **Start a review** with `openspec-new-change` using the same scope, and diff the new findings against the archived baseline. The note's watchdog signals and event timeline tell you what to re-check.
5. **Update the skill-evolution log** with what worked / what caused problems for the next outlook.

## Completion Checklist ("Done" State)

The analysis is **complete** — nothing more to add — when ALL of the following are true:

1. ✅ Market-outlook note written and saved at a timestamped path `report/<Market>-outlook-<YYYY-MM-DD>.md`
2. ✅ `task_state.json` updated with the final view (Bullish/Neutral/Bearish, target band, confidence score, status)
3. ✅ Human has approved the final note (Gate 3)
4. ✅ OpenSpec change archived (if run inside one), with tasks.md fully ticked
5. ✅ Review reminder date set
6. ✅ Skill evolution log updated (mandatory)

---

## Guardrails

- **Evidence before narrative** — every number and every document claim needs a citation (verbatim quote) and as-of date (P1)
- **Computation-native** — compute every signal by executed script; never transcribe an aggregator reading (P3)
- **Propose before deciding** — no market view without all prior phases complete (P13)
- **Debate both sides at their strongest** — no one-sided narrative (P5)
- **Gates are non-negotiable** — Regime / Breadth / Sanity / Critical-News overrides (P6)
- **Fragility is a valuation input, not a disclaimer** (P10)
- **Log and preserve every source** — local copy mandatory (P11)
- **Check end-conditions** before leaving any phase (P12)
- **No lookahead** — event-window to the as-of date; post-cutoff events marked and excluded (P9)
- **Verbatim quotes only** — no paraphrased document claims without a quote; no fabricated quotes (P1, document-intelligence)
- **State confidence, conviction, and watchdog criteria** — honest views only (P7, P8)
- **Human disposes** — user makes the final call (P13)
- **Sanity-check script outputs** — units/currency assert before a number enters the note (Phase 4)
- **Check source freshness** — exclude stale price/valuation sources (Phase 5)
- **Reject single stocks** — the unit of analysis is a market/index; route single-stock requests to `stock-analysis` (Phase 1)