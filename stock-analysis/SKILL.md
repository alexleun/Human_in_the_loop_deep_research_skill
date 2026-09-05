---
name: stock-analysis
description: "A structured, deep-research workflow for analyzing stocks (optimized for Hong Kong / HKEX listings) using only free, public, no-API-key sources, producing a detailed report with an explicit BUY / HOLD / SELL recommendation and price target."
---

# Stock Analysis Skill

A structured, evidence-driven workflow for analyzing an individual stock — optimized for **Hong Kong / HKEX** listings (e.g. `1810.HK`), using **only free, public sources that require no API key**. Produces a **detailed written report** culminating in an explicit **BUY / HOLD / SELL** recommendation with a price target, confidence level, and falsification criteria.

**v1.1 changes:** Added explicit "STOP and ask" human-approval gates (Principle 8), mandatory fetch-and-save source preservation with an end-condition compliance check (Phase 2), a technical-data fallback clause (Phase 5), DCF sensitivity-before-compute and real-peer-table discipline (Phase 4), a multi-stock file layout, post-report lifecycle, phase-revisit triggers, and an explicit done-state checklist. Based on skill-evolution lessons from the 0066.HK and 1810.HK analysis runs (2026-09-04).

The final investment call always belongs to the **human**. This skill proposes, the user disposes.

---

## When to Use This Skill

- Analyzing a single listed company to reach a written BUY / HOLD / SELL view.
- Target is a **HKEX / SEHK** stock (though the flow generalizes to other exchanges).
- Data must come from **public, free sources** — no paid API key required.
- Output is a **detailed report + recommendation** (not a trading bot or live dashboard).

**Not for:** executing trades, backtesting strategies, or building a portfolio-management system.

---

## Core Principles

### 1. Public-Source Only (No API Keys)
All data must come from free, publicly accessible sources. If a normally useful source is paywalled/API-gated, substitute a free alternative and document it. Never fabricate data.

### 2. Grounding & Anti-Hallucination (P2 deep-research)
Every factual output must carry **exact quoted text** or a **source citation** (URL / source ID) and an **as-of date**. Distinguish **facts** (source-quoted), **claims** (attributed third-party views), and **inference** (your reasoning — labeled as such). Any zero-source number is stripped from the report.

### 3. Code-First Computation (P3 deep-research)
All ratios, growth rates, CAGRs, DCF, and scenario math are computed by **running Python** on the collected figures — never from LLM memory.

### 4. Blended Analysis (Fundamental + Technical + Catalysts + Risks)
A defensible BUY/HOLD/SELL requires:
- **Fundamentals** — quality, growth, profitability, financial health
- **Valuation** — price vs intrinsic worth and peers (fair-value range + price target)
- **Technicals** — trend, momentum, support/resistance (timing/risk context)
- **Catalysts & risks** — what could change the thesis, plus an explicit **falsification criterion**

### 5. Integrity of Recommendation
Give a clear rating with a price target, horizon, and **confidence level**. If data is thin or contradictory, say so — a transparent "HOLD, low confidence" beats a false, confident buy. Always end with a risk/disclaimer statement: this is research, not personalized investment advice.

### 6. Source Preservation (P20 deep-research)
Save a local copy of every source before extracting findings (`sources/…`), and index them in `sources_index.md`. Without local copies, findings are unrecoverable if URLs change.

### 7. End-Conditions Discipline (P15 deep-research)
Every phase defines explicit end conditions. The LLM exits a phase only when its end conditions are all true, and the human verifies at the decision gates.

### 8. Human-Approval Gates (explicit "STOP and ask")
- **Gate 1 (Phase 1 → 2):** STOP — present the proposed scope, horizon, and output contract; do NOT proceed to Phase 2 until the human confirms.
- **Gate 2 (Phase 7 → 8):** STOP — present the proposed recommendation (rating, target, confidence, thesis); do NOT proceed to Phase 8 until the human approves.
- **Gate 3 (Phase 8):** STOP — present the final report; do NOT mark the analysis complete until the human approves.
Gates are implemented as explicit "stop and ask" mechanisms, not conceptual checkpoints. The LLM proposes, the human disposes.

---

## Workflow Overview

```
Phase 1: Scope  ── define stock, exchange/code, horizon, output contract
   │  (human approval gate 1)
   ▼
Phase 2: Collect ── gather + preserve public sources (HKEXnews, reports, aggregators)
   │
   ▼
Phase 3: Fundamentals ── quality, growth, profitability, financial health
   │
   ▼
Phase 4: Valuation ── relative + DCF/dividend → fair value range + price target
   │
   ▼
Phase 5: Technicals ── trend, momentum, support/resistance
   │
   ▼
Phase 6: Catalysts & Risks ── upside catalysts, downside risks, falsification criteria
   │
   ▼
Phase 7: Synthesize & Decide ── BUY / HOLD / SELL + target + confidence
   │  (human approval gate 2)
   ▼
Phase 8: Report ── detailed written report + recommendation + disclaimer
   │  (human approval gate 3)
```

