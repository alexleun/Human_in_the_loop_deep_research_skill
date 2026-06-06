---
name: culture-research
description: "A structured, multi-round workflow for exploratory and qualitative cultural research studies using region-parallel search."
---

# Culture Research Skill v3.1

A structured workflow for **cultural one-off studies** focused on human behavior, social practices, and everyday life. Designed for web-search-based paper collection and qualitative synthesis — no programming, no human-subject data collection, no dashboards.

**v3.0 changes:** Added topic-intent analysis (global vs local scope), active Director role, state synchronization via `project-state.json`, formal cross-phase gates, 09-report-writing phase, paywall access protocol, machine-readable findings index, evidence model refinement (access + evidence tiers), contradiction-identification algorithm, sub-theme filter for matrix, and comprehensive truncation/encoding safeguards. Consolidated feedback from 17 sub-sessions on a 46-paper, 6-region project.

**v3.1 changes:** Clarified sub-session execution model with two formal modes (human-executed and LLM-executed). Added source preservation requirement (save local copies of fetched content). Formalized PM review loop between sub-sessions as a cross-phase gate. Added scale-dependent MCP tool selection guidance. Added openspec bridge section (adapted from deep-research skill). Added generational/time-period as first-class dimension in tag taxonomy and entity schema. Consolidated feedback from a 67-paper, 8-region gift-giving project.

---

## When to Use This Skill

- Study is exploratory / qualitative / cultural — not quantitative or experimental
- Primary sources are **published papers and professor-authored study reports** found via web search
- Output is a **synthesis document + knowledge graph + Obsidian vault** — not a dashboard or app
- Research question is about **human behavior, cultural practices, or daily life patterns**
- Goal includes **generating novel research directions** from cross-paper synthesis

---

## Core Point of View

### 0. Topic-Intent Analysis (NEW in v3.0)

Before any search, determine whether the research question is **global** or **local**:

- **Global scope:** Asking about human behavior across cultures (e.g., "How does daily time allocation vary across cultures?"). Requires region-parallel search.
- **Local scope:** Asking about a specific region/culture (e.g., "How do Japanese office workers manage work-life boundaries?"). Requires depth-first search within that region.

The skill works for both — regions, search templates, and analysis dimensions adjust accordingly. Document the scope decision in the explore phase.

### 1. Region-Parallel Search, Not Keyword-Only Search

Cultural behavior is studied differently across academic traditions. A single English keyword search will miss Chinese sociology, Japanese ethnography, and French anthropology. **Search must be organized by geographic region, each with tailored queries and sources.**

### 2. Deep Reading Before Abstraction

Do not extract entities or build graphs from papers you have not read carefully. Each paper gets a **critical appraisal** (methodology quality, cultural positioning, evidence strength, verbatim key quotes) before any knowledge base entry. This prevents propagating shallow or misinterpreted findings.

### 3. Analysis Must Be Multi-Round and Sequential

One pass of analysis cannot surface deep patterns. The workflow uses **five sequential rounds**, each building on the previous:
1. Thematic categorization (what behaviors are studied?)
2. Cross-cultural comparison (how do behaviors differ by region?)
3. Contradiction deep-dive (where do findings disagree and why?)
4. Gap mapping (what is not studied and who is not represented?)
5. Research question generation (what new studies would fill the gaps?)

### 4. Iteration Checkpoint Before Final Output

After all five rounds, the workflow pauses for a **review checkpoint**. Weak links, missing dimensions, and insufficiently grounded questions are identified. If needed, earlier rounds are revisited. The synthesis document is written only after the checkpoint passes.

### 5. Knowledge Graph + Obsidian Vault as Dual Output

The MCP knowledge graph tool provides structured query and persistence. Simultaneously, all entities, relations, and analysis outputs are written as **Obsidian-compatible markdown** (`#tag`, `[[wikilink]]`, YAML frontmatter). The user opens the `knowledge-base/` folder as an Obsidian vault and immediately sees the graph view — no plugins or configuration needed.

**Scale-dependent tool selection (NEW in v3.1):** The MCP `create_entities` and `create_relations` tools are impractical for large knowledge bases (449 entities → hundreds of MCP tool calls). Use this guidance:

| Entity Count | Recommended Approach |
|---|---|
| < 50 | Use MCP tools directly (`create_entities`, `create_relations`) |
| 50 – 500 | Write markdown files to disk + produce `findings-index.json`. Skip MCP graph tools for bulk import. Use `relations.json` as the machine-readable graph. |
| 500+ | Same as 50–500. Additionally, provide a Python/PowerShell batch-import script for any downstream graph database. |

### 6. Source Grounding (Anti-Hallucination)

Every factual output must cite **exact quoted text** from the source. Paraphrasing introduces hallucination risk. Each paper's metadata includes the search query that found it, the URL, and the professor's institutional affiliation.

