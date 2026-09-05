---
name: stock-analysis
description: "A merged deep-research + equity-research workflow for producing institutional-grade, evidence-first analysis of a SINGLE stock (optimal for HKEX / SEHK): public-only sources, code-first computation, DCF + reverse-DCF + SOTP valuation, adversarial Bull/Bear debate, a fragility audit, deterministic governance gates, a document-intelligence layer, and an explicit BUY / HOLD / SELL / AVOID / WATCH call with confidence, conviction, price target, and falsification criteria."
---

# Stock Analysis Skill (v2.0)

A **merged deep-research + equity-research** workflow for analyzing an **individual** listed company — optimized for **Hong Kong / HKEX** listings (e.g. `1810.HK`, `0700.HK`), using **only free, public, no-API-key sources**. Produces an **institutional-grade analyst note** culminating in an explicit **BUY / HOLD / SELL / AVOID / WATCH** recommendation with a **price target**, **confidence**, **conviction**, and **falsification criteria**.

**v2.0 changes (this is now the single canonical single-stock skill):** Absorbed the institutional methodology formerly kept in `stock-deep-research`: adversarial Bull/Bear debate (`06-debate.md`), fragility audit & red-team (`07-fragility-audit.md`), deterministic governance gates + 7-state rating (`08-synthesize.md`), Goldman-style analyst note (`09-report.md`), and the SOTP/reverse-DCF requirements. Added a documented document-intelligence layer (search protocol, coverage report, deep-read appraisals, evidence `#access/#evidence/#status` tags, `documents/findings-index.json`, event timeline). The `stock-deep-research` skill is now the **whole-market (index-level)** skill — see its README row.

**v1.1 changes (record):** Added explicit "STOP and ask" human-approval gates (Principle 13), mandatory fetch-and-save source preservation with an end-condition compliance check (Phase 2), a technical-data fallback clause (Phase 5), DCF sensitivity-before-compute and real-peer-table discipline (Phase 4), a multi-stock file layout, post-report lifecycle, phase-revisit triggers, and an explicit done-state checklist. Based on skill-evolution lessons from the 0066.HK and 1810.HK analysis runs (2026-09-04).

**v1.2 changes (record):** Added an environment probe (Phase 1); primary-filing PDF extraction fallback with logged substitution (Phase 2); earnings reconciliation + per-source reporting-currency discipline (Phase 3); a units/currency sanity gate, required reverse-DCF, forward-EPS dispersion check, and peer FX rule (Phase 4); a price-freshness check and standard price+MA+volume chart output (Phase 5); a numeric confidence-scoring rubric (Phase 8); timestamped report filenames + FX/artifacts references (Phase 9); a task-ticking discipline; and a layout sync (price-history CSV, `report/charts/`, mandatory evolution log). Based on the stock-analysis v1.1 run on 0992.HK (Lenovo, 2026-09-05).

The final investment call always belongs to the **human**. This skill proposes; the user disposes.

This skill adapts best-practice patterns from the public literature:

| Source (found via web research) | Pattern adopted |
|---|---|
| FinanceHarness (arXiv 2607.27853) | Layered finance tool surface; evidence-first; **pre/post-cutoff anti-lookahead** discipline |
| Agentic-Investing-Framework (GitHub) | **Bull/Bear adversarial debate**, DCF + **reverse-DCF**, Monte Carlo, verdict memo |
| DataPai Stock Intelligence | **Governance gates** (Quality, Regime, Sanity, Critical-News), multi-state rating, confidence + conviction |
| AdvancingTitans/stock-analysis | **Evidence-before-narrative**; Fact/Derived/Analysis taxonomy; action conditions |
| oierkid/quant-stock-analysis-valuation | **Narrative → fundamentals → SOTP valuation → fragility audit → analyst note** |
| Culture-research / deep-research skills (in-repo) | Document-intelligence layer: search protocol, coverage report, deep-read appraisals, evidence `#access/#evidence` tags, verbatim-quote rule |

---

## When to Use This Skill

- Reaching a written BUY/HOLD/SELL view on a **single** listed company, with the rigor of an equity research note.
- Target is a **HKEX / SEHK** stock (though the flow generalizes to US/CN/JP/KR).
- Data must come from **free, public sources** — no paid API key.
- Output is a **detailed research report + recommendation**, not a trading bot or live dashboard.

