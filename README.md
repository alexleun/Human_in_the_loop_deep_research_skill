# Human-in-the-Loop Research Skills

A collection of structured, artifact-driven AI research skills for **OpenCode** environments. Every skill in this repository is built around a single principle: **the human stays in the loop, learns alongside the AI, and never receives a finished black box.**

This repository currently ships five skills:

| Skill | Folder | Version | Best for |
|---|---|---|---|
| **deep-research** | `deep-research/` | v2.3 | Topic-agnostic, quantitative + qualitative research with code-first analysis, Jupyter notebooks, and bilingual or single-language website output |
| **culture-research** | `culture-research/` | v3.3 | Cultural / behavioral one-off studies: paper collection, deep reading, knowledge graph, multi-round qualitative analysis, Obsidian vault |
| **frontier-research** | `frontier-research/` | v1.0 | Engineering / science / frontier-tech research: systems mapping, epistemic stress-tested evidence, generative + convergent synthesis, discovery-first technical report |
| **stock-analysis** | `stock-analysis/` | v1.1 | Single-stock analysis (HKEX-optimized) using public-only, no-API-key sources: fundamentals + valuation + technicals + catalysts/risks, ending in a written BUY / HOLD / SELL report |
| **stock-deep-research** | `stock-deep-research/` | v1.1 | Institutional-grade single-stock equity research: fuses stock-analysis + deep-research — evidence-first, code-first, adversarial Bull/Bear debate, DCF + reverse-DCF + SOTP, fragility audit, deterministic governance gates, and a BUY / HOLD / SELL / AVOID / WATCH call |

---

## 🧠 The Philosophy: Co-Learning over Blind Automation

In a world where commercial tools (like OpenAI Deep Research or Perplexity Pro) try to automate everything away, humans are left in the dark. 
* **The Problem with Black Boxes:** If an AI does 100% of the work in secret and just hands you a finished file, **the human learns nothing.** A static report cannot help an independent developer truly understand how to build or evolve their project. 
* **The Solution (Co-Learning):** This skill treats research as a collaborative partnership. By forcing human-gated checkpoints, you are forced to review the data, analyze the gaps, and think critically. **As the AI conducts research, you develop your own skills alongside it.**

---

## 🧠 The Philosophy: Human Responsibility in the Age of Autonomous Agents

It is 2026, and the industry trend is hyper-focused on "Agent AI"—building fully autonomous, zero-human-in-the-loop systems designed to replace human workflows entirely. While this level of automation works for repetitive tasks, **deep research cannot and should not be fully outsourced to a black box.**

* **The Accountability Gap:** Autonomous agents can search, calculate, and compile, but they cannot hold responsibility. If an AI generates a flawed analysis, the AI suffers zero consequences. **The final accountability and liability always rest on the human developer.**
* **The Problem with Black Boxes:** If an AI does 100% of the work in secret and hands you a finished file, **the human learns nothing.** When human jobs and skills disappear behind automated screens, we stop growing. A static report cannot teach an independent developer how to truly lead their project.
* **The Solution (Co-Learning & Oversight):** This skill explicitly rejects the "zero-human" hype. It treats research as an augmented partnership. By forcing human-gated checkpoints, you retain absolute strategic control. You review the data, track the calculations in open Jupyter Notebooks, and **develop your own expertise alongside the machine.**

---

## 🔄 The Human-in-the-Loop Is Always Yours to Control

These skills halt at gated checkpoints by design — but you are never locked in. At **any point** during a research session, you can:

* **Suspend** a sub-session and inspect its batch notes
* **Add comments** or redirect the agent mid-phase
* **Modify** the process, schema, or artifacts before the next step
* **Override** findings, adjust scope, or change direction
* **Do nothing** and accept — that is also a valid decision

The loop is yours. The AI proposes; you dispose. Whether you actively steer every phase or passively approve all suggestions, the choice is always in your hands.

---

## 📦 What's New — Upgrades from Real Research

