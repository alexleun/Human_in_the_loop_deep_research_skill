# opencode Skill Changelog

## stock-analysis v2.1 — 2026-09-06
**Applied lessons from two live evolution logs (`log/001-skill-evolution-log.md` — 0001.HK CK Hutchison; `log/007-skill-evolution-log.md` — 0700.HK Tencent):** valuation conventions (implied-required-return reverse-DCF, median-of-methods targets), first-class non-IFRS↔IFRS and FCF-definition labeling, revenue/turnover scope labeling, price-freshness output, report-filename single source of truth, review reminders with date AND reason, and HKEXnews record-once extraction handling.
### stock-analysis v2.1
| Change | Detail |
|---|---|
| **Reverse-DCF = Implied Required Return** | §2b canonical reading is now the implied required return at 0% growth; when DCF value at 0% growth exceeds market price, report "market applies a higher required return / holding discount". A growth-solver that pins at a bound is labeled **degenerate**. |
| **Median-of-Methods Target** | Default price target = **median** of the SOTP/DCF/peer/DDM outputs, never an arbitrary blend; scenario weighting uses the base-median method set with **floor/ceiling methods excluded BEFORE weighting** (DDM floor bug: −11% → +8%). |
| **Non-IFRS ↔ IFRS Bridge (First-Class)** | Explicit item-by-item bridge (SBC, investee/associate contributions, intangible amortization, one-offs); driving line (reported / IFRS / non-IFRS) always labeled. |
| **FCF Definition Labeling** | Every FCF figure labeled **official vs aggregator-standard**; when they differ (e.g. 182.6B vs 215.6B), **report both with definitions** — never pick silently. Conflicting definitions surface as contested signals into Phase 7 (Fragment 2). |
| **Revenue/Turnover Scope Labeling** | Consolidated vs including-associates scope stated per source (0001's ~280B vs ~507B trap); flagged in `sources_index.md`, Phase 3, and the report. |
| **Price-Freshness Outcome in Outputs** | Phase 5 outputs include the freshness outcome: primary vs secondary closes, stale-source exclusions, primary source + as-of timestamp. |
| **Report Filename = Single Source of Truth** | `report/<Code>-<Company>-<YYYY-MM-DD>-analysis.md` fixed in the Phase 1 output contract; divergence rule (Phase-1 name wins, both corrected); `task_state.json` and the note must match. |
| **Review Reminder with Date AND Reason** | `task_state.json.review_reminder = {"date", "reason"}`; completion checklist and post-report lifecycle updated. |
| **HKEXnews Record-Once** | HKEXnews annual/interim PDFs recorded once as not machine-extractable; no per-run re-attempt — direct to the documented aggregator-substitute access ladder. |
| **Task Ticking Discipline** | Ticking at each phase finish now also requires syncing `task_state.json` and filling change artifacts as phases run. |
| **Guardrails** | Canonical file set (superseded files renamed `*.legacy.md`); main-spec requirement headers kept stable (active-change specs renamed via explicit renames only). |
| **Version** | `skill.json` 2.0 → 2.1. |

## stock-analysis v2.0 — 2026-09-05
**Re-architecture: the canonical single-stock skill.** Absorbed all institutional-grade single-stock content from stock-deep-research v1.x so every single-stock request routes to one skill. Expanded from 8 to 9 phases and folded in the document-intelligence layer + adversarial debate + fragility audit + governance gates + AVOID/WATCH.
### stock-analysis v2.0
| Change | Detail |
|---|---|
| **9-Phase Protocol (from 8)** | `01-scope → 02-collect → 03-fundamentals → 04-valuation → 05-technicals → 06-debate → 07-fragility-audit → 08-synthesize → 09-report`. `06-debate.md` and `07-fragility-audit.md` added; `06-catalysts-risks.md` merged into debate; old `07-synthesize.md`/`08-report.md` renumbered. |
| **Adversarial Bull/Bear Debate (Phase 6)** | Bull and Bear argued independently and at their strongest before any synthesis; fed by document appraisals, event timeline, and verbatim quotes (adopted from stock-deep-research v1.x). |
| **Fragility Audit (Phase 7)** | Fragility as a valuation input — concentration, policy, litigation, supply-chain, inventory — with disclosure / multiple haircut / scenario discount; contested-signal detection from `findings-index.json`. |
| **Deterministic Governance Gates (Phase 8)** | Rule-based Quality / Regime / Sanity / Critical-News gates that cannot be argued out of position before a rating is published. |
| **5-State Rating** | BUY / HOLD / SELL / **AVOID** / **WATCH** with price target, confidence (0–1), conviction (HIGH/MEDIUM/LOW), falsification criteria, action conditions. |
| **Document Intelligence Layer (Phase 2/3)** | Search protocol, coverage reports with `evidence_status` / `#access` / `#status` tags, access ladder, verbatim-quote rule, URL verification, deep-read appraisals under `documents/appraisals/`, `documents/findings-index.json`, `documents/event-timeline.md` with as-of windowing. |
| **Confidence Rubric (Phase 8)** | 0–10 numeric score across 5 axes; wide spread or unreconciled earnings caps at MEDIUM; conviction computed. |
| **Timestamped Report + Task Ticking** | Report saved as `<Code>-<Company>-<YYYY-MM-DD>-analysis.md` with prior versions kept; `tasks.md` ticked at the end of every phase. |
| **Bluebook Report Style** | Goldman/BlueBook-style analyst note chain (thesis → summary table → debate → valuation → terms of risk), Gates 2/3 for recommendation and report approval. |
| **Version** | `skill.json` 1.2 → 2.0; header "(v1.2)" → "(v2.0)". |

## stock-deep-research v2.0 — 2026-09-05
**Re-architecture: whole-market (index-level) outlook skill.** Repurposed from single-stock to market-level analysis. Computation-native and direct-from-source: every signal is computed by shipped Python, never transcribed from aggregators. Single-stock requests are rejected in Phase 1 and routed to `stock-analysis`.
### stock-deep-research v2.0
| Change | Detail |
|---|---|
| **Whole-Market Subject** | Market / index unit (e.g. HSI, S&P 500) fixed in a Phase 1 contract; 1–3 month horizon; Bullish / Neutral / Bearish stance + target band + sector tilts + watchdog signals. |
| **Computation-Native (9 phases)** | `01-scope → 02-collect → 03-market-fundamentals → 04-market-valuation → 05-technicals-and-regime → 06-market-debate → 07-fragility-audit → 08-synthesize → 09-market-report`. |
| **8 Starter Templates (`templates/`)** | `01_index_stats`, `02_regime`, `03_breadth`, `04_market_valuation`, `05_sector_rs`, `06_scenarios`, `chart`, `08_event_timeline`. Each range-fetches or loads data, computes with sanity gates, persists CSV/JSON/PNG artifacts; all pass `python -m py_compile`. |
| **Direct-From-Source Numeric Statistics** | Dedicated pipelines range-fetch official index stats (index value, 52-week high/low, P/E, gross dividend yield) from index/issuer domains — no aggregator retyping. |
| **Regime & Breadth Notebooks (Phase 5)** | Technical regime (trend vs range) + breadth with anti-lookahead event-windowing capped at the as-of date; standard price + MA20/50/200 + volume chart in `report/charts/<market>-price-<asof>.png`. |
| **Valuation Percentile + Scenario Band (Phase 4)** | Level-relative valuation percentile and dispersion; numbered scenario notebook with sanity gates producing a target band. |
| **Document Intelligence Layer** | Search protocol, coverage reports (`evidence_status`, `#access`, `#status`), access ladder, verbatim-quote rule, deep-read appraisals, `findings-index.json`, event timeline with as-of windowing. |
| **Governance Gates + Six-Axis Confidence (Phase 8)** | Deterministic Quality / Regime / Sanity / Critical-News gates then six-axis confidence rubric (breadth, trend integrity, valuation, macro regime, event shock, data confidence) with explicit counters. |
| **Per-Market State** | `skill.json` `task_state_path` now `{market}`; `template-task_state.json` type `whole-market-analysis`; task ticking at end of each phase. |
| **Version** | `skill.json` 1.2 → 2.0; header "(v1.2)" → "(v2.0)". |

## stock-analysis v1.2 — 2026-09-05
**Refined from the stock-analysis v1.1 run on 0992.HK (Lenovo Group):** closed 12 operational weak points found during the run — unreadable primary PDFs, a missing reverse-DCF, silent units/currency bugs, stale sources, unreconciled earnings, unhandled EPS dispersion, unspecified peer FX, no environment probe, no task ticking, and no chart artifacts.
### stock-analysis v1.2
| Change | Detail |
|---|---|
| **Environment Probe (Phase 1)** | Check python libs, container availability, console encoding, and source-domain reachability BEFORE Phase 2; record the environment line in `task_state.json` so the fallback is decided early. |
| **Primary-PDF Extraction Fallback (Phase 2)** | Attempt `pdftotext`/HTML/Python extraction; if a filing is not machine-readable, log the aggregator substitution + reason (source preservation raised from advisory to operational). |
| **Earnings Reconciliation (Phase 3)** | Mandatory pass reconciling reported op profit vs sum of segment op profits vs adjusted profit; hunt one-off/non-cash items (warrant revaluation, CB interest, impairments); label which line drives the read. |
| **Currency Consistency (Phase 3)** | State every source's reporting currency; mixed-currency comparisons carry an FX assumption. |
| **Units/Currency Sanity Gate (Phase 4)** | `check_units()`/`--sanity` assert per script output (e.g. `0 < price-target < 100×EPS`); catches `/1000` and USD→HKD bugs before a number enters the report. |
| **Reverse-DCF Required (Phase 4)** | Concrete script sketch (root-solve `Price(DCF(g)) = market`); if skipped, record the gap explicitly — no aspirational task. Payout-ratio sanity check added. |
| **Forward-EPS Dispersion Check (Phase 4)** | Sample 2+ estimate sources before applying a forward P/E; if max/min differ > ~20%, prefer scenario-weighted valuation and disclose the range. |
| **Peer FX Rule (Phase 4)** | State each peer's reporting currency; adjust to a common basis or disclose FX assumptions. |
| **Price-Freshness Check (Phase 5)** | Compare primary close vs 1–2 secondary quotes; flag stale (>2 trading days or >1% off) sources; excluded sources recorded. |
| **Standard Chart (Phase 5)** | Price + MA20/50/200 + volume chart by default under `report/charts/`; price series persisted to `data/<code>-price-history-<asof>.csv` for technical diffs. |
| **Confidence Scoring Rubric (Phase 7)** | Numeric 0–10 score across 5 axes, mapped to High/Medium/Low; wide valuation spread or unreconciled earnings caps at Medium. |
| **Timestamped Report + FX/Artifacts (Phase 8)** | Report saved as `<Code>-<Company>-<YYYY-MM-DD>-analysis.md`; prior dated versions kept for diffing; methodology lists reverse-DCF, reconciliation, FX, and chart references. |
| **Task Ticking Discipline** | Tick `tasks.md` at the end of every phase, not at archive time. |
| **Layout Sync** | `data/<code>-price-history-*.csv`, `report/charts/`, mandatory `skill-evolution-log.md`. |
| **Version** | `skill.json` 1.1 → 1.2. |

## stock-analysis v1.1 — 2026-09-04
**Refined from two live HKEX runs (0066.HK, 1810.HK):** closed process gaps found in the skill-evolution logs — source preservation was skipped, approval gates were not enforced, technical data fallbacks were unhandled, and valuation was over-tuned toward a target.
### stock-analysis v1.1
| Change | Detail |
|---|---|
| **"STOP and ask" Gates** | Principle 8 now implements Gates 1–3 as explicit stop points: present scope, present recommendation (Phase 7→8), present final report — no proceeding until the human approves. |
| **Source Preservation Enforced** | `02-collect.md`: "fetch first, extract after" — save every fetched source to `sources/` with the `write` tool at fetch time; `sources_index.md` gains a Local Copy column; "n/a (fetched)" is a gap, not done. |
| **End-Condition Compliance Check** | Phase 2 adds a compliance mapping: each end condition points at actual evidence; unmet items truthfully flagged as gaps; an end-condition is done only when its evidence is stated, not asserted. |
| **Technical-Data Fallback** | `05-technicals.md`: if OHLC can't be fetched directly — document the limitation, cross-reference ≥2 independent aggregators, and mark independently-computed vs third-party indicators. |
| **DCF Sensitivity-Before-Compute** | `04-valuation.md`: freeze the assumption block and write the sensitivity grid (growth × WACC) BEFORE the first run; never re-tune to hit a target; flag any recalibration as a revision; report a range, not a point. |
| **Real Peer Table** | Relative valuation requires 3–6 real listed comparables with each peer's own multiples and a computed discount/premium — never an opaque single-aggregator composite. |
| **Multi-Stock Layout** | Suggested layout becomes `stock-analysis-{code}/` per analysis; `skill.json` `task_state_path` updated accordingly. |
| **Post-Report Lifecycle + Done State** | SKILL.md adds Post-Report Lifecycle (archive, review reminder, re-review flow) and a Completion Checklist marking the real terminal state. |
| **Phase Loading + Revisit Triggers** | Phase Router instructs reading each phase file before work; explicit revisit triggers (e.g. valuation contradicts growth → revisit Phase 3) added. |
| **Version** | `skill.json` 1.0 → 1.1. |

## stock-deep-research v1.1 — 2026-09-04
**Refined in parallel with stock-analysis** — same lessons applied to the fused 9-phase skill (which inherits identical source-preservation, gating, DCF, and peer-comparison requirements).
### stock-deep-research v1.1
| Change | Detail |
|---|---|
| **"STOP and ask" Gates (P13)** | Gates 1–3 are explicit stop points (scope → collect; recommendation → note; note acceptance). |
| **Source Preservation Enforced (P11)** | Phase 2: fetch-and-save with the `write` tool; Local Copy column; compliance mapping to real evidence. |
| **DCF Sensitivity-Before-Compute (Phase 4)** | Freeze assumptions, write sensitivity grid first, never re-tune, report a range; peer table uses real comparables with per-peer multiples + discount/premium. |
| **Technical-Data Fallback (Phase 5)** | Document OHLC limitation, cross-reference ≥2 aggregators, distinguish independently-computed vs third-party indicators. |
| **Multi-Stock Layout** | `stock-deep-research-{code}/`; `skill.json` `task_state_path` updated. |
| **Post-Report Lifecycle + Done State** | SKILL.md adds lifecycle (archive, review date, re-review) and Completion Checklist. |
| **Phase Loading + Revisit Triggers** | Phase Router loading instruction; revisit triggers from fragility/debate/valuation surprises. |
| **Version** | `skill.json` 1.0 → 1.1; header "(v1.0)" → "(v1.1)". |

## stock-deep-research v1.2 — 2026-09-05
**Refined in parallel with stock-analysis v1.2** — the same 12 lessons from the 0992.HK run applied to the fused 9-phase skill (which inherits identical sanity, reconciliation, dispersion, FX, freshness, chart, and task-ticking requirements).
### stock-deep-research v1.2
| Change | Detail |
|---|---|
| **Environment Probe (Phase 1)** | Python libs, container, console encoding, source-domain reachability checked before Phase 2; recorded in `task_state.json`. |
| **Primary-PDF Extraction Fallback (Phase 2)** | `pdftotext`/HTML/Python extraction attempted; unreadable filings require a logged aggregator substitution + reason. |
| **Earnings Reconciliation (Phase 3)** | Reported vs segment vs adjusted profit reconciled; one-off/non-cash items hunted and labeled; driving line stated. |
| **Currency Consistency (Phase 3)** | Per-source reporting currency stated; mixed-currency comparisons carry an FX assumption. |
| **Units/Currency Sanity Gate (Phase 4)** | `check_units()`/`--sanity` assert per script output; payout printout sanity-checked (a 0% payout from a dividend payer is usually a bug). |
| **Reverse-DCF Concrete Steps (Phase 4)** | Root-solve `Price(DCF(g)) = market` script sketch; skipping requires an explicit recorded gap — no aspirational task. |
| **Forward-EPS Dispersion Check (Phase 4)** | 2+ estimate sources sampled before a forward P/E; > ~20% spread → scenario-weighted valuation + disclosed range. |
| **Peer FX Rule (Phase 4)** | Per-peer reporting currency; common basis or disclosed FX assumption. |
| **Price-Freshness Check (Phase 5)** | Primary close vs 1–2 secondary quotes; >1% or >2-day-old sources excluded or flagged. |
| **Standard Chart (Phase 5)** | Price + MA20/50/200 + volume chart in `report/charts/`; price series in `data/<code>-price-history-<asof>.csv`. |
| **Confidence Scoring Rubric (Phase 8)** | Numeric 0–10 retained alongside confidence/conviction; wide spread or unreconciled earnings caps at MEDIUM. |
| **Timestamped Note + FX/Artifacts (Phase 9)** | `<Code>-<Company>-<YYYY-MM-DD>-analyst-note.md`; methodology lists reverse-DCF, reconciliation, FX, chart refs. |
| **Task Ticking Discipline** | Tick `tasks.md` at the end of every phase, not at archive time. |
| **Layout Sync** | `data/<code>-price-history-*.csv`, `report/charts/`, mandatory `skill-evolution-log.md`. |
| **Version** | `skill.json` 1.1 → 1.2; header "(v1.1)" → "(v1.2)". |

## stock-analysis v1.0 — 2026-09-03
**New skill: Single-Stock Analysis (HKEX-optimized, public-only sources).**
Adds an 8-phase workflow for reaching a written BUY / HOLD / SELL view on a single listed company using only free, public, no-API-key sources. Blends fundamentals, valuation, technicals, and catalysts/risks into an explicit recommendation with a price target, confidence, and falsification criteria.
### stock-analysis v1.0
| Feature | Detail |
|---|---|
| **8-Phase Blended Protocol** | `01-scope → 02-collect → 03-fundamentals → 04-valuation → 05-technicals → 06-catalysts-risks → 07-synthesize → 08-report`. |
| **Public-Source Only** | Free, public, no-API-key data (HKEXnews, reports, free aggregators); substitute a documented free alternative if paywalled; never fabricate data. |
| **Grounding & Anti-Hallucination** | Every factual output carries exact quoted text or citation + as-of date; facts vs claims vs inference distinguished (adopts deep-research P2). |
| **Code-First Computation** | Ratios, CAGRs, DCF, scenario math run in Python (adopts deep-research P3); Source Preservation (P20) and End-Conditions Discipline (P15) adopted from deep-research. |
| **Explicit Recommendation** | BUY / HOLD / SELL + price target, horizon, confidence, falsification criteria, disclaimer. |
| **Human-Approval Gates** | After Scope (contract), after Synthesize (call review), and at report approval — the human makes the final investment call. |
| **State Template** | Ships `template-task_state.json` (skill, current_phase, per-phase status, decision date, horizon, rating, price target). |

## stock-deep-research v1.0 — 2026-09-03
**New skill: Institutional-Grade Equity Research (fuses stock-analysis + deep-research).**
Adds a 9-phase analyst-note workflow with an evidence-first, code-first methodology: adversarial Bull/Bear debate, DCF + reverse-DCF + SOTP, a fragility audit (epistemic stress-test), deterministic governance gates, and an explicit BUY / HOLD / SELL / AVOID / WATCH call with confidence, conviction, price target, and falsification criteria.
### stock-deep-research v1.0
| Feature | Detail |
|---|---|
| **9-Phase Protocol** | `01-scope → 02-collect → 03-fundamentals → 04-valuation → 05-technicals → 06-debate → 07-fragility-audit → 08-synthesize → 09-report`. |
| **Evidence-First / Fact Taxonomy** | Fact / Derived-Fact / Analysis taxonomy; narrative translated into economics; a model may complete an analysis chain but never invent a missing fact (P1). |
| **Adversarial Bull/Bear Debate** | Bull and Bear argued independently and at their strongest before any synthesis (P5); refutation pass refutes hallucinations before the call. |
| **Multi-Method Valuation** | Relative + DCF + reverse-DCF + SOTP for mixed-quality businesses → fair-value range + price target (P3, P4). |
| **Fragility Audit** | Fragility as a valuation input, not an appendix — disclosure / multiple haircut / scenario discount per risk (P10). |
| **Deterministic Governance Gates** | Rule-based Quality / Regime / Sanity / Critical-News gates that cannot be argued out of position (P6). |
| **Anti-Lookahead Discipline** | Pre-cutoff facts vs post-cutoff reasoning separated; no decision justified with data dated after the as-of date (P9). |
| **Rating + Conviction** | BUY / HOLD / SELL / AVOID / WATCH + confidence (0–1), conviction (HIGH/MEDIUM/LOW), falsification criteria, action conditions (P7, P8). |
| **Human-Approval Gates** | After Scope, before finalizing the note (call review, Phase 8→9), and at note approval (P13). |
| **State Template** | `template-task_state.json` with per-phase status, decision date, horizon, rating, price target. |

## frontier-research v1.0 — 2026-09-03
**New skill: Engineering / Science / Frontier-Tech Research.**
Adds a fifth skill to the repository, designed for topics where rigorous technical claims, complex systemic dynamics, and honest uncertainty reporting matter. Built from the branch chat log `Introduction to Critical Thinking.md`, it ships a 10-phase protocol with a **dedicated epistemic stress-test gate** and a **user-calibration gate**, driven by three core mental frameworks (Systems Thinking; Critical Thinking & Anti-Bias; Epistemic First Principles & Triangulation).
### frontier-research v1.0
| Feature | Detail |
|---|---|
| **10-Phase Protocol** | `01-system-map → 02-harvest → 03-epistemic-ledger → 04-red-team → 05-epistemic-stress-test → 06-generative-synthesis → 07-calibration → 08-deep-convergence → 09-report-drafting → 10-self-audit`. |
| **Phase 5 Stress-Test Gate** | **Reuses the shared culture-research v3.3 methodology** (Axiomatic Audit, Steelman Red Team, Causal Loops & Systems Mapping, CCS routing) rather than redefining it — keeping methodology aligned across skills. Input `evidence/03-epistemic-ledger.md`; output `evidence/05-stress-tested-matrix.json`; downstream phases (6/8/10) must not cite `Unsubstantiated_Speculation` claims. |
| **Phase 7 Calibration Gate** | Presents the systems map, red-team findings, stress-test matrix, and innovation hypotheses to the user and folds budget / timeline / technical preference into `project-state.json → user_constraints` before convergence. |
| **Three Mental Frameworks** | Systems Thinking (causal loops, stocks & flows, feedback), Critical Thinking & Anti-Bias (premise verification, red-teaming, steel-manning, counterfactual), Epistemic First Principles & Triangulation (≥2 independent sources, `[Fact]/[Hypothesis]/[Speculation]` labeling, physical/mathematical consistency). |
| **Anti-Hallucination Guardrails** | Calculations First, Citation Requirement (every metric carries source + epistemic tag), Uncertainty Quantification (`[DATA DEFICIT: Requires Empirical Testing]`). |
| **State Model** | `project-state.json` with `user_constraints` + `epistemic_ledger` (`verified_facts` / `unverified_claims` / `falsified_hypotheses`) for honest multi-session resume. |
| **Public Docs** | README skill-table row, repository-structure block, feature-table, and 10-phase pattern diagram added; CHANGELOG entry created. |

**Focus: Epistemic Stress-Test & Systems Mapping phase.**
Adds a destructive evidence-verification phase to culture-research and adapts it to deep-research's code-first Phase 7 Review. Replaces the earlier "Phase 2.5" proposal after SHUFFLE resolved the matrix structure; the new phase is inserted as **Phase 5** (post-Knowledge Base), shifting Phases 5–9 to 6–10. See `GAP-ANALYSIS.md` at repo root for the full before/after mapping and applicability matrix.
### culture-research v3.3
| Change | Detail |
|---|---|
| **New Phase 5** (`05-epistemic-stress-test.md`) | Axiomatic Audit (evidence grounding), Steelman Red Team (anti-confirmation-bias), Causal Loops & Systems Mapping (emergence lens). Emits `stress-tested-matrix.json`. |
| **Cognitive Complexity Score (CCS)** | `CCS = min(10, Contradiction_Density×3.5 + Chain_Length×0.3 + Loop_Count×0.8)`. Routes to Mode A (automated) or Mode B (Strategic HITL, 2–3 forks). |
| **New Principle 18** (SKILL.md) | Epistemic Stress-Test & Systems Mapping. |
| **Principle 17** (SKILL.md) | Updated: GATE = Phase 5, REDUCE = Phase 6, SS8→SS9, SS9→SS7 references for Sleep/Eating. |
| **Renumbered phase files** | `05-multi-round-analysis.md`→`06`, `06-checkpoint.md`→`07`, `07-synthesis.md`→`08`, `08-sub-session-orchestration.md`→`09`, `09-report-writing.md`→`10`. Use `git mv` (folder is a git repo). |
| **Cross-references updated** | `03-deep-read.md`, `04-knowledge-base.md`, `06/07/08/09/10-*.md`: input gates, SS renumber (SS7 audit, SS9 Eating/Sleep, SS13 checkpoint, etc.), report-writing Phase 10. |
| **SKILL.md** | Workflow diagram, Phase Router, Cross-Phase Gates (Epistemic Stress-Test Completion Gate), File Persistence (`stress-tested-matrix.json`), findings-index `epistemic_status` field. Version `skill.json` 3.1 → 3.3. |
### deep-research v2.3
| Change | Detail |
|---|---|
| **New Principle 21** (SKILL.md) | Epistemic Stress-Test & Systems Mapping adapted to the code-first model (script-based CCS, JSON/DOT systems maps). |
| **Phase 7 Epistemic Audit** (`07-review.md`) | Axiomatic citation validation, Steelman counter-hypotheses, causal loop mapping; CCS computed by script; results folded into the review manifest. |
| **End Conditions** | Added Epistemic Audit checklist + audit summary requirement. |
| **Guardrails** | Added "Run the epistemic audit at review" rule. Version `skill.json` 2.2 → 2.3. |

## deep-research v2.2 — 2026-06-09
**Focus: Cross-skill refinement from quantitative project experience.**
Informed by a 202-day Hong Kong passenger statistics project (single-language, quantitative, 5M+ records). Adds new principles, shortcuts, and optional features based on real-world pain points — no new files created.
### Updated Principles (SKILL.md)
| Principle | Change |
|---|---|
| **6. Encoding Awareness** | Added Windows stdout encoding guidance: `sys.stdout.reconfigure(encoding='utf-8')` with try/except, required before any `print()` containing CJK/Unicode characters on Windows. |
| **Cross-Phase Gates: Parity Check** | Made optional — annotated "(skip for single-language projects)" in gate table. |
### Phase File Updates
| File | Changes |
|------|---------|
| `03-collect.md` | Added **Existing-data shortcut** at top: skip fetch if data pre-exists, go directly to validation and pipeline setup |
| `04-analyze.md` | Added **CJK Font Verification** section (before batch figure generation): matplotlib font check script, font fallback config, placement instruction |
| `05-report.md` | Added **Discovery-First Framing** as optional report-writing mode (cross-pollinated from culture-research), with key rules and audience-based selection guidance |
| `08-iterate.md` | Added **Dashboard-first iteration** note: prefer dashboard updates over full report regeneration for data-heavy projects |

## culture-research v3.2.1 — 2026-06-08
**Focus: Structural Map-Reduce Optimization.**
Informed by the 38-paper pain-and-culture project, this minor update formalizes the Map-Reduce dispatch logic within the existing v3.2 workflow. No new files or principles created; existing analysis phases now strictly enforce thematic decomposition.
### Updated Principles (SKILL.md)
| Principle | Change |
|---|---|
| **3. Analysis Multi-Round** | Explicitly redefined as a **Map-Reduce** process: 1. MAP (Map findings to #theme tags during reading); 2. SHUFFLE (Group findings by tag in findings-index.json); 3. REDUCE (Dispatch theme-specific sub-sessions). |
| **17. Map-Reduce Analysis Architecture** | **NEW.** Formalized requirement for Phase 5 (Analysis). Requires theme-based sub-session dispatching rather than paper-based aggregation. |
### Updated Workflow Structure (SKILL.md)
| Section | Change |
|---|---|
| **Workflow Overview** | Replaced flow diagram with a **Map-Reduce visualized architecture**, explicitly highlighting the "Map-Reduce Dispatch" gate between Phase 4 and Phase 5. |
### Phase File Updates
| File | Changes |
|---|---|
| 03-deep-read.md | Added mandatory **Atomic Finding + Tag Mapping** instruction: every extracted finding must be bound to a #behavior/{domain} or #theme tag at the point of extraction. |
| 04-knowledge-base.md | Updated findings-index.json logic: mandated theme-based grouping (theme -> [list of findings]) to facilitate the Shuffle layer of Map-Reduce. |
| 05-multi-round-analysis.md | Formalized **Dispatch Rule**: PM must launch one sub-session per theme identified in findings-index.json. Each sub-session receives ONLY findings related to its theme to reduce context noise and improve cross-cultural contradiction analysis. |
| 07-synthesis.md | Added **Assembly Instruction**: synthesis synthesis must be performed by stitching together the pre-analyzed/reduced theme documents, enforcing Discovery-First Framing. |


## culture-research v3.2 — 2026-06-07

Major upgrade from a 38-paper, 3-region pain-and-culture project. Consolidates a failed-first-draft report-writing cycle into structural improvements. New principles added — no new files created.

### New Principles (SKILL.md)

| Principle | Description |
|-----------|-------------|
| **14. Discovery-First Framing** | Every report-writing output must lead with claims about the world, not claims about the research process. Methodology mentioned exactly once in an endnote. Critical omission from v3.0/3.1 that caused a full-report rewrite. |
| **15. Human-Approval Gates** | Formal gates after Explore (research question), Checkpoint (verdict), Synthesis (document), and Report Writing (section plan) require explicit human sign-off before proceeding. Prevents progressing on misaligned foundation. |
| **16. Unfindable Paper Protocol** | Systematic handling of papers that cannot be accessed: timeboxed attempts, minimal appraisal with `no-abstract-available`, no replacement, documented in coverage report. |

### Updated Sections (SKILL.md)

| Section | Change |
|---------|--------|
| **Header** | Version bumped from v3.1 to v3.2; v3.2 changes summary paragraph added |
| **Cross-Phase Gates** | Added Human-Approval Gate row (after Explore, Checkpoint, Synthesis, Report Writing) |
| **File Persistence** | Updated to reflect `report/` directory convention (not `knowledge-base/article/`); added `report-charter.md`, `rewrite/` subdirectory, `section-plan.md` |

### Phase File Updates

| File | Changes |
|------|---------|
| `09-report-writing.md` | **Major rewrite.** Added Core Principle: Discovery-First Framing with concrete checks. Added pre-writing section plan approval gate. Added style calibration heuristic table (Aeon/Atlantic/Sapiens/Nature profiles). Added variable-length planning table (200-1000 words per section role). Added methodology placement rule (endnote only). Added collaboration-first pattern as alternative to sub-agents. Added failure mode #7 ("Article reads as methodology report"). Expanded quality checklist with discovery-first checks. Updated file naming conventions to `report/`. |
| `01-explore.md` | Added region-count sizing guide table (1-2 / 3-4 / 5-6 / 7+ regions with paper count, SS count, best-fit). Added human-approval gate to end conditions. |
| `02-search-collect.md` | Added search-protocol.md template reference. Added cross-region deduplication rules (DOI match, title+surname match, conflict resolution). |
| `03-deep-read.md` | Added Unfindable Paper Protocol (5-minute timebox, minimal appraisal, no replacement). Added Mid-Phase Calibration guidance (review after first 3-5 appraisals before scaling). |
| `04-knowledge-base.md` | Added multi-context finding handling guidance (array of contexts vs separate entities). |
| `05-multi-round-analysis.md` | Added calibration run guidance for analysis rounds (test on 1 domain for R1, 2-3 rows for R2, 1-2 cells for R3 before scaling). |
| `08-sub-session-orchestration.md` | Replaced fixed 15-SS sequence table with Project Sizing Guide: Small (5 SS, 1-2 regions, 5-15 papers), Medium (13-15 SS, 3-4 regions, 20-50 papers, recommended), Large (18-22 SS, 5-6 regions, 40-80 papers), Exhaustive (25+ SS, 7+ regions, 60+ papers). |

## deep-research v2.1 — 2026-06-05

Consolidated cross-skill lessons from the culture-research v3.1 upgrade (67-paper, 8-region gift-giving project). Targeted edits — no new files created.

### New Principles (SKILL.md)

| Principle | Description |
|-----------|-------------|
| **20. Source Preservation** | Mandatory local copy of all fetched content before extraction; filename recorded in source metadata |

### Updated Sections (SKILL.md)

| Section | Change |
|---------|--------|
| **Post-Research → openspec Bridge** | Replaced placeholder reference to v1.0 with detailed artifact mapping table (research outputs → openspec change artifacts) |
| **Guardrails** | Updated "Log every source" to reference Principle 20; added "Map artifacts to openspec before archiving" |
| **Header** | Version bumped from v2.0 to v2.1; change description added |

## culture-research v3.1 — 2026-06-05

Consolidated feedback from a 67-paper, 8-region gift-giving project. Targeted edits to existing files — no new files created.

### New Principles (SKILL.md)

| Principle | Description |
|-----------|-------------|
| **11. Source Preservation** | Mandatory local copy of all fetched content before extraction |
| **12. Sub-Session Execution Modes** | Two formal modes: human-executed (prompt written to disk, human launches) vs LLM-executed (LLM launches via task tool). Decision tree included. |
| **13. Generational / Time-Period Dimension** | `#generation/{cohort}` tag, `time_period` field in `cultural_context` entity, search templates for generational queries |

### Updated Principles

| Principle | Change |
|-----------|--------|
| **5. Knowledge Graph + Obsidian Vault** | Added scale-dependent MCP tool selection table (< 50 → direct MCP, 50–500 → skip MCP, write files, 500+ → + batch-import script) |
| **7. Sub-Session Orchestration** | Added two execution modes + formal PM Review Loop with PROCEED/LOOP/PAUSE decision and documentation requirement |

### Phase File Updates

| File | Changes |
|------|---------|
| `02-search-collect.md` | Added generational/cohort dimension to search protocol (line 22) |
| `03-deep-read.md` | Added source preservation requirement as mandatory step with local-copy filename tracking; added to end conditions |
| `04-knowledge-base.md` | Added `#generation/{cohort}` to tag taxonomy; added `time_period` field to entity schema; added scale-dependent MCP guidance section |
| `05-multi-round-analysis.md` | Added generational/cohort gaps as section 4 in Round 4; bumped gap count to 18 |
| `08-sub-session-orchestration.md` | Added execution modes section; replaced verification checklist with formal PM Review Loop; added PM Review Loop gate to cross-phase gates table |

### Cross-Phase Gates

| Gate | Change |
|------|--------|
| PM Review Loop | NEW — after each sub-session, PM must read batch note, spot-check output, update state, log decision |

### Tag Taxonomy

| Tag | Change |
|-----|--------|
| `#generation/{cohort}` | NEW — boomer, gen-x, millennial, gen-z, multi, pre-modern, colonial, post-war, contemporary, not-applicable |

### Entity Schema

| Entity | Field | Change |
|--------|-------|--------|
| `cultural_context` | `time_period` | NEW optional field for generational comparison in scope |