**Not for:** analyzing a whole market or index (use `stock-deep-research`), executing trades, portfolio rebalancing, backtesting strategies, or building a factor model.

---

## Core Principles

### P1. Evidence Before Narrative (anti-hallucination)
Narrative must be **translated into economics** and every factual output must carry an **exact quote** or **citation (URL / source ID) and an as-of date**. Use the **Fact / Derived-Fact / Analysis** taxonomy:
- **Fact** — directly supported by a cited or frozen source.
- **Derived fact** — calculated from supported inputs with an explicit formula and matching time boundary (e.g. market cap from price × shares).
- **Analysis** — interpretation, scenario, or valuation-model conclusion (labeled as such).

A model may complete an analysis chain; it may **never invent a missing fact**. Any zero-source number is stripped from the report.

### P2. Public-Source Only (No API Keys)
All data from free, public sources. If a source is paywalled/API-gated, substitute a free alternative and document it. **Never fabricate data.**

### P3. Code-First Computation
All ratios, CAGRs, DCF, reverse-DCF, SOTP, and scenario math are computed by **running Python** on collected figures — never from LLM memory. On Windows, prefix scripts with `sys.stdout.reconfigure(encoding='utf-8')` (try/except wrapped) to avoid cp950 console crashes.

### P4. Blended Analysis (Fundamental + Valuation + Technical + Debate)
A defensible call requires all of:
- **Fundamentals** — quality, growth, profitability, financial health
- **Valuation** — relative + intrinsic (fair-value range + price target), including DCF, reverse-DCF (what is the market pricing in?), and SOTP where the company has mixed-quality businesses
- **Technicals & regime** — trend, momentum, support/resistance, market regime
- **Adversarial debate** — the Bull and Bear cases argued at their strongest, plus catalysts and risks

### P5. Adversarial Bull/Bear Debate
Run the Bull and Bear cases **independently and at their strongest**. Do not let one side see the other's conclusion first. The synthesis weighs both strongest cases rather than a one-sided narrative. Hallucinations from one side get refuted by the other before reaching the final call.

### P6. Governance Gates (deterministic guardrails)
Before publishing a rating, run **rule-based, non-negotiable gates** that cannot be argued out of position:
- **Quality Gate** — refuse BUY on low-quality companies (no profitability, weak balance sheet).
- **Regime Gate** — if both technical and fundamental are bearish, demote BUY → HOLD.
- **Sanity Override** — if all input signals point one way but the call says the opposite, flag inconsistency and demote.
- **Critical-News Override** — CRITICAL negative event (fraud / bankruptcy / sanctions / major litigation) forces SELL/AVOID regardless of a cheap valuation.

### P7. Integrity of Recommendation
Give a **rating**, **price target**, **horizon**, **confidence (0–1)**, and **conviction (HIGH/MEDIUM/LOW)**. If data is thin or contradictory, say so. Distinguish **SELL** (hold the position to exit) from **AVOID** (material risk — do not engage). Use **WATCH** when conviction is low but no material risk. Always end with a risk/disclaimer statement: research, not personalized advice.

### P8. Falsification Discipline
Every thesis must carry an explicit **falsification criterion** and **action conditions** (monitoring signals that confirm/invalidate the view). If the criterion triggers, the recommendation is revisited immediately.

### P9. Anti-Lookahead / Point-in-Time Discipline
Distinguish **pre-cutoff evidence** (findable facts) from **post-cutoff reasoning** (outcome anticipation). Do not present future knowledge as if it were known at decision time. Never use data dated after the "as-of" decision date to justify the decision.

### P10. Fragility Audit (not just a disclaimer)
Treat fragility as a **valuation input**, not an appendix. Assess geographic/channel/customer concentration, policy dependence, litigation/IP exposure, supply-chain bottlenecks, inventory/warranty risk. Decide whether each risk warrants **disclosure only**, a **multiple haircut**, or a **scenario discount**.

### P11. Source Preservation (P20 deep-research)
Save a **local copy** of every source before extracting findings (`sources/…`, `documents/…`) and index them in `sources_index.md`. Without local copies, findings are unrecoverable if URLs change.

### P12. End-Conditions Discipline
Every phase defines **end conditions as a checklist**. The LLM exits a phase only when all end conditions are true, and the human verifies at gates.