The existing skills were upgraded after being used in production research. culture-research v3.2 incorporates lessons from a 38-paper, 3-region pain-and-culture study including a failed-first-draft report-writing cycle that drove the Discovery-First Framing principle. culture-research v3.3 adds an **Epistemic Stress-Test & Systems Mapping phase** that destructively verifies evidence before synthesis. deep-research v2.1 absorbed methodological discipline from the same lineage. deep-research v2.2 incorporates quantitative project lessons from a 202-day Hong Kong passenger statistics analysis (5M+ records, Traditional Chinese only), adding Windows encoding resilience, existing-data shortcuts, CJK font verification, and optional Discovery-First Framing cross-pollinated from culture-research v3.2. deep-research v2.3 adapts the Epistemic Stress-Test into its Phase 7 Review with a code-first systems-mapping approach. Two v1.0 skills extend this lineage to equity research: **stock-analysis** (a focused 8-phase single-stock BUY / HOLD / SELL workflow on public-only sources) and **stock-deep-research** (an institutional-grade 9-phase note that fuses stock-analysis + deep-research, adding adversarial Bull/Bear debate, DCF + reverse-DCF + SOTP, a fragility audit, and deterministic governance gates). In v1.1 (2026-09-04) both stock skills were refined from two live HKEX runs (0066.HK, 1810.HK): hard **"STOP and ask" human-approval gates**, mandatory **fetch-and-save source preservation** with end-condition compliance checks, a **technical-data fallback clause**, **DCF sensitivity-before-compute** (no post-hoc re-tuning) and **real-peer-table** valuation, multi-stock file layouts, post-report lifecycle, phase-revisit triggers, and explicit done-state checklists.

### culture-research v3.2 Highlights (v3.0 → v3.1 → v3.2)

#### v3.0 Foundation
| Feature | What It Does |
|---|---|
| **Science Communication Phase** (`09-report-writing.md`) | Generates a science magazine article, research brief, executive summary, and slide deck from the synthesis — with style calibration, sub-agent chapter writing, and HTML export |
| **Dual Evidence Model** | Every finding is tagged with `#evidence/{level}` **and** `#access/{type}` (full-text, abstract-only, metadata-only). Downstream analysis uses both fields — no more indistinguishable findings. |
| **Findings Index** (`findings-index.json`) | Machine-readable index alongside markdown entity files. Analysis rounds use this instead of re-reading 92+ finding files manually. |
| **Cross-Appraisal Consistency** | `papers/appraisals/_cross-appraisal-check.md` must exist before deep-read phase is complete — a 5-point checklist prevents skipped validation. |
| **Director Observations** | Every sub-session batch note includes a Director Observations section — aggregated methodology patterns tracked and fed back into the skill. |
| **File Truncation Safeguard** | Every file read checks for the 50KB cap. Critical end-of-file content (data tables, references) is no longer silently missed. |
| **Windows Encoding & Non-ASCII** | `ï`, `é`, `ü` in filenames and CJK content no longer cause inaccessible files. |
| **Sub-Theme Derivation Procedure** | Round 1 uses a 3-step inductive procedure with granularity rules (4-8 per domain). |
| **Contradiction Identification Algorithm** | Round 3 replaced vague "find contradictions" with a deterministic matrix-scan → direction flag → entity verification pipeline. |
| **3-Tier Speculation Classification** | Checkpoint distinguishes evidence-derived, gap-derived, and speculative claims (replaces binary). |
| **state.json Synchronization** | Sub-sessions read `project-state.json` for current deliverable paths instead of trusting static prompt descriptions. |

#### v3.1 Additions
| Feature | What It Does |
|---|---|
| **Source Preservation** | Fetching any paper content requires saving a local copy (`papers/raw/`) before extraction — findings remain verifiable after URLs go offline. |
| **Sub-Session Execution Modes** | Two formal modes: human-executed (prompt written to disk, human launches) vs LLM-executed (agent launches via task tool). Decision tree included. |
| **PM Review Loop** | After each sub-session, PM reads batch note, spot-checks output, updates state, logs PROCEED/LOOP/PAUSE decision. Prevents undetected quality drift. |
| **Scale-Dependent MCP Guidance** | < 50 entities → MCP tools, 50–500 → write files + JSON, 500+ → add batch-import script. Prevents tool-bottleneck on large knowledge bases. |
| **Generational / Time-Period Dimension** | Optional `time_period` field on `cultural_context` entities; `#generation/{cohort}` tag taxonomy. Enables cross-generational comparison. |

