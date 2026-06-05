# Phase 4: Knowledge Base Construction

**Purpose:** Extract structured entities and relations from appraised papers, persist in MCP knowledge graph + Obsidian-compatible markdown vault.

**Execution pattern:** For >20 appraised papers, run as sub-sessions (SS7 = entities, SS8 = relations). For ≤20 papers, can run in one session.

---

## Before Starting: Encoding Check (NEW in v3.0)

Run `_check_encoding.ps1` to detect files with non-ASCII characters in their names. Rename with ASCII-only equivalents and record the mapping in `_filename_map.json`. This prevents "PathNotFound" errors during entity extraction.

---

## Scale-Dependent MCP Guidance (NEW in v3.1)

The MCP `create_entities` and `create_relations` tools are designed for small graphs (< 50 nodes). For larger projects:

- **< 50 entities:** Use MCP tools directly
- **50 – 500 entities:** Write markdown files to disk + produce `findings-index.json` + `relations.json`. Skip MCP graph tools. The JSON files serve as the machine-readable graph.
- **500+ entities:** Same as above. Additionally, provide a batch-import script for downstream graph databases.

The tag taxonomy, entity schema, and `relations.json` format remain the same regardless of tool choice.

---

## 4a. Entity Extraction

Create entities for each paper following this schema:

| Entity Type | Fields | Example |
|---|---|---|
| `researcher` | name, institution, discipline, region, key publications | `Kim_2023_SeoulWorkRoutines` |
| `cultural_context` | country/region, urban/rural, socioeconomic setting, time_period (optional, add when generational comparison is in scope) | See granularity rules below |
| `method` | study type, data collection, duration, sample size, approach | `time_diary_survey_7day` |
| `behavior_domain` | domain, sub-themes | `work` with sub-themes |
| `finding` | key result (verbatim), domain, cultural context, evidence strength, access type, theory relation | See template |

**Every entity** is written to:
1. Individual markdown file at `knowledge-base/entities/{type}/{name}.md` with YAML frontmatter
2. The MCP knowledge graph (via `create_entities` tool)

### File Format (Obsidian-compatible)

```yaml
---
type: finding
id: {paper_id}_F{index}
tags:
  - behavior/{domain}
  - region/{region}
  - evidence/{level}
  - access/{type}         # (NEW) full-text, abstract-only, metadata-only
sources:
  - "[[{PaperID}]]"
created: YYYY-MM-DD
---
```

### Cultural Context Granularity (NEW in v3.0)

Use these rules consistently:
- **For single-site ethnographies:** `country_city_site` (e.g., `egypt_cairo_doqi`)
- **For multi-site ethnographies:** `country_city_site` per site
- **For quantitative studies with national samples:** `country_national` (e.g., `japan_national`)
- **For multi-country comparisons:** `region_scale` (e.g., `east_asia_multi`, `eu_multi_country`)

This ensures consistent granularity across different sub-agents.

### Researcher Naming Rules (NEW in v3.0)

- For 1-author papers where only surname is given: use `Surname` as entity `id:`
- For multi-author papers: use `Surname_Firstname` if available, or `Surname` alone
- Surnames with diacritics (Saïdi, López) should be preserved in the entity `id:` field; for filenames, use ASCII-only transliteration (e.g., `Saidi`)

---

## 4b. Tag Taxonomy (Strict — REFINED in v3.0)

Use ONLY these tag categories:

- `#region/{region}` — east-asia, south-asia, southeast-asia, europe, americas, middle-east, africa, oceania, global
- `#discipline/{name}` — anthropology, sociology, psychology, urban-studies, public-health, economics, history
- `#behavior/{domain}` — work, family, leisure, sleep, mobility, eating, hygiene, social, religious, care
- `#method/{type}` — ethnography, time-diary, survey, daily-diary, mixed, review
- `#population/{group}` — urban, rural, students, elderly, working-age, mixed, children, disabled, indigenous, migrants
- `#generation/{cohort}` (NEW in v3.1) — boomer, gen-x, millennial, gen-z, multi, pre-modern, colonial, post-war, contemporary, not-applicable
- `#evidence/{level}` — high, medium, low
- `#access/{type}` — full-text, abstract-only, metadata-only
- `#status/{value}` — contradicted, supported, gap

**No ad-hoc tags.** If a tag doesn't fit a category, do not create one.

**Evidence model (REFINED in v3.0):** Use TWO orthogonal fields:
- `#access/{type}` — how we accessed the source (full-text, abstract-only, metadata-only)
- `#evidence/{level}` — confidence in the claim itself (high/medium/low)
This replaces the single `evidence/` tag that made all findings indistinguishable.

---

## 4c. Wikilink Conventions

- `[[PaperID]]` — links to the paper appraisal file
- `[[researcher/{Name}]]` — links to researcher entity
- `[[behavior_domain/{Domain}]]` — links to behavior domain entity
- `[[cultural_context/{Context}]]` — links to cultural context entity
- `[[method/{Method}]]` — links to method entity
- `[[finding/{ID}]]` — links to a specific finding

