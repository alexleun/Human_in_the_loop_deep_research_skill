---
name: stock-deep-research
description: "A fused deep-research + stock-analysis workflow for producing institutional-grade, evidence-first equity research on a single stock (optimal for HKEX / SEHK). Combines public-only sources, code-first computation, adversarial Bull/Bear debate, DCF + reverse-DCF + SOTP valuation, a fragility audit, deterministic governance gates, and an explicit BUY / HOLD / SELL / AVOID / WATCH call with confidence, conviction, price target, and falsification criteria."
---

# Stock Deep-Research Skill (v1.0)

A **merged deep-research + equity-research** workflow for analyzing a single listed company — optimized for **Hong Kong / HKEX** listings (e.g. `1810.HK`, `0700.HK`), using **only free, public, no-API-key sources**. Produces an **institutional-grade analyst note** culminating in an explicit **BUY / HOLD / SELL / AVOID / WATCH** recommendation with a **price target**, **confidence**, **conviction**, and **falsification criteria**.

The final investment call always belongs to the **human**. This skill proposes; the user disposes.

This skill fuses two prior skills in this repository (`stock-analysis` and `deep-research`) and adapts best-practice patterns from the public literature:

| Source (found via web research) | Pattern adopted |
|---|---|
| FinanceHarness (arXiv 2607.27853) | Layered finance tool surface; evidence-first; **pre/post-cutoff anti-lookahead** discipline |
| Agentic-Investing-Framework (GitHub) | **Bull/Bear adversarial debate**, DCF + **reverse-DCF**, Monte Carlo, verdict memo |
| DataPai Stock Intelligence | **Governance gates** (Quality, Regime, Sanity, Critical-News), 7-state rating, confidence + conviction, reflector learning |
| AdvancingTitans/stock-analysis | **Evidence-before-narrative**; Fact/Derived/Analysis taxonomy; Quick/Standard/Deep; action conditions |
| oierkid/quant-stock-analysis-valuation | **Narrative → fundamentals → SOTP valuation → fragility audit → analyst note** |
| AQuA / AutoScientist-Quant | **Validated evidence**, anti-lookahead, sealed decomposition, robustness |

---

## When to Use This Skill

- Reaching a written BUY/HOLD/SELL view on a **single** listed company, with the rigor of an equity research note.
- Target is a **HKEX / SEHK** stock (though the flow generalizes to US/CN/JP/KR).
- Data must come from **free, public sources** — no paid API key.
- Output is a **detailed research report + recommendation**, not a trading bot or live dashboard.

**Not for:** executing trades, portfolio rebalancing, backtesting strategies, or building a factor model.

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
Give a **rating**, **price target**, **horizon**, **confidence** (0–1), and **conviction** (HIGH/MEDIUM/LOW). If data is thin or contradictory, say so. Distinguish **SELL** (hold the position to exit) from **AVOID** (material risk — do not engage). Use **WATCH** when conviction is low but no material risk. Always end with a risk/disclaimer statement: research, not personalized advice.

### P8. Falsification Discipline
Every thesis must carry an explicit **falsification criterion** and **action conditions** (monitoring signals that confirm/invalidate the view). If the criterion triggers, the recommendation is revisited immediately.

### P9. Anti-Lookahead / Point-in-Time Discipline
Distinguish **pre-cutoff evidence** (findable facts) from **post-cutoff reasoning** (outcome anticipation). Do not present future knowledge as if it were known at decision time. Never use data dated after the "as-of" decision date to justify the decision.

### P10. Fragility Audit (not just a disclaimer)
Treat fragility as a **valuation input**, not an appendix. Assess geographic/channel/customer concentration, policy dependence, litigation/IP exposure, supply-chain bottlenecks, inventory/warranty risk. Decide whether each risk warrants **disclosure only**, a **multiple haircut**, or a **scenario discount**.

### P11. Source Preservation (P20 deep-research)
Save a **local copy** of every source before extracting findings (`sources/…`) and index them in `sources_index.md`. Without local copies, findings are unrecoverable if URLs change.