#### v3.2 Additions
| Feature | What It Does |
|---|---|
| **Discovery-First Framing** | Report-writing outputs must lead with claims about the world, not the research process. Methodology relegated to a single endnote. Prevents the "reads as a lit review" failure mode. |
| **Human-Approval Gates** | Formal gates after Explore (question), Checkpoint (verdict), Synthesis (document), and Report Writing (section plan) require explicit human sign-off before proceeding. |
| **Pre-Writing Section Plan Gate** | Before drafting any chapter, the human must approve a section plan (titles, narrative arc, key claims). Catches misaligned voice before it propagates. |
| **Style Calibration Heuristics** | Concrete, checkable style profiles for Aeon, The Atlantic, Sapiens, and Nature News — sentence length, paragraph structure, opening patterns, citation style. |
| **Variable-Length Planning** | Long-form articles (5,000–10,000 words) use a density planning table (tight 200-word sections to expansive 1,000-word sections) instead of the fixed 400-500 word template. |
| **Unfindable Paper Protocol** | 5-minute timebox per unfindable paper; minimal appraisal with `no-abstract-available`; no replacement. Prevents time sinks while maintaining honest coverage. |
| **Project Sizing Guide** | Small (5 SS, 1–2 regions), Medium (13–15 SS, 3–4 regions, recommended), Large (18–22 SS, 5–6 regions), Exhaustive (25+ SS). Replaces the fixed 15-SS sequence. |
| **Calibration Run for Analysis Rounds** | Test Round 1 on one domain, Round 2 on 2–3 rows, Round 3 on 1–2 cells before scaling. Prevents format drift across large outputs. |

### culture-research v3.3 Highlights (Phase 5: Epistemic Stress-Test & Systems Mapping)

| Feature | What It Does |
|---|---|
| **New Phase 5: Epistemic Stress-Test** (`05-epistemic-stress-test.md`) | A destructive verification pass inserted between the Knowledge Base (Phase 4) and Multi-Round Analysis (now Phase 6). Replaces the old Phase 2.5 proposal after SHUFFLE resolved the matrix structure. |
| **Axiomatic Audit** | Rechecks whether every extracted finding is actually grounded in evidence, mediated, contextualized, or speculative — and tags each finding accordingly. |
| **Steelman Red Team** | Systematically challenges the most convenient or tentative conclusions to detect AI hallucination, confirmation bias, and premature convergence. |
| **Causal Loops & Systems Mapping** | Builds a causal-loop diagram highlighting feedback loops, leverage points, and systemic blindspots — adding an emergence lens beyond linear cause-and-effect. |
| **Cognitive Complexity Score (CCS)** | `CCS = min(10, Contradiction_Density×3.5 + Chain_Length×0.3 + Loop_Count×0.8)`. Routes to Mode A (automated audit, CCS<6 or `--mode=auto`) or Mode B (Strategic HITL with 2–3 forks, CCS≥6 and interactive). |
| **`stress-tested-matrix.json`** | Phase 5 output — the authoritative Reduce input. Phase 6 and Phase 8 MUST NOT cite claims flagged `Unsubstantiated_Speculation`. |
| **Renumbered phases 5–9 → 6–10** | Phase 5 inserted shifts Multi-Round Analysis→6, Checkpoint→7, Synthesis→8, Sub-Session Orchestration→9, Report Writing→10. |
| **`epistemic_status` field** | Optional per-finding field (`Verified_Axiom` / `Inferred_Bridge` / `Unsubstantiated_Speculation`) in `findings-index.json`, set by Phase 5, orthogonal to access/evidence tags. |

### frontier-research v1.0 Highlights (New)