### 7. Sub-Session Orchestration (NEW in v2.0, Refined in v3.1)

For projects with >20 papers, split work into **sub-sessions**, each with tight scope, explicit end conditions, and batch notes. The main session is the **project manager** — it creates prompts, verifies outputs, and tracks state.

**Two execution modes (NEW in v3.1):**
- **Human-executed mode:** LLM writes prompt to `sub-sessions/SS{n}-*.md`, human reads and approves, human copies prompt into new LLM session
- **LLM-executed mode:** LLM builds prompt internally and launches sub-agent via `task` tool, main session verifies output, human is informed

Choose based on complexity. See Principle 12 for the decision tree.

**PM Review Loop (NEW in v3.1):** After each sub-session returns, the PM must:
1. Read the batch note / Director Observations
2. Spot-check 1-2 output files
3. Decide: PROCEED → next sub-session / LOOP → re-run with corrections / PAUSE → surface to human
4. Document the decision in `skill-evolution-log.md`
5. Update `project-state.json`
6. Save sub-session feedback to `messages/SS{n}-to-management.md`

Without this loop, sub-sessions proceed without quality verification until the cross-appraisal check, which is too late for course correction.

### 8. State Synchronization & Cross-Phase Gates (NEW in v3.0)

Sub-sessions no longer trust static prompt descriptions. A `project-state.json` in the project root tracks current deliverable paths, entity counts, and completion status. Cross-phase gates (e.g., cross-appraisal consistency check) produce accountable artifacts that downstream phases can reference.

### 9. Active Director Role (NEW in v3.0)

No longer a placeholder. The Director is a dedicated sub-session (or part of the Project Manager) that:
- Aggregates Director Observations from all sub-sessions
- Identifies methodology patterns and quality variance across appraisals
- Proposes skill updates based on project experience
- Runs the cross-appraisal consistency check
- Maintains the skill evolution log

### 10. Evidence Model: Dual Access + Evidence Tiers (NEW in v3.0)

Replace the single `evidence/` tag with two orthogonal fields:
- **`access/`** — `full-text`, `abstract-only`, `metadata-only` (how we accessed it)
- **`evidence/`** — `high`, `medium`, `low` (confidence in the claim, independent of access)

This allows downstream rounds to differentiate "high-confidence claim from abstract-only paper" from "speculative claim from full-text paper."

### 11. Source Preservation (NEW in v3.1)

After fetching any paper content (full-text, abstract, or metadata), save a local copy before extracting findings:
- Full-text PDF → `papers/raw/{paper-id}.pdf`
- Abstract HTML page → `papers/raw/{paper-id}-abstract.html`
- Google Scholar page → `papers/raw/{paper-id}-gs-abstract.html`

Without local copies, findings become unrecoverable if URLs change or go offline. This is a **mandatory** step, not optional.

### 12. Sub-Session Execution Modes (NEW in v3.1)

Sub-sessions can execute in two modes. Choose before launching:

| Mode | Prompt Creation | Who Launches | Best For |
|---|---|---|---|
| **Human-executed** | LLM writes prompt to `sub-sessions/SS{n}-*.md` | Human reads, approves, copies into new session | Complex tasks, first-time users, calibration runs |
| **LLM-executed** | LLM builds prompt internally, launches via `task` tool | Main session LLM launches directly | Routine tasks, experienced users, speed |

Decision tree:
1. Is the task complex or unfamiliar? → **Human-executed**
2. Is this a calibration run (first region batch)? → **Human-executed**
3. Is the task routine and well-understood? → **LLM-executed**
4. Does the human want to review before execution? → **Human-executed**

Both modes produce the same output. The difference is the review/approval step before execution. In LLM-executed mode, the PM must still verify output before proceeding (see PM Review Loop below).

### 13. Generational / Time-Period Dimension (NEW in v3.1)

Research questions involving generational comparison or historical change require `time_period` / `generation` as a first-class dimension:

- **Tag taxonomy addition:** `#generation/{cohort}` — boomer, gen-x, millennial, gen-z, multi, pre-modern, colonial, post-war, contemporary
- **Entity schema addition:** `cultural_context` entity gains an optional `time_period` field (e.g., `2010s`, `post-2000`, `pre-industrial`)
- **Search templates:** Add `"generational OR cohort OR longitudinal time-use"` to region query templates when generational comparison is in scope
- **Round 4 addition:** Generational coverage gaps must be assessed alongside other dimensions

---

## Workflow Overview

