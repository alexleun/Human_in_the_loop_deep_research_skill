# opencode Skill Changelog

## culture-research v3.0 — 2026-06-05

Consolidated feedback from 17 sub-sessions on a 46-paper, 6-region cultural study of human daily behavior. Every phase file was rewritten to fix weaknesses identified in practice.

### New Files

| File | Purpose |
|---|---|
| `09-report-writing.md` | Science communication phase: science magazine article, research brief, executive summary, slide deck. Includes style calibration, sub-agent chapter writing, HTML export with CSS, word count enforcement. |

### Breaking Changes

- **Dual evidence model**: `#evidence/{level}` tag is now accompanied by `#access/{type}` (full-text, abstract-only, metadata-only). The single `evidence/` tag previously made all findings indistinguishable. Downstream analysis rounds must use both fields.
- **findings-index.json required**: SS7 must now produce a machine-readable index alongside markdown entity files. SS8 and all analysis rounds use this instead of re-reading 92 finding files manually.
- **Cross-appraisal consistency artifact required**: `papers/appraisals/_cross-appraisal-check.md` must exist before deep-read phase is marked complete.
- **Director Observations mandatory**: Every sub-session batch note must include a Director Observations section (no longer a placeholder).

### Structural Improvements

| Change | Files Affected | Impact |
|---|---|---|
| Topic-intent analysis (global vs local scope) | `01-explore.md`, `SKILL.md` | Prevents over-designed search for local-scope projects |
| Paywall access protocol (5 priority tiers) | `03-deep-read.md`, `SKILL.md` | Sub-agents now follow deterministic fallback (DOI → PubMed → Google Scholar → search log → no-abstract-available) |
| File truncation safeguard | All 9 phase files | Every read checks for 50KB cap; critical end-of-file content no longer missed |
| Windows encoding & non-ASCII handling | `03-deep-read.md`, `04-knowledge-base.md`, `SKILL.md` | `ï`, `é`, `ü` in filenames no longer cause inaccessible files |
| Search-log cross-check | `03-deep-read.md`, `02-search-collect.md` | DOIs, abstract figures, and affiliations verified independently before inclusion |
| Regional coverage fail-safe | `03-deep-read.md`, `02-search-collect.md` | Low-paper-count regions documented as structural gaps instead of padded |
| Cultural context granularity rules | `04-knowledge-base.md` | Single-site, multi-site, national, and multi-country contexts now have deterministic naming |
| Researcher naming conventions | `04-knowledge-base.md` | Diacritics preserved in entity IDs, ASCII-only in filenames; 1-author vs multi-author rules |
| Relation cardinality rules | `04-knowledge-base.md` | Multi-author: one `observed_by` per author. Multi-domain: one `describes` per tag. |
| Cross-paper relation criteria | `04-knowledge-base.md` | `extends`, `supports`, `contradicts` now have operational definitions |
| Sub-theme derivation method | `05-multi-round-analysis.md` (Round 1) | 3-step inductive procedure with granularity rule (4-8 per domain) replaces undefined "inductively identify" |
| Sub-theme filter for matrix | `05-multi-round-analysis.md` (Round 2) | Only sub-themes with ≥2 regions or ≥3 papers become matrix rows; 294-cell monster avoided |
| Operationalized evidence/agreement/symbols | `05-multi-round-analysis.md` (Round 2) | HIGH/MEDIUM/LOW thresholds defined; consensus/mixed/single-source defined; ✅/⚠️/📊/❓ thresholds defined |
| Contradiction-identification algorithm | `05-multi-round-analysis.md` (Round 3) | Matrix scan → direction flag → entity verification replaces "find contradictions" |
| 3-tier speculation classification | `06-checkpoint.md` | Evidence-derived / gap-derived / speculative (replaces binary "speculative vs not") |
| Loop-actionability rule | `06-checkpoint.md` | "LOOP only if the gap can be closed within the existing paper set" prevents infinite loops |
| `project-state.json` state synchronization | `08-sub-session-orchestration.md` | Sub-sessions read `project-state.json` for current deliverable paths instead of trusting static prompt descriptions |
| Active Director role | `08-sub-session-orchestration.md`, `SKILL.md` | Director Observations now aggregated, methodology patterns tracked, skill evolution log maintained |
| Skill evolution phase | `08-sub-session-orchestration.md` | Post-archive step producing `skill-evolution-log.md` entries |
| `task_id` convention documented | `08-sub-session-orchestration.md` | `task_id` must start with `"ses"` (lowercase) |
| Sequential task reliability | `09-report-writing.md` | Sequential sub-agent execution is the recommended pattern |
| End-condition scripts suggested | `07-synthesis.md` | `verify-wikilinks.ps1`, `check-end-conditions.ps1` patterns provided |

### Bug Fixes