| Feature | What It Does |
|---|---|
| **10-Phase Engineering Protocol** | `01-system-map → 02-harvest → 03-epistemic-ledger → 04-red-team → 05-epistemic-stress-test → 06-generative-synthesis → 07-calibration → 08-deep-convergence → 09-report-drafting → 10-self-audit`. A dedicated **stress-test gate** and a **user-calibration gate** sit before any convergent synthesis. |
| **Three Core Mental Frameworks** | Systems Thinking (causal loops, stocks & flows, feedback), Critical Thinking & Anti-Bias (premise verification, red-teaming, steel-manning), Epistemic First Principles & Triangulation (labeling, physical/mathematical consistency, ≥2 independent sources). |
| **Reused Epistemic Stress-Test Gate (Phase 5)** | Reuses the culture-research v3.3 methodology (Axiomatic Audit, Steelman Red Team, Causal Loops & Systems Mapping, CCS routing) rather than redefining it — keeping the two skills' methodology aligned. Emits `evidence/05-stress-tested-matrix.json`. |
| **Mid-Term Calibration Gate (Phase 7)** | Presents the systems map, red-team findings, stress-tested matrix, and innovation hypotheses to the user and folds budget / timeline / technical preference into `project-state.json → user_constraints` before convergence. |
| **Anti-Hallucination Guardrails** | Calculations First, Citation Requirement (every metric carries a source + epistemic tag), and Uncertainty Quantification (`[DATA DEFICIT: Requires Empirical Testing]`) enforced cross-session. |
| **Epistemic Ledger State** | `epistemic_ledger` in `project-state.json` tracks `verified_facts` / `unverified_claims` / `falsified_hypotheses` for honest multi-session resume. |

### stock-analysis v1.1 Highlights (New)

An 8-phase single-stock workflow, HKEX-optimized, public-only sources, no API key:

| Feature | What It Does |
|---|---|
| **Blended Analysis (8 phases)** | `01-scope → 02-collect → 03-fundamentals → 04-valuation → 05-technicals → 06-catalysts-risks → 07-synthesize → 08-report`. A defensible call needs fundamentals + valuation + technicals + catalysts/risks, not any one in isolation. |
| **Public-Source Only** | Free, public, no-API-key data (HKEXnews, reports, free aggregators) — never fabricate data; substitute a documented free alternative if a source is paywalled. |
| **Grounding & Anti-Hallucination** | Every factual output carries exact quoted text or a citation (URL / source ID) plus an as-of date; facts vs claims vs inference are distinguished (adopts deep-research P2). |
| **Code-First Computation** | All ratios, growth rates, CAGRs, DCF, and scenario math run in Python — never from LLM memory (adopts deep-research P3). |
| **Explicit Recommendation** | Ends in a written BUY / HOLD / SELL with a price target, horizon, confidence level, falsification criteria, and a disclaimer. |
| **Human-Approval Gates** | Gates after Scope (contract), before finalizing the report (recommendation review), and at report approval — the human makes the final investment call. |
| **HK-Specific Data Notes** | HKEXnews cross-checking, HKD reporting-currency notes, price-aggregator alignment, trading halts / closing auction, and Stock Connect / policy catalysts built into Phase 6. |

### stock-deep-research v1.1 Highlights (New)

An institutional-grade 9-phase equity-research workflow, **fusing stock-analysis + deep-research**:

| Feature | What It Does |
|---|---|
| **Evidence-First Analyst Note (9 phases)** | `01-scope → 02-collect → 03-fundamentals → 04-valuation → 05-technicals → 06-debate → 07-fragility-audit → 08-synthesize → 09-report`. Narrative is translated into economics; every number cited and dated. |
| **Fact / Derived-Fact / Analysis Taxonomy** | Facts are cited, derived facts are computed from supported inputs with an explicit formula, analysis is labeled as interpretation — a model may complete an analysis chain but never invent a missing fact. |
| **Adversarial Bull/Bear Debate (Phase 6)** | Bull and Bear argued independently and at their strongest before any synthesis; hallucinations from one side get refuted by the other before the call. |
| **Multi-Method Valuation (Phase 4)** | Relative + DCF + **reverse-DCF** (what is the market pricing in?) + **SOTP** for mixed-quality businesses → fair-value range + price target. |
| **Fragility Audit (Phase 7)** | Fragility treated as a **valuation input**, not an appendix — concentration, policy, litigation, supply-chain, inventory risk each get disclosure / multiple haircut / scenario discount. |
| **Deterministic Governance Gates (Phase 8)** | Rule-based Quality / Regime / Sanity / Critical-News gates that cannot be argued out of position before a rating is published. |
| **Anti-Lookahead / Point-in-Time Discipline** | Pre-cutoff facts vs post-cutoff reasoning are separated; a decision is never justified with data dated after the as-of date. |
| **Explicit Rating + Conviction** | BUY / HOLD / SELL / **AVOID** / **WATCH** with price target, confidence (0–1), conviction (HIGH/MEDIUM/LOW), falsification criteria, and action conditions. |
| **State & Templates** | Ships a `template-task_state.json` skeleton (skill, current_phase, per-phase status, decision date, horizon, rating, price target) for honest multi-session resume. |

