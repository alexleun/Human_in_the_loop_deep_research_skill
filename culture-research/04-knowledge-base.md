# Phase 4: Knowledge Base Construction

**Purpose:** Extract structured entities and relations from appraised papers, persist in MCP knowledge graph + Obsidian-compatible markdown vault.

## 4a. Entity Extraction

Create entities for each paper following this schema:

| Entity Type | Fields | Example |
|---|---|---|
| `researcher` | name, institution, discipline, region, key publications | `Kim_2023_SeoulWorkRoutines` |
| `cultural_context` | country/region, urban/rural, socioeconomic setting, time period | `urban_South_Korea_2020s` |
| `method` | study type, data collection, duration, sample size, approach | `time_diary_survey_7day` |
| `behavior_domain` | domain, sub-themes | `work` with sub-themes: `hours`, `boundary`, `remote` |
| `finding` | key result (verbatim), domain, cultural context, evidence strength, theory relation | See below |

**Every entity** is written to:
1. MCP knowledge graph (via `create_entities` tool)
2. Individual markdown file at `knowledge-base/entities/` with:

```yaml
---
type: finding
tags:
  - behavior/sleep
  - region/east-asia
  - evidence/medium
sources:
  - "[[Kim_2023_SleepPatterns]]"
---
# Sleep deprivation among urban Korean workers
{verbatim quote}
```

## 4b. Relation Mapping

Create relations between entities:

| Relation | From | To | Meaning |
|---|---|---|---|
| `observed_by` | finding | researcher | who found this |
| `observed_in` | finding | cultural_context | where this was observed |
| `describes` | finding | behavior_domain | what behavior this is about |
| `produced_by` | finding | method | how this was studied |
| `supports` | finding | finding | agreement across papers |
| `contradicts` | finding | finding | disagreement across papers |
| `extends` | finding | finding | builds on prior finding |

Write relations to MCP knowledge graph and produce `knowledge-base/relations.json`.

## 4c. Summary Document

Produce `knowledge-base/summary.md` with:
- Entity count per type
- Relation count per type
- Most-connected entities (hub analysis)
- Coverage statistics (which behavior domains and regions have the most entities)
- Obsidian `#tag` and `[[wikilink]]` formatting throughout

## Obsidian Vault Conventions

All markdown files under `knowledge-base/` and `papers/appraisals/` follow:

**Tags:** `#region/{region}`, `#discipline/{name}`, `#behavior/{domain}`, `#method/{type}`, `#population/{group}`, `#evidence/{level}`, `#status/{value}`

**Wikilinks:** `[[PaperAuthor_Year_ShortTitle]]`, `[[researcher/{name}]]`, `[[behavior/{domain}/{sub-theme}]]`, `[[finding/{id}]]`

**Frontmatter:** every entity note has type, tags, and sources.
