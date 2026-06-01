---
name: culture-research
description: Cultural one-off study workflow: paper collection, deep reading, knowledge graph construction, multi-round iterative analysis, and Obsidian-based knowledge visualization. No programming or human-subject data collection.
license: MIT
metadata:
  version: "1.0"
  files:
    - "01-explore.md"
    - "02-search-collect.md"
    - "03-deep-read.md"
    - "04-knowledge-base.md"
    - "05-multi-round-analysis.md"
    - "06-checkpoint.md"
    - "07-synthesis.md"
---

# Culture Research Skill

A structured workflow for **cultural one-off studies** focused on human behavior, social practices, and everyday life. Designed for web-search-based paper collection and qualitative synthesis — no programming, no human-subject data collection, no dashboards.

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

---

## Workflow Overview

```
Explore ──→ Search Design ──→ Region Searches (parallel) ──→ Acquisition
                                                                │
                                                                ▼
                                                         Deep Reading (parallel per paper)
                                                                │
                                                                ▼
                                                     Knowledge Base ──→ Entities + Relations
                                                                │          └── Obsidian `.md` files
                                                                ▼
                                          ┌── Round 1: Thematic Categorization
                                          │── Round 2: Cross-Cultural Comparison
                                          │── Round 3: Contradiction Deep-Dive
                                          │── Round 4: Gap & Blind Spot Mapping
               Iteration Checkpoint ←─────┘── Round 5: Research Question Generation
                    │
                    ▼ (if weak links, loop back to relevant round)
         ┌─ Refine rounds ─┐
         └────→ Synthesis Document
```

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