### deep-research v2.x Highlights

| Feature | What It Does |
|---|---|
| **End-Conditions Discipline** | Every phase has an explicit completion checklist. No more "I think it's done" — verifiable criteria for all 10 phases. |
| **Cross-Phase Gates** | 7 formal verification gates between phases: source verification, data validation, code validation, encoding check, parity check, HTML structure, cross-artifact consistency. |
| **File Truncation Safeguard** | After every file read, check for the 50KB cap. Critical EOF content is no longer missed. |
| **Non-ASCII Filename Handling** | Source filenames with `é`, `ü`, `ñ`, `ç`, CJK characters handled via `_filename_map.json`. |
| **State Synchronization** | `task_state.json` promoted from optional to recommended. Every phase end-condition includes a state update step. |
| **Skill Evolution Log** | Post-archive step produces `skill-evolution-log.md` entries — each completed change feeds back into skill improvement. |

#### v2.2 Additions
| Feature | What It Does |
|---|---|
| **Windows stdout Encoding** | `sys.stdout.reconfigure(encoding='utf-8')` guidance added to Principle 6 — prevents `print()` crashes on cp950 Windows consoles with CJK/Unicode output. |
| **Existing-Data Shortcut** | Phase 3 now documents that when data pre-exists, skip fetch and go directly to validation + pipeline setup. |
| **CJK Font Verification** | New pre-render font check in Phase 4: verifies CJK font availability before batch figure generation, prevents silent tofu-box rendering. |
| **Discovery-First Framing (optional)** | Phase 5 adds optional narrative-style report mode cross-pollinated from culture-research v3.2 — methodology in endnote only, opening hook required. |
| **Dashboard-First Iteration** | Phase 8 recommends updating interactive dashboards over full report regeneration for data-heavy projects. |
| **Single-Language Gate Support** | Parity Check gate made optional — annotated "(skip for single-language projects)" in cross-phase gates table. |

---

## 📦 Repository Structure

```
.
├── deep-research/        # Core deep-research skill (v2.3)
│   ├── SKILL.md
│   ├── 01-explore.md … 10-implement.md
│   └── state-management.md
├── culture-research/     # Cultural / qualitative research skill (v3.3)
│   ├── SKILL.md
│   ├── 01-explore.md … 10-report-writing.md
│   ├── 05-epistemic-stress-test.md (v3.3, new)
│   └── 09-sub-session-orchestration.md (v3.3 update)
├── frontier-research/    # Engineering / science / frontier-tech skill (v1.0)
│   ├── SKILL.md
│   ├── 01-system-map.md … 10-self-audit.md
│   ├── 05-epistemic-stress-test.md (reuses shared v3.3 methodology)
│   └── state-management.md
├── stock-analysis/       # Single-stock analysis, HKEX-optimized (v1.1)
│   ├── SKILL.md
│   ├── 01-scope.md … 08-report.md
│   └── template-task_state.json
├── stock-deep-research/  # Institutional-grade equity research, fuses stock-analysis + deep-research (v1.1)
│   ├── SKILL.md
│   ├── 01-scope.md … 09-report.md
│   ├── 06-debate.md (Bull/Bear), 07-fragility-audit.md (epistemic stress-test)
│   └── template-task_state.json
└── README.md
```

Each `SKILL.md` is the entry point; numbered `.md` files are phase-specific instructions the agent loads on demand.

---

## ✅ Prerequisites

1. **OpenCode** — the agent runtime. Initialize your local OpenCode environment first.

---

