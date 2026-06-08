# opencode Skill Changelog

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
