---
name: culture-research
description: Cultural one-off study workflow: paper collection, deep reading, knowledge graph construction, multi-round iterative analysis, and Obsidian-based knowledge visualization. No programming or human-subject data collection. Designed for sub-session orchestration across many sessions.
license: MIT
metadata:
  version: "2.0"
  files:
    - "01-explore.md"
    - "02-search-collect.md"
    - "03-deep-read.md"
    - "04-knowledge-base.md"
    - "05-multi-round-analysis.md"
    - "06-checkpoint.md"
    - "07-synthesis.md"
    - "08-sub-session-orchestration.md"
---

# Culture Research Skill

A structured workflow for **cultural one-off studies** focused on human behavior, social practices, and everyday life. Designed for web-search-based paper collection and qualitative synthesis — no programming, no human-subject data collection, no dashboards.

**v2.0 changes:** Added sub-session orchestration pattern (file `08`) for projects exceeding single-session capacity. Updated each phase file with explicit end-conditions, paywall-fallback discipline, and batch note requirements.

---

## When to Use This Skill

- Study is exploratory / qualitative / cultural — not quantitative or experimental
- Primary sources are **published papers and professor-authored study reports** found via web search
- Output is a **synthesis document + knowledge graph + Obsidian vault** — not a dashboard or app
- Research question is about **human behavior, cultural practices, or daily life patterns**
- Goal includes **generating novel research directions** from cross-paper synthesis

---

## Core Point of View

This skill is built on several methodological principles developed through practice:

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

The order matters — gaps are meaningful only after you know what exists, contradictions only after you know the patterns.

### 4. Iteration Checkpoint Before Final Output
After all five rounds, the workflow pauses for a **review checkpoint**. Weak links, missing dimensions, and insufficiently grounded questions are identified. If needed, earlier rounds are revisited. The synthesis document is written only after the checkpoint passes.

### 5. Knowledge Graph + Obsidian Vault as Dual Output
The MCP knowledge graph tool provides structured query and persistence. Simultaneously, all entities, relations, and analysis outputs are written as **Obsidian-compatible markdown** (`#tag`, `[[wikilink]]`, YAML frontmatter). The user opens the `knowledge-base/` folder as an Obsidian vault and immediately sees the graph view — no plugins or configuration needed.

### 6. Source Grounding (Anti-Hallucination)
Every factual output must cite **exact quoted text** from the source. Paraphrasing introduces hallucination risk. Each paper's metadata includes the search query that found it, the URL, and the professor's institutional affiliation.

### 7. Sub-Session Orchestration for Multi-Session Projects (NEW in v2.0)
For projects with >20 papers, single-session execution hits context limits. Split work into **sub-sessions**, each with:
- Tight scope (one phase, one batch)
- Explicit **end conditions** (a checklist, not a description)
- A **batch note** appended to outputs for the project manager
- File-persistence to the same project directory across sessions

The main session is the **project manager** — it does not execute paper work, it writes sub-session prompts and verifies outputs. See `08-sub-session-orchestration.md` for details.

---

## Workflow Overview

```
Explore ──→ Search Design ──→ Region Searches (parallel sub-sessions) ──→ Acquisition
                                                                          │
                                                                          ▼
                                       Deep Reading (1 sub-session per region; 1 sub-agent per paper)
                                                                          │
                                                                          ▼
                                           Knowledge Base ──→ Entities + Relations
                                                                          │          └── Obsidian `.md` files
                                                                          ▼
                                                ┌── Round 1: Thematic Categorization
                                                │── Round 2: Cross-Cultural Comparison
                                                │── Round 3: Contradiction Deep-Dive
                                                │── Round 4: Gap & Blind Spot Mapping
                  Iteration Checkpoint ←────────┘── Round 5: Research Question Generation
                       │
                       ▼ (if weak links, loop back to relevant round)
            ┌─ Refine rounds ─┐
            └────→ Synthesis Document
```

**For projects with >20 papers:** Each phase is implemented as a sub-session with explicit end-conditions. See `08-sub-session-orchestration.md`.

---

## Phase Router

| Current Task | Load This File |
|---|---|
| Scoping topic, discussing with human | `01-explore.md` |
| Designing search strategy, executing region-parallel collection | `02-search-collect.md` |
| Per-paper deep reading and critical appraisal | `03-deep-read.md` |
| Building knowledge graph entities, relations, Obsidian vault | `04-knowledge-base.md` |
| Running 5-round iterative analysis (thematic → comparison → contradiction → gaps → questions) | `05-multi-round-analysis.md` |
| Review checkpoint, identifying weak links, looping back | `06-checkpoint.md` |
| Writing final synthesis document | `07-synthesis.md` |
| **Multi-session project: writing sub-session prompts, verifying outputs, tracking tasks** | **`08-sub-session-orchestration.md`** |

---

## End-Conditions Discipline (NEW in v2.0)

Every phase and every sub-session must define its **end conditions** as a checklist, not a description. The end-conditions pattern is:

```markdown
## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ [Specific deliverable exists at specific path]
2. ✅ [Quality criterion met, e.g., "every file uses YAML frontmatter"]
3. ✅ [Coverage criterion, e.g., "all 46 papers have entities extracted"]
4. ✅ [Format criterion, e.g., "all wikilinks verified"]
5. ✅ [Batch note appended]
```

Without end-conditions, sub-sessions exit prematurely or drift. With end-conditions, the sub-session knows when it is done and the project manager can verify completion objectively.

---

## Paywall & Access Fallback (NEW in v2.0)

Many academic papers are paywalled. The skill does not require full text access — it requires **honest evidence status**:

- `evidence_status: full-text` — paper fully read; verbatim quotes verified
- `evidence_status: open-repository` — accepted manuscript or pre-print retrieved from author's institutional repository
- `evidence_status: abstract-only` — only abstract, publisher blurb, table of contents, and open reviews were accessible

For `abstract-only` papers:
- Mark all findings as `[inferred from abstract — full text not accessed]`
- Document in batch note: "X papers were paywalled; finding extraction is from abstracts only"
- The downstream synthesis must weight paywalled papers' contributions lower

This honest scoping prevents hallucination when sources cannot be fully verified.

---

## File Persistence (NEW in v2.0)

All sub-sessions read and write to the **same project directory**:

```
{project_root}/
├── papers/
│   ├── search-protocol.md
│   ├── raw/                      # search logs per region
│   ├── meta/                     # paper metadata (optional, can be in search logs)
│   ├── appraisals/               # one .appraisal.md per paper
│   ├── unified-candidate-list.md # final paper roster
│   └── coverage-report.md        # (optional)
├── knowledge-base/
│   ├── entities/                 # Obsidian-compatible entity notes
│   ├── relations.json            # structured relations
│   ├── summary.md                # human-readable KB overview
│   ├── analysis/                 # round1...round5 outputs + checkpoint
│   └── synthesis.md              # final synthesis (last)
└── sub-sessions/                 # (NEW) prompts for SS1-SSn, organized by phase
```

The main session verifies files exist after each sub-session returns. The project directory is the single source of truth across sessions.

---

## Batch Note Pattern (NEW in v2.0)

Every sub-session appends a `# SS{n} Batch Note` section to its primary output. This section documents:
- What was produced (count by type)
- What evidence_status distribution was achieved
- Open issues for the project manager
- Papers to re-evaluate
- Honest assessment of quality (e.g., "abstract-only for 5 of 8 papers")

The main session reads the batch note first to decide whether to proceed, loop, or intervene.