### P12. End-Conditions Discipline
Every phase defines **end conditions as a checklist**. The LLM exits a phase only when all end conditions are true, and the human verifies at gates.

### P13. Human-Approval Gates
- **Phase 1 → 2:** human confirms scope, horizon, and output contract.
- **Phase 8 → 9:** human reviews the proposed recommendation (produced in Phase 8 Synthesize & Govern) before the final analyst note is finalized.
- **Phase 9:** human approves the final analyst note.
The LLM proposes, the human disposes.

---

## Workflow Overview

```
Phase 1: Scope ── stock, exchange/code, horizon, investor profile, output contract
   │  (human approval gate 1)
   ▼
Phase 2: Collect & Preserve ── public sources (HKEXnews, reports, aggregators) + local copies
   │
   ▼
Phase 3: Fundamentals ── quality, growth, profitability, financial health
   │
   ▼
Phase 4: Valuation ── relative + DCF + reverse-DCF + SOTP → fair value range + price target
   │
   ▼
Phase 5: Technical & Regime ── trend, momentum, support/resistance, market regime
   │
   ▼
Phase 6: Bull/Bear Debate & Catalysts ── adversarial cases, catalysts, risks
   │
   ▼
Phase 7: Fragility Audit & Red-Team ── concentration, anti-lookahead, counter-hypotheses
   │
   ▼
Phase 8: Synthesize & Govern ── governance gates → rating + target + confidence + conviction
   │  (human approval gate 2)
   ▼
Phase 9: Analyst Note ── narrative → fundamentals → valuation → fragility → conclusion + action conditions
   │  (human approval gate 3)
```

**Phase revisiting is normal.** A fragility surprise in Phase 7 may send you back to Phases 3–4. Do not force a single pass.

---

## Phase Router

| Current Task | Load This File |
|---|---|
| Defining stock, horizon, investor profile, output contract | `01-scope.md` |
| Collecting and preserving public sources | `02-collect.md` |
| Analyzing quality, growth, profitability, financial health | `03-fundamentals.md` |
| Valuing the stock (relative + DCF + reverse-DCF + SOTP) | `04-valuation.md` |
| Reading trend, momentum, regime, support/resistance | `05-technicals.md` |
| Running the Bull/Bear debate, catalysts and risks | `06-debate.md` |
| Auditing fragility, anti-lookahead, counter-hypotheses | `07-fragility-audit.md` |
| Synthesizing + running governance gates to rate the stock | `08-synthesize.md` |
| Writing the final analyst note with action conditions | `09-report.md` |

---

## Suggested File Layout

```
{project_root}/
├── stock-deep-research/
│   ├── task_state.json          # multi-session state (phase, progress)
│   ├── sources/
│   │   ├── sources_index.md     # every source: URL + local copy + access date
│   │   └── YYYY-MM-DD-<desc>.{html,pdf,md}   # preserved local copies
│   ├── data/                    # extracted figures / datasets
│   ├── notebooks/               # Python computation scripts (DCF, reverse-DCF, SOTP)
│   ├── debate/                  # bull.md, bear.md, judge_notes.md
│   ├── report/
│   │   └── <Code>-<Company>-analyst-note.md   # final deliverable
│   └── skill-evolution-log.md   # lessons learned (optional)
```

---

## HK-Specific Data Notes

- **Company announcements:** always cross-check the **HKEXnews** portal (`www1.hkexnews.hk`) — the authoritative, free filing source for HKEX-listed companies.
- **Reporting currency:** HK companies report in HKD unless stated otherwise; some (yuan- or USD-reporting) need a consistent-currency note when comparing.
- **Price sources:** free aggregators (Yahoo Finance HK, AAStocks, Investing.com) may differ; pick one primary source, state it, and record "as of" timestamps.
- **Liquidity/halts:** HK stocks can have suspensions and a closing-auction regime — note any halt affecting the technical picture.
- **Northbound/connectivity** (Stock Connect) and HK/China policy can be material catalysts and risks — include them in the debate phase.

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
- **State confidence, conviction, and falsification criteria** — honest ratings only (P7, P8)
- **Human disposes** — user makes the final call (P13)
