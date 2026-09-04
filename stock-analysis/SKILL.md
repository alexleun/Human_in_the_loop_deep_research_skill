---
name: stock-analysis
description: "A structured, deep-research workflow for analyzing stocks (optimized for Hong Kong / HKEX listings) using only free, public, no-API-key sources, producing a detailed report with an explicit BUY / HOLD / SELL recommendation and price target."
---

# Stock Analysis Skill

A structured, evidence-driven workflow for analyzing an individual stock — optimized for **Hong Kong / HKEX** listings (e.g. `1810.HK`), using **only free, public sources that require no API key**. Produces a **detailed written report** culminating in an explicit **BUY / HOLD / SELL** recommendation with a price target, confidence level, and falsification criteria.

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

### 8. Human-Approval Gates
- **Phase 1 → 2:** human confirms scope/horizon/output contract
- **Phase 7 → 8:** human reviews the proposed recommendation before the final report is finalized
- **Phase 8:** human approves the final report
The LLM proposes, the human disposes.

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

---

## Phase Router

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
├── stock-analysis/
│   ├── task_state.json          # multi-session state (phase, progress)
│   ├── sources/
│   │   ├── sources_index.md     # every source: URL + local copy + access date
│   │   └── YYYY-MM-DD-<desc>.{html,pdf,md}   # local preserved copies
│   ├── data/                    # extracted figures / datasets
│   ├── notebooks/               # Python computation scripts
│   ├── report/
│   │   └── <Code>-<Company>-analysis.md   # final report
│   └── skill-evolution-log.md   # lessons learned (optional)
```

---

## HK-Specific Data Notes

- **Company announcements:** always cross-check the **HKEXnews** portal (`www1.hkexnews.hk`) — the authoritative, free filing source for HKEX-listed companies.
- **Reporting currency:** Hong Kong companies report in HKD unless stated otherwise; some (e.g. yuan- or USD-reporting) need a consistent-currency note when comparing.
- **Price sources:** free aggregators (Yahoo Finance HK, AAStocks, Investing.com) may differ slightly; pick one primary source and state it, and record "as of" timestamps.
- **Liquidity/halts:** HK stocks can have trading suspensions and the closing auction regime — note any halt that affects the technical picture.
- **Northbound/connectivity** (Stock Connect) and **HK/China policy** can be material catalysts and risks for HK listings — include in Phase 6.

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