### P13. Human-Approval Gates (explicit "STOP and ask")
- **Gate 1 (Phase 1 → 2):** STOP — present the proposed scope, horizon, investor profile, and output contract; do NOT proceed to Phase 2 until the human confirms.
- **Gate 2 (Phase 8 → 9):** STOP — present the proposed recommendation (rating, target, confidence, conviction, thesis) produced in Phase 8; do NOT proceed to the analyst note (Phase 9) until the human approves.
- **Gate 3 (Phase 9):** STOP — present the final analyst note; do NOT mark the analysis complete until the human accepts it.
Gates are implemented as explicit "stop and ask" mechanisms, not conceptual checkpoints. The LLM proposes, the human disposes.

---

## Workflow Overview

```
Phase 1: Scope ── stock, exchange/code, horizon, investor profile, output contract
   │  (human approval gate 1)
   ▼
Phase 2: Collect & Preserve ── public sources + document-intelligence intake (corpus, coverage report)
   │
   ▼
Phase 3: Fundamentals ── quality, growth, profitability, financial health + deep-read appraisals
   │
   ▼
Phase 4: Valuation ── relative + DCF + reverse-DCF + SOTP → fair value range + price target
   │
   ▼
Phase 5: Technical & Regime ── trend, momentum, support/resistance, market regime
   │
   ▼
Phase 6: Bull/Bear Debate & Catalysts ── adversarial cases, catalysts, risks, event timeline
   │
   ▼
Phase 7: Fragility Audit & Red-Team ── concentration, contested signals, anti-lookahead, counter-hypotheses
   │
   ▼
Phase 8: Synthesize & Govern ── governance gates → rating + target + confidence + conviction
   │  (human approval gate 2)
   ▼
Phase 9: Analyst Note ── narrative → fundamentals → valuation → fragility → conclusion + action conditions
   │  (human approval gate 3)
```

**Phase revisiting is normal.** A fragility surprise in Phase 7 may send you back to Phases 3–4. Do not force a single pass.

**Phase revisiting triggers (proactive, not reactive):** When any of these fire, loop back to the referenced phase and update the affected computations before continuing:
- A new source or announcement changes a core financial input → revisit **Phase 2–3** and recompute the affected metrics.
- Phase 4 valuation output contradicts a Phase 3 growth assumption → revisit **Phase 3** and update growth before finalizing valuation.
- Phase 6 reveals a risk that changes a growth/valuation assumption → revisit **Phase 3–4** before synthesis.
- Phase 7 fragility audit finds a concentration/anti-lookahead issue that invalidates an earlier input → revisit the affected phase.

Each revisit must be recorded in `task_state.json` (updated phases + reason) before moving on.

---

## Phase Router

**Before each phase, load its phase file with the `read` tool** — e.g. before Phase 4, read `04-valuation.md` and follow its procedure and end conditions. Do not work from this overview alone.

| Current Task | Load This File |
|---|---|
| Defining stock, horizon, investor profile, output contract | `01-scope.md` |
| Collecting and preserving public sources + document corpus | `02-collect.md` |
| Analyzing quality, growth, profitability, financial health | `03-fundamentals.md` |
| Valuing the stock (relative + DCF + reverse-DCF + SOTP) | `04-valuation.md` |
| Reading trend, momentum, regime, support/resistance | `05-technicals.md` |
| Running the Bull/Bear debate, catalysts and risks | `06-debate.md` |
| Auditing fragility, contested signals, anti-lookahead | `07-fragility-audit.md` |
| Synthesizing + running governance gates to rate the stock | `08-synthesize.md` |
| Writing the final analyst note with action conditions | `09-report.md` |

---

## Suggested File Layout

