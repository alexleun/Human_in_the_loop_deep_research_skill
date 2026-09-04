# opencode Skill Changelog

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