## 🚀 Quick Start

### Step 1 — Copy the skills into your OpenCode skills folder

**Windows (cmd/PowerShell)**

```powershell
Copy-Item -Recurse ".\deep-research" ".opencode\skills\deep-research"
Copy-Item -Recurse ".\culture-research" ".opencode\skills\culture-research"
Copy-Item -Recurse ".\frontier-research" ".opencode\skills\frontier-research"
Copy-Item -Recurse ".\stock-analysis" ".opencode\skills\stock-analysis"
Copy-Item -Recurse ".\stock-deep-research" ".opencode\skills\stock-deep-research"
```

**macOS / Linux (bash)**

```bash
cp -R ./deep-research        .opencode/skills/deep-research
cp -R ./culture-research     .opencode/skills/culture-research
cp -R ./frontier-research    .opencode/skills/frontier-research
cp -R ./stock-analysis       .opencode/skills/stock-analysis
cp -R ./stock-deep-research  .opencode/skills/stock-deep-research
```

### Step 2 — Trigger the skill from a prompt

**Example — culture research**

```text
analysis topic "study human daily behavior",
using skill .opencode\skills\culture-research
```

**Example — deep research**

```text
analysis topic "compare 10 open-source vector databases for production use",
using skill .opencode\skills\deep-research
```

**Example — stock analysis**

```text
analysis topic "analyze Tencent (0700.HK) and give a BUY/HOLD/SELL recommendation",
using skill .opencode\skills\stock-analysis
```

**Example — stock deep research**

```text
analysis topic "produce an institutional-grade equity research note on 1810.HK with a call and price target",
using skill .opencode\skills\stock-deep-research
```

The agent will load the skill's `SKILL.md`, walk through the phases halting at human-gated checkpoints, and write all intermediate artifacts to your local project folder.

---

## 🔄 The 6-Phase Pattern (deep-research)

```
[ User Query ]
    │
    ▼
┌──────────────┐   ┌──────────────┐   ┌─────────────────┐   ┌────────────────┐
│  proposal.md │ → │    specs/    │ → │ notebooks/*.ipynb│ → │  /dist/        │
└──────────────┘   └──────────────┘   └─────────────────┘   └────────────────┘
 (The Strategy)     (The Schema)       (Trackable Labs)      (index.html Web)
                          │                  ▲                     ▲
                          ▼                  │                     │
                [ HUMAN INTERACTION ] ───────┴─────────────────────┘
               (Verify & Learn Schema)    (Manual adjustments anytime)
```

1. **Query Deconstruction** — parse intent, isolate variables, surface knowledge gaps.
2. **Strategy Proposal** — high-level blueprint of domains, sources, and investigation paths.
3. **Schema & Spec Mapping** — build the target grid. **🛑 Human gate.**
4. **Targeted Web Discovery** — parallel search agents index sources into a local Knowledge Base.
5. **Notebook-Driven Analysis** — fully transparent Jupyter notebooks. You can read and re-run every cell.
6. **Artifact Synthesis** — a self-contained, browser-openable `index.html` report.

---

## 🧭 The Culture-Research Pattern

```
Explore → Search Design → Region-Parallel Search → Acquisition
                                              │
                                              ▼
                                Deep Reading (1 sub-session per region)
                                              │
                                              ▼
                              Knowledge Base (entities + relations)
                                              │
                                              ▼
              Phase 5: Epistemic Stress-Test & Systems Mapping  ←── NEW in v3.3
              (Axiomatic Audit + Steelman Red Team + Causal Loops)
              → stress-tested-matrix.json (authoritative Reduce input)
                                              │
                                              ▼
                          Round 1: Thematic  →  Round 2: Cross-Cultural
                          Round 3: Contradictions →  Round 4: Gaps
                          Round 5: Research Questions
                                              │
                                              ▼
                              Iteration Checkpoint  ←── loop back if weak
                                              │
                                              ▼
                                  Synthesis Document
                                                  │
                                                  ▼
                              Science Communication
                              (article, brief, summary, slide deck)
```


Supports projects with 20+ papers via sub-session orchestration — each sub-session has explicit end-conditions, batch notes, and file persistence to the same project directory.

