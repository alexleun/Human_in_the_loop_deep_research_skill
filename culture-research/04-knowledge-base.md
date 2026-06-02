# Phase 4: Knowledge Base Construction

**Purpose:** Extract structured entities and relations from appraised papers, persist in MCP knowledge graph + Obsidian-compatible markdown vault.

**Execution pattern:** For >20 appraised papers, run as sub-sessions (SS7 = entities, SS8 = relations). For ≤20 papers, can run in one session.

---

## 4a. Entity Extraction

Create entities for each paper following this schema:

| Entity Type | Fields | Example |
|---|---|---|
| `researcher` | name, institution, discipline, region, key publications | `Kim_2023_SeoulWorkRoutines` |
| `cultural_context` | country/region, urban/rural, socioeconomic setting, time period | `urban_South_Korea_2020s` |
| `method` | study type, data collection, duration, sample size, approach | `time_diary_survey_7day` |
| `behavior_domain` | domain, sub-themes | `work` with sub-themes: `hours`, `boundary`, `remote` |
| `finding` | key result (verbatim), domain, cultural context, evidence strength, theory relation | See template |

**Every entity** is written to:
1. MCP knowledge graph (via `create_entities` tool)
2. Individual markdown file at `knowledge-base/entities/{type}/{name}.md` with YAML frontmatter

### File Format (Obsidian-compatible)

```yaml
---
type: finding
id: {paper_id}_F{index}
tags:
  - behavior/{domain}
  - region/{region}
  - evidence/{level}
sources:
  - "[[{PaperID}]]"
created: YYYY-MM-DD
---

# Finding: {short title}

## Verbatim Quote
"{exact verbatim quote from the appraisal file}"

## Behavior Domain
[[behavior_domain/{domain}]]

## Cultural Context
[[cultural_context/{context}]]

## Method
[[method/{method}]]

## Researchers
[[researcher/{Name}]]

## Evidence Strength
{LEVEL} (justified in appraisal)

## Source Paper
[[{PaperID}]] — see `papers/appraisals/{PaperID}.appraisal.md`
```

---

## 4b. Tag Taxonomy (Strict)

Use ONLY these tag categories:

- `#region/{region}` — east-asia, south-asia, southeast-asia, europe, americas, middle-east, africa, oceania
- `#discipline/{name}` — anthropology, sociology, psychology, urban-studies, public-health, economics, history
- `#behavior/{domain}` — work, family, leisure, sleep, mobility, eating, hygiene, social, religious, care
- `#method/{type}` — ethnography, time-diary, survey, daily-diary, mixed, review
- `#population/{group}` — urban, rural, students, elderly, working-age, mixed
- `#evidence/{level}` — high, medium, low
- `#status/{value}` — contradicted, supported, gap

**No ad-hoc tags.** If a tag doesn't fit a category, do not create one.

---

## 4c. Wikilink Conventions

- `[[PaperID]]` — links to the paper appraisal file
- `[[researcher/{Name}]]` — links to researcher entity
- `[[behavior_domain/{Domain}]]` — links to behavior domain entity
- `[[cultural_context/{Context}]]` — links to cultural context entity
- `[[method/{Method}]]` — links to method entity
- `[[finding/{ID}]]` — links to a specific finding

---

## 4d. Relation Mapping

| Relation | From | To | Meaning |
|---|---|---|---|
| `observed_by` | finding | researcher | who found this |
| `observed_in` | finding | cultural_context | where this was observed |
| `describes` | finding | behavior_domain | what behavior this is about |
| `produced_by` | finding | method | how this was studied |
| `supports` | finding | finding | agreement across papers |
| `contradicts` | finding | finding | disagreement across papers |
| `extends` | finding | finding | builds on prior finding |

The first 4 relations are mechanical (one per finding). The last 3 require cross-paper analysis (defer subtle contradictions to Round 3).

---

## 4e. Summary Document

Produce `knowledge-base/summary.md` with:
- Entity count per type
- Relation count per type
- Most-connected entities (hub analysis)
- Coverage statistics (which behavior domains and regions have the most entities)
- Obsidian `#tag` and `[[wikilink]]` formatting throughout

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ At least one entity file exists per entity type (5 entity types total)
2. ✅ Every appraisal file has at least:
   - 1 researcher entity extracted
   - 1 cultural_context entity extracted
   - 1 method entity extracted
   - 1 behavior_domain entity extracted
   - At least 2 finding entities extracted
3. ✅ Every entity file uses YAML frontmatter with the schema above
4. ✅ Every entity file has tags from the approved taxonomy only
5. ✅ Every entity file has working `[[wikilink]]` references
6. ✅ Every finding entity includes a verbatim quote pulled from an appraisal file
7. ✅ `knowledge-base/relations.json` exists with all 4 mechanical relations per finding + cross-paper relations
8. ✅ `knowledge-base/summary.md` exists with entity/relation statistics, hub analysis, and Obsidian formatting
9. ✅ `_index.md` or batch note documents entity counts, papers that produced the most entities, open issues

---

## Verbatim Quote Rule (CRITICAL)

Every finding entity must include a verbatim quote pulled directly from an appraisal file. Never paraphrase. The appraisal file is the single source of truth for content; entities are pointers to that content.

---

## Paywall & Abstract-Only Discipline (NEW in v2.0)

For findings extracted from `evidence_status: abstract-only` papers:
- Mark the finding with `#evidence/low` tag
- Note in the finding's body: `[inferred from abstract]`
- The downstream synthesis must weight these findings lower
- Do NOT create cross-paper relations to/from these findings unless the relation is also inferable from the abstract

---

## What NOT to Do

- Do NOT run analysis rounds in this phase — that is Phase 5
- Do NOT create the synthesis document
- Do NOT use ad-hoc tags outside the approved taxonomy
- Do NOT fabricate verbatim quotes
- Do NOT skip the relations phase