- **Cross-appraisal consistency check**: Specified in v2.0 but had no accountable artifact. Now produces `_cross-appraisal-check.md` with 5-point checklist.
- **`evidence_status: no-abstract-available`**: Added as fourth option. v2.0 only had three statuses; papers with zero accessible text had no valid status.
- **Abstract-only verbatim quote rule**: Clarified that the abstract IS the source; single sentence with 2+ findings can be quoted once and cross-referenced.
- **Professor-led definition**: Clarified that ANY co-author with professorial position qualifies (including senior author). PhD-candidate-led papers with professor senior author count.
- **SS_TEMPLATE.md**: Now includes truncation warning, encoding warning, `project-state.json` reference, and active Director Observations template.

---

## deep-research v2.0 — 2026-06-05

Upgraded with end-conditions discipline, cross-phase gates, state synchronization, and methodological safeguards, drawing on lessons from the culture-research v3.0 upgrade.

### Structural Improvements

| Change | Files Affected | Impact |
|---|---|---|
| End-Conditions Discipline (Principle 15) | All 10 phase files + `SKILL.md` | Every phase now has explicit completion checklist. No more "I think it's done" — each phase has verifiable criteria. |
| Cross-Phase Gates (Principle 16) | `SKILL.md`, `06-web-output.md` | Formalized 7 verification gates between phases (source verification, data validation, code validation, encoding check, parity check, HTML structure, cross-artifact). Phase 6 already had exit gates — now pattern is systematic. |
| File Truncation Safeguard (Principle 17) | `03-collect.md`, `04-analyze.md`, `05-report.md`, `07-review.md`, `SKILL.md` | After every file read, check for 50KB cap. Critical end-of-file content (data tables, references, methodology notes) no longer missed. |
| Non-ASCII Filename Handling (Principle 18) | `03-collect.md`, `SKILL.md` | Source filenames with é, ü, ñ, ç, CJK characters now handled via `_filename_map.json` mapping. Previously worked around but not documented. |
| State Synchronization (Principle 19) | `state-management.md`, `SKILL.md`, all end-conditions | `task_state.json` promoted from optional to recommended. Every phase's end-conditions now include an update step. |
| Skill Evolution Log | `09-archive.md`, `SKILL.md` | Post-archive step producing `skill-evolution-log.md` entries. Turns every completed change into a skill improvement cycle. |

### Files Updated

- `SKILL.md` — 5 new methodology principles (15-19), updated guardrails, cross-phase gates table
- `01-explore.md` — Added end-conditions checklist
- `02-propose.md` — Added end-conditions checklist
- `03-collect.md` — Added end-conditions, truncation safeguard, non-ASCII handling
- `04-analyze.md` — Added end-conditions, truncation safeguard
- `05-report.md` — Added end-conditions, truncation safeguard
- `06-web-output.md` — Added formal end-conditions checklist (previously only had exit gates)
- `07-review.md` — Added end-conditions, truncation safeguard
- `08-iterate.md` — Added end-conditions
- `09-archive.md` — Added end-conditions, skill evolution log reference
- `10-implement.md` — Added end-conditions
- `state-management.md` — Updated to reflect promotion to recommended practice

### Principles Carried Forward from culture-research v3.0

| Principle | culture-research v3.0 | deep-research v2.0 |
|---|---|---|
| End-Conditions Discipline | Every phase has checklist | Every phase has checklist |
| Cross-Phase Gates | Formal verification between phases | Formal verification between phases |
| File Truncation Safeguard | All phases check for 50KB cap | All file-heavy phases check |
| Non-ASCII Filename Handling | `_filename_map.json` pattern | Source collection phase |
| State Synchronization | `project-state.json` | `task_state.json` (existing, promoted) |
| Skill Evolution Log | Post-archive step | Post-archive step |
| Director Observations | Active role accumulating lessons | Not carried forward (deep-research is LLM+human, not sub-session architecture) |
| Dual Evidence Model | `access/` + `evidence/` tags | Already had `data-confidence` + `data-source` — no change needed |
| Paywall Access Protocol | 5-tier fallback | Already had URL verification — expanded with truncation check |
| Topic-Intent Analysis | Global vs local scope | Not applicable (deep-research already works on any topic) |

---

## About the Skills

Both skills are part of the [opencode](https://opencode.ai) ecosystem — structured workflows that LLMs load via the `skill` tool to execute complex, multi-step research tasks within conversational sessions.

- **culture-research**: For qualitative cultural one-off studies. Paper collection, knowledge graph construction, multi-round synthesis, and science communication. Designed for sub-session orchestration across many sessions.
- **deep-research**: For structured deep research on any topic. Data collection, code-first analysis, bilingual web output, and application implementation. Designed for LLM+human collaboration in guided sessions.

Both skills share grounding methodology (anti-hallucination through verbatim source quotes, encoding awareness for CJK content, state synchronization across sessions) but differ in execution patterns and artifact types.