```
Topic-Intent Analysis (global vs local)
       │
Explore ──→ Search Design ──→ Region Searches ──→ Unified Roster ──→ Deep Reading
                                       (parallel sub-sessions)    (1 SS per region)
                                                                       │
                                                                       ▼
                         Knowledge Base ──→ Entities + Relations + findings-index.json
                         (SS7 entities,     (SS8 relations)
                          SS8 relations)
                                                                       │
                                                                       ▼
                ┌── Round 1: Thematic Categorization (SS9)
                │── Round 2: Cross-Cultural Comparison (SS10)
                │── Round 3: Contradiction Deep-Dive (SS11)
                │── Round 4: Gap & Blind Spot Mapping (SS12)
                │── Round 5: Research Question Generation (SS13)
                │
  Cross-Phase Gates ──→ Cross-Appraisal Consistency Check
                │       Director Observations Aggregation
                │
 Iteration Checkpoint ←─┘ (SS14)
       │
       ▼ (if weak links, loop back)
  Synthesis (SS15)
       │
       ▼
  Report Writing (SS16+) — optional: science article, research brief, slide deck
       │
       ▼
  Skill Evolution (SS17+) — retrospective, skill updates
```

---

## Phase Router

| Current Task | Load This File |
|---|---|
| Scoping topic, topic-intent analysis, discussing with human | `01-explore.md` |
| Designing search strategy, executing region-parallel collection | `02-search-collect.md` |
| Per-paper deep reading and critical appraisal | `03-deep-read.md` |
| Building knowledge graph entities, relations, Obsidian vault | `04-knowledge-base.md` |
| Running 5-round iterative analysis (thematic → comparison → contradiction → gaps → questions) | `05-multi-round-analysis.md` |
| Review checkpoint, identifying weak links, looping back | `06-checkpoint.md` |
| Writing final synthesis document | `07-synthesis.md` |
| **Multi-session project: writing sub-session prompts, verifying outputs, tracking state** | **`08-sub-session-orchestration.md`** |
| **Writing science article, research brief, or other communication output** | **`09-report-writing.md`** |

---

## End-Conditions Discipline

Every phase and every sub-session must define its **end conditions** as a checklist, not a description:

```markdown
## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ [Specific deliverable exists at specific path]
2. ✅ [Quality criterion met]
3. ✅ [Coverage criterion met]
4. ✅ [Format criterion met]
5. ✅ [Batch note appended]
```

Without end-conditions, sub-sessions exit prematurely or drift. With end-conditions, the sub-session knows when it is done and the project manager can verify completion objectively.

---

## Paywall & Access Protocol (NEW in v3.0)

Many academic papers are paywalled. Follow this priority protocol:

1. **Priority 1:** Check the DOI landing page for open-access or abstract text
2. **Priority 2:** If landing page blocks (403/cookie-wall), try **PubMed abstract** if indexed (requires PMID)
3. **Priority 3:** Search **Google Scholar** with exact title and author — GS abstracts are often more detailed than publisher abstracts and include cited-by counts
4. **Priority 4:** Use the **search-log abstract** (from `papers/raw/search-log-{region}.md`)
5. **Priority 5:** If all fail, the `evidence_status` is `no-abstract-available`

For `abstract-only` papers:
- Mark all findings with `[inferred from abstract — full text not accessed]`
- The appraisal can still be completed, but every finding must carry the `[inferred from abstract]` marker
- Author's limitations section: `[Cannot be assessed from abstract; full text not accessed]`
- Note in batch note: "X papers were paywalled; finding extraction is from abstracts only"

An `abstract-only` paper typically contributes 2–4 directional claims (no effect sizes, no subgroup analysis, no methodological detail). A `full-text` paper typically contributes 6–15 claims with supporting detail. Weight accordingly in synthesis.

---

## File Truncation Safeguard (NEW in v3.0)

All file reads may be capped at ~50KB by the `read` tool. After reading any file:

1. Check for truncation markers: `...truncated...` or `"Full output saved to..."`
2. If truncated, read the remainder with `offset=N` parameter
3. **Batch notes and open questions at the end of each file are critical inputs** — always verify they are captured
4. For open-access papers particularly: fetch in 2–3 offset segments to guarantee the Limitations section is captured (it is always >80% through the paper)

This safeguard applies to ALL phases: deep-read, entity extraction, relations, analysis rounds, checkpoint, synthesis, and report writing.

---

## Windows Encoding & Non-ASCII Filenames (NEW in v3.0)

Windows cmd/PowerShell treats non-ASCII characters in filenames inconsistently. `ï`, `é`, `ü`, `ñ`, `ç` are common in author surnames.

**Detection:** If a `read` call fails with "PathNotFound" but `dir /b` shows the file exists, the filename likely contains a non-ASCII character.

**Workaround:** Use `cmd /c copy` with a wildcard (`?` in place of the special character) to copy to a temp path, then `read` the copy.

**Recommended:** Before each phase that reads many files, run a `_check_encoding.ps1` script that:
1. Detects files with non-ASCII chars in their names
2. Renames them with ASCII-only equivalents (e.g., `Saïdi` → `Saidi`)
3. Records the original-to-mapped mapping in `_filename_map.json`