---

## 4d. Finding `_index.md` (REFINED in v3.0)

The `_index.md` must include these explicit sections:

1. Entity counts by type (required)
2. Paper-to-finding mapping table with wikilinks (required)
3. Regional breakdown of cultural contexts (recommended)
4. Behavior domain overview (recommended)
5. Open issues / anomalies encountered (required)
6. SS{n} Batch Note (required)
7. Director Observations (required)

---

## 4e. findings-index.json (NEW in v3.0)

Alongside markdown entity files, produce `knowledge-base/findings-index.json` — a machine-readable index with one entry per finding:

```json
{
  "id": "finding_id",
  "source_paper": "PaperID",
  "researchers": ["Surname_Firstname"],
  "cultural_context": "country_city_site",
  "method": "method_type",
  "behavior_domains": ["work", "family"],
  "quote": "Exact verbatim quote...",
  "tags": ["evidence/medium", "access/abstract-only", "region/east-asia"]
}
```

This file serves as the programmatic input for SS8 (relations) and all analysis rounds, eliminating the need to re-read all 92 finding files manually.

---

## 4f. Relation Mapping (REFINED in v3.0)

| Relation | From | To | Meaning | Cardinality (NEW) |
|---|---|---|---|---|
| `observed_by` | finding | researcher | who found this | 1 per author |
| `observed_in` | finding | cultural_context | where observed | 1 per context |
| `describes` | finding | behavior_domain | what behavior | 1 per domain tag |
| `produced_by` | finding | method | how studied | 1 per method |
| `supports` | finding | finding | agreement | See criteria below |
| `contradicts` | finding | finding | disagreement | Defer subtle to Round 3 |
| `extends` | finding | finding | builds on | See criteria below |

**Cardinality rules (NEW):**
- `observed_by`: Create ONE relation per author (not one per paper). A 3-author paper produces 3 relations.
- `describes`: Create ONE relation per behavior domain tag. A finding tagged `work` + `family` produces 2 relations.
- `source_paper` field is REQUIRED on every relation: the PaperID of the appraisal file that produced this finding.

**Cross-paper relation criteria (NEW):**
- `extends`: Same first-author AND same behavior domain AND chronological ordering
- `supports`: Different papers, same behavior domain AND same region AND convergent conclusion
- `contradicts`: Same behavior domain AND same region AND opposite conclusion

---

## 4g. Summary Document

Produce `knowledge-base/summary.md` with:
- Entity count per type
- Relation count per type
- Most-connected entities (hub analysis)
- Coverage statistics (which behavior domains and regions have the most entities)
- Access distribution (how many findings are full-text vs abstract-only)
- Obsidian `#tag` and `[[wikilink]]` formatting throughout

---

## 4h. Validation Step (NEW in v3.0)

After writing all files, run validation:
1. Every finding has exactly 4 mechanical relations (observed_by, observed_in, describes, produced_by)
2. Every relation has non-empty `evidence_quote` and `source_paper`
3. Total cross-paper relations ≥ 5
4. Every entity file has tags from the approved taxonomy only
5. All `[[wikilink]]` references resolve to existing files

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ At least one entity file exists per entity type (5 entity types total)
2. ✅ Every appraisal file has: 1 researcher, 1 cultural_context, 1 method, 1 behavior_domain, at least 2 finding entities
3. ✅ Every entity file uses YAML frontmatter with the schema above
4. ✅ Every entity file has tags from the approved taxonomy only
5. ✅ Every entity file has working `[[wikilink]]` references
6. ✅ Every finding entity includes `access/` tag AND `evidence/` tag (dual model)
7. ✅ `knowledge-base/findings-index.json` exists with all findings (machine-readable)
8. ✅ `knowledge-base/relations.json` exists with all 4 mechanical relations per finding + cross-paper relations + validation passed
9. ✅ `knowledge-base/summary.md` exists with entity/relation statistics, hub analysis, access distribution
10. ✅ `_index.md` has all required sections (counts, mapping table, regional breakdown, open issues, batch note, Director Observations)
11. ✅ Validation step passed (relations complete, wikilinks resolve, tags conform)

---

## Verbatim Quote Rule (CRITICAL)

Every finding entity must include a verbatim quote pulled directly from an appraisal file. Never paraphrase. The appraisal file is the single source of truth for content; entities are pointers to that content.

---

## Quote Extraction Strategy (NEW in v3.0)

1. For each paper, read the appraisal's "Key findings" section first
2. Select the 2 most impactful findings
3. For each, find the single sentence or short paragraph that best encapsulates it
4. Extract verbatim — do not paraphrase or truncate
5. Include the page/paragraph reference if available
6. Quote should be 1-3 sentences, not exceeding 5% of appraisal length

---

## What NOT to Do

- Do NOT run analysis rounds in this phase — that is Phase 5
- Do NOT create the synthesis document
- Do NOT use ad-hoc tags outside the approved taxonomy
- Do NOT fabricate verbatim quotes
- Do NOT skip the relations phase
- Do NOT skip the validation step
