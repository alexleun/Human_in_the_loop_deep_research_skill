# opencode Skill Changelog

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