```
{project_root}/
├── stock-analysis-{code}/       # one suffixed dir per analysis (multi-stock support)
│   ├── task_state.json          # multi-session state (phase, progress, decisions, environment line)
│   ├── sources/
│   │   ├── sources_index.md     # every source: URL + local copy + access date + evidence_status/access tags
│   │   └── YYYY-MM-DD-<desc>.{html,pdf,md}   # preserved local copies (mandatory)
│   ├── documents/               # document-intelligence layer
│   │   ├── search-protocol.md   # written before searching (types, hierarchy, criteria)
│   │   ├── coverage-report.md   # honest gap flagging (never padded)
│   │   ├── candidate-list.md    # deduplicated candidate documents
│   │   ├── appraisals/          # {doc-id}.md deep-read appraisals (verbatim quotes)
│   │   ├── findings-index.json  # machine-readable finding index (id, source_doc, quote, tags)
│   │   └── event-timeline.md    # dated market/company events (anti-lookahead cut-off)
│   ├── data/                    # extracted figures / datasets
│   │   └── <code>-price-history-<asof>.csv    # daily price series (technical baseline)
│   ├── notebooks/               # Python computation scripts (fundamentals, valuation, technicals)
│   ├── debate/                  # bull.md, bear.md, judge_notes.md
│   ├── report/
│   │   ├── <Code>-<Company>-<YYYY-MM-DD>-analysis.md   # timestamped final report
│   │   └── charts/
│   │       └── <code>-price-<asof>.png                # price + MA + volume chart
│   └── skill-evolution-log.md   # lessons learned (mandatory)
```

## Task Ticking Discipline

Running inside an OpenSpec change, tick tasks **at the end of each phase**, not at archive time. When a phase's end conditions pass, mark its `- [ ]` rows complete in `tasks.md` before starting the next phase. A single end-of-run sweep hides where each phase actually finished.

---

## HK-Specific Data Notes

- **Company announcements:** always cross-check the **HKEXnews** portal (`www1.hkexnews.hk`) — the authoritative, free filing source for HKEX-listed companies.
- **Reporting currency:** HK companies report in HKD unless stated otherwise; some (yuan- or USD-reporting) need a consistent-currency note when comparing.
- **Price sources:** free aggregators (Yahoo Finance HK, AAStocks, Investing.com) may differ; pick one primary source, state it, and record "as of" timestamps.
- **Liquidity/halts:** HK stocks can have suspensions and a closing-auction regime — note any halt affecting the technical picture.
- **Northbound/connectivity** (Stock Connect) and HK/China policy can be material catalysts and risks — include them in the debate phase.

---

## Post-Report Lifecycle

The analysis does not end at note approval. After Gate 3:

1. **Archive the OpenSpec change** (if the analysis ran inside one): `openspec archive <change-name> --yes`.
2. **Preserve the spec** for future diffing — the archived change keeps the baseline (scope, specs, design) for comparison.
3. **Set a review reminder date** (e.g. next quarterly results, or 3–6 months for the horizon) and record it in `task_state.json`.
4. **Start a review** with `openspec-new-change` using the same scope, and diff the new findings against the archived baseline. The note's action conditions and falsification criteria tell you what to re-check.
5. **Update the skill-evolution log** with what worked / what caused problems for the next analysis.

## Completion Checklist ("Done" State)

The analysis is **complete** — nothing more to add — when ALL of the following are true:

1. ✅ Analyst note written and saved at a timestamped path `report/<Code>-<Company>-<YYYY-MM-DD>-analysis.md`
2. ✅ `task_state.json` updated with the final decision (rating, target, confidence score, status)
3. ✅ Human has approved the final note (Gate 3)
4. ✅ OpenSpec change archived (if run inside one), with tasks.md fully ticked
5. ✅ Review reminder date set
6. ✅ Skill evolution log updated (mandatory)

---

## Guardrails

- **Evidence before narrative** — every number needs a citation and as-of date (P1)
- **Propose before deciding** — no rating without all prior phases complete (P13)
- **Code, don't memorize** — compute metrics by script (P3)
- **Debate both sides at their strongest** — no one-sided narrative (P5)
- **Gates are non-negotiable** — Quality / Regime / Sanity / Critical-News overrides (P6)
- **Fragility is a valuation input, not a disclaimer** (P10)
- **Log and preserve every source** — local copy mandatory (P11)
- **Check end-conditions** before leaving any phase (P12)
- **No lookahead** — pre-cutoff facts vs post-cutoff reasoning (P9)
- **Verbatim quotes only** — no paraphrased findings without a quote; no fabricated quotes (P1, document-intelligence)
- **State confidence, conviction, and falsification criteria** — honest ratings only (P7, P8)
- **Human disposes** — user makes the final call (P13)
- **Sanity-check script outputs** — units/currency assert before a number enters the note (Phase 4)
- **Reconcile earnings** — never carry a reported-vs-segment-vs-adjusted contradiction silently (Phase 3)
- **Check source freshness** — exclude stale price sources (Phase 5)