Phase revisiting is normal: a valuation surprise discovered in Phase 6 may send you back to Phase 3–4. Do not force a single pass.

**Phase revisiting triggers (proactive, not reactive):** When any of these fire, loop back to the referenced phase and update the affected computations before continuing:
- A new source or announcement changes a core financial input → revisit **Phase 2–3** and recompute the affected metrics.
- Phase 4 valuation output contradicts a Phase 3 growth assumption → revisit **Phase 3** and update growth before finalizing valuation.
- Phase 6 reveals a risk that changes a growth/valuation assumption → revisit **Phase 3–4** before Phase 7.
- A record the agent flags as uncertain in an earlier phase becomes critical later → revisit the source and its extraction.

Each revisit must be recorded in `task_state.json` (updated phases + reason) before moving on.

---

## Phase Router

**Before each phase, load its phase file with the `read` tool** — e.g. before Phase 4, read `04-valuation.md` and follow its procedure and end conditions. Do not work from this overview alone.

| Current Task | Load This File |
|---|---|
| Defining the stock, horizon, and output contract | `01-scope.md` |
| Collecting and preserving public sources | `02-collect.md` |
| Analyzing quality, growth, profitability, financial health | `03-fundamentals.md` |
| Valuing the stock and setting a price target | `04-valuation.md` |
| Reading trend, momentum, support/resistance | `05-technicals.md` |
| Identifying catalysts and risks | `06-catalysts-risks.md` |
| Reaching the BUY / HOLD / SELL decision | `07-synthesize.md` |
| Writing the final detailed report | `08-report.md` |

---

## Suggested File Layout

```
{project_root}/
├── stock-analysis-{code}/          # one suffixed dir per analysis (multi-stock support)
│   ├── task_state.json             # multi-session state (phase, progress, decisions)
│   ├── sources/
│   │   ├── sources_index.md        # every source: URL + local copy + access date
│   │   └── YYYY-MM-DD-<desc>.{html,pdf,md}   # local preserved copies (mandatory)
│   ├── data/                       # extracted figures / datasets
│   ├── notebooks/                  # Python computation scripts (fundamentals, valuation, technicals)
│   ├── report/
│   │   └── <Code>-<Company>-analysis.md   # final report
│   └── skill-evolution-log.md      # lessons learned (optional)
```

---

## HK-Specific Data Notes

- **Company announcements:** always cross-check the **HKEXnews** portal (`www1.hkexnews.hk`) — the authoritative, free filing source for HKEX-listed companies.
- **Reporting currency:** Hong Kong companies report in HKD unless stated otherwise; some (e.g. yuan- or USD-reporting) need a consistent-currency note when comparing.
- **Price sources:** free aggregators (Yahoo Finance HK, AAStocks, Investing.com) may differ slightly; pick one primary source and state it, and record "as of" timestamps.
- **Liquidity/halts:** HK stocks can have trading suspensions and the closing auction regime — note any halt that affects the technical picture.
- **Northbound/connectivity** (Stock Connect) and **HK/China policy** can be material catalysts and risks for HK listings — include in Phase 6.

---

## Post-Report Lifecycle

The analysis does not end at report approval. After Gate 3:

1. **Archive the OpenSpec change** (if the analysis ran inside one): `openspec archive <change-name> --yes`.
2. **Preserve the spec** for future diffing — the archived change keeps the baseline (scope, specs, design) for comparison.
3. **Set a review reminder date** (e.g. next quarterly results, or 3–6 months for the horizon) and record it in `task_state.json`.
4. **Start a review** with `openspec-new-change` using the same scope, and diff the new findings against the archived baseline. The report's falsification criteria and open questions tell you what to re-check.
5. **Update the skill-evolution log** with what worked / what caused problems for the next analysis.

## Completion Checklist ("Done" State)

The analysis is **complete** — nothing more to add — when ALL of the following are true:

1. ✅ Report written and saved at `report/<Code>-<Company>-analysis.md`
2. ✅ `task_state.json` updated with the final decision (rating, target, status)
3. ✅ Human has approved the final report (Gate 3)
4. ✅ OpenSpec change archived (if run inside one)
5. ✅ Review reminder date set
6. ✅ Skill evolution log updated (if applicable)

---

## Guardrails

- **Propose before deciding** — no BUY/HOLD/SELL without all prior phases complete
- **Log and preserve every source** — local copy mandatory (Principle 6)
- **Never invent data** — every number needs a citation and as-of date
- **Code, don't memorize** — compute metrics by script (Principle 3)
- **Distinguish facts/claims/inference** — and flag uncertainty (Principle 2)
- **State confidence and falsification criteria** — honest recommendations only (Principle 5)
- **Human disposes** — the user makes the final investment call (Principle 8)
- **Do not diagnose the timing infinitely** — technicals refine, the fundamental thesis leads for long horizons