---

## 🧭 The Frontier-Research Pattern

```
01 System Map → 02 Harvest → 03 Epistemic Ledger → 04 Red-Team
                                                        │
                                                        ▼
               Phase 5: EPISTEMIC STRESS-TEST  ←── dedicated gate (v1.0)
               (Axiomatic Audit + Steelman + Causal Loops + CCS routing)
               → evidence/05-stress-tested-matrix.json
                                                        │
                                                        ▼
               06 Generative Synthesis (divergent)
                                                        │
                                                        ▼
               Phase 7: USER CALIBRATION  ←── human sign-off gate
               (fold budget/timeline/preference into user_constraints)
                                                        │
                                                        ▼
               08 Deep Convergence → 09 Report Drafting → 10 Self-Audit
                                                              │
                                                              ▼
                                               FINAL_DELIVERABLE_REPORT.md
```

Built for engineering / science / frontier-tech topics: it forces cross-domain abstraction and counterfactual reasoning (Phase 6) and scanner-of-speculation final audit (Phase 10), keeping the release honest about what is verified, inferred, or unknown.

---

## 🧭 The Stock-Analysis Pattern

A single-stock workflow on free, public, no-API-key sources:

```
01 Scope → 02 Collect → 03 Fundamentals → 04 Valuation
                 │            │                 │
                 ▼            ▼                 ▼
        05 Technicals → 06 Catalysts & Risks → 07 Synthesize
                                                │  (human reviews the proposed call)
                                                ▼
                                      08 Report: BUY / HOLD / SELL
                                      + price target, confidence, falsification criteria
```

---

## 🧭 The Stock-Deep-Research Pattern

The institutional-grade fusion of `stock-analysis` + `deep-research`:

```
01 Scope → 02 Collect → 03 Fundamentals → 04 Valuation (DCF + reverse-DCF + SOTP)
                                                             │
                                                             ▼
                                           05 Technical & Market Regime
                                                             │
                                                             ▼
                               06 Bull/Bear Debate & Catalysts (adversarial)
                                                             │
                                                             ▼
                               07 Fragility Audit & Red-Team (epistemic stress-test)
                                                             │
                                                             ▼
                08 Synthesize & Govern → deterministic Quality / Regime /
                Sanity / Critical-News gates → rating + target + confidence + conviction
                                                             │  (human reviews the call)
                                                             ▼
                        09 Analyst Note: BUY / HOLD / SELL / AVOID / WATCH
                        + price target, falsification criteria, action conditions
```

---

## 🧭 Ongoing Evolution

These skills are not static. Every research project that uses them generates feedback:

- **Weak spots** found during review are fixed at the phase level
- **Methodology gaps** discovered during analysis are codified into new principles
- **Director Observations** from sub-sessions accumulate into `skill-evolution-log.md` entries
- Each post-archive step produces documented improvements that feed back into the skill itself

The more you research with these skills, the sharper they become.

---

## 🎯 When to Use vs. When to Skip

### ✅ Great fit
- Market / competitor matrix mapping
- New technology or protocol deep-dive
- Literature and documentation audits
- Cultural / behavioral qualitative studies
- Bilingual (EN/ZH) research reports with website output
- Single-stock analysis with a written BUY / HOLD / SELL view (HKEX-optimized)
- Institutional-grade equity research on a single company (Bull/Bear debate + DCF + fragility audit + governance gates)

### ❌ Not a fit
- Single-fact Q&A ("what is the capital of X?")
- Creative writing, brainstorming, naming
- Quick debugging or instant code fixes
- Time-critical answers (the human gate is intentional, not a bug)
- Executing trades, portfolio rebalancing, or building a live trading bot (the stock skills are research + recommendation only, not execution)

---

## ⚠️ Disclaimer

This project is an **experimental, independent-developer** project shared publicly for educational and collaborative purposes.

> **Use at your own risk.** No guarantees or warranties are provided regarding stability, security, API cost / token management, or performance. OpenCode update frequently outside this project — breaking changes may occur. Anyone adapting or executing these skills in their own agent environments assumes full responsibility for any outcomes.

## 📄 License

MIT — see [LICENSE](LICENSE).