---

## Cross-Phase Gates (NEW in v3.0)

These verification steps happen BETWEEN phases and produce accountable artifacts:

| Gate | After Phase | Artifact | Run By |
|---|---|---|---|
| Cross-Appraisal Consistency Check | Deep Reading | `papers/appraisals/_cross-appraisal-check.md` | Director / PM |
| Cross-Region Relation Consistency | Knowledge Base | Check findings-index.json covers all papers | PM |
| Sub-Theme Viability Filter | Round 1 | Decision: which sub-themes become matrix rows | Director |
| Round Output Completeness | Each Round | Verify prior round's end conditions met | Sub-agent (checked by PM) |
| Synthesis Input Coherence | Checkpoint | `checkpoint-review.md` | Checkpoint sub-agent |
| Skill Evolution | Archive | `skill-evolution-log.md` | Director / PM |
| PM Review Loop (NEW in v3.1) | Each Sub-Session | Batch note read + output spot-check + decision logged | PM |
| Source Preservation (NEW in v3.1) | Each Fetch | Local copy saved to `papers/raw/` | Sub-agent |

---

## Openspec Bridge (NEW in v3.1)

Research outputs (papers, findings, design decisions) can seed openspec changes for downstream implementation (databases, dashboards, websites). Copy forward these artifacts:

| From Research | To Openspec Change |
|---|---|
| `explore/scope-definition.md` | `proposal.md` — research questions, scope |
| `papers/search-protocol.md` + `coverage-report.md` | `design.md` — data sources section |
| `knowledge-base/findings-index.json` | `specs/<capability>/spec.md` — requirements |
| Design decisions from explore phase | `design.md` — architecture decisions |
| `skill-evolution-log.md` | Lessons for next change's `design.md` |

**What NOT to carry forward:**
- Do NOT copy raw appraisal files — link to them from `papers/`
- Do NOT re-debate settled design decisions — reference them
- Do NOT copy the entire knowledge base — link from the openspec change

---

## File Persistence

```
{project_root}/
├── papers/
│   ├── search-protocol.md
│   ├── raw/                      # search logs per region
│   ├── meta/                     # paper metadata (optional)
│   ├── appraisals/               # one .appraisal.md per paper
│   ├── appraisals/_cross-appraisal-check.md   # (NEW) consistency artifact
│   ├── unified-candidate-list.md # final paper roster
│   └── coverage-report.md        # (optional)
├── knowledge-base/
│   ├── entities/                 # Obsidian-compatible entity notes
│   ├── findings-index.json       # (NEW) machine-readable findings index
│   ├── relations.json            # structured relations
│   ├── summary.md                # human-readable KB overview
│   ├── analysis/                 # round1...round5 outputs + checkpoint
│   ├── synthesis.md              # final synthesis
│   └── article/                  # (NEW) report-writing outputs
│       ├── final-article.md
│       └── final-article.html
├── sub-sessions/
│   ├── README.md
│   └── SS_TEMPLATE.md
├── messages/                     # (NEW) sub-session feedback to management
│   └── SS{n}-to-management.md
├── project-state.json            # (NEW) state synchronization file
└── skill-evolution-log.md        # (NEW) accumulated skill improvement records
```

---

## Batch Note Pattern

Every sub-session appends a `# SS{n} Batch Note` section to its primary output. This section documents:
- What was produced (count by type)
- What evidence_status / access distribution was achieved
- Open issues for the project manager
- Papers to re-evaluate
- Honest assessment of quality

The main session reads the batch note first to decide whether to proceed, loop, or intervene.

## Tag Taxonomy (Extended in v3.1)

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

No ad-hoc tags. If a tag doesn't fit a category, do not create one.

## Entity Schema (Extended in v3.1)

The `cultural_context` entity gains an optional `time_period` field:

```yaml
---
type: cultural_context
id: japan_tokyo_urban
time_period: 2010s       # (NEW) optional: pre-modern, colonial, post-war, 2000s, 2010s, 2020s, multi
tags:
  - region/east-asia
  - population/urban
---
```

When the research question involves generational comparison, every cultural_context should include a `time_period` field. When the question is purely cross-sectional, it can be omitted.

## Director Observations (NEW in v3.0 — Active, Not Placeholder)

Every sub-session includes a `## Director Observations` section in its batch note. The Director (a dedicated sub-session or PM role) aggregates these into quarterly observations:

1. **Quality variance** — Are sub-session outputs meeting the same quality bar?
2. **Scope discipline** — Are sub-sessions staying within boundaries?
3. **Prompt clarity** — What parts of the prompts need improvement?
4. **Coordination overhead** — How much attention does each SS require?
5. **Generalizable lessons** — What should update the skill?

The Director produces a `knowledge-base/director-report-{round}.md` after each major phase.
