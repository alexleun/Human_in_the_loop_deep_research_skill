---
name: deep-research
description: Deep research workflow with human guidance. Topic-agnostic. For detailed phase instructions, load the corresponding sub-file from this directory.
license: MIT
metadata:
  version: "4.1"
  files:
    - "01-explore.md"
    - "02-propose.md"
    - "03-collect.md"
    - "04-analyze.md"
    - "05-report.md"
    - "06-web-output.md"
    - "07-review.md"
    - "08-iterate.md"
    - "09-archive.md"
    - "10-implement.md"
    - "state-management.md"
---

# Deep Research Skill

A modular skill for structured deep research in collaboration with a human. Works on **any topic**.

---

## Research Lifecycle

```
  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
  │  EXPLORE  │───▶│ PROPOSE  │───▶│  APPLY   │───▶│  REVIEW  │
  │ (think)   │    │ (design) │    │ (do)     │    │ (audit)  │
  └──────────┘    └──────────┘    └──────────┘    └──────────┘
       │                              │                 │
       │   ┌──────────────────────────┘                 │
       │   │   ┌────────────────────────────────────────┘
       ▼   ▼   ▼
     ┌──────────────────────────────────────────────────────┐
     │                    ITERATE                            │
     └──────────────────────────────────────────────────────┘
       │                              ▲
       │   (scope grows beyond)       │   (issues found,
       ▼                              │    loop back)
     ┌──────────────────────────────────────────────────────┐
     │              OPESPEC CHANGES (follow-on)              │
     │  Branch research output into independently tracked   │
     │  changes: data pipeline, knowledge base, web pages   │
     └──────────────────────────────────────────────────────┘
```

**Phase revisiting is normal.** Real research is not linear. You will discover encoding corruption during Phase 6 and need to fix Phase 5 output. You will spot structural issues during review (Phase 7) and need to regenerate Phase 6 pages. This is expected — do not feel pressure to complete each phase in one pass.

**When to loop back:**
- **Phase 6 → Phase 5:** If web output reveals that the report structure (cards vs prose, section ordering) isn't working, update the report design in Phase 5 before regenerating pages.
- **Phase 7 → Phase 5/6:** Review audit findings, fix at the source (Phase 5 for content, Phase 6 for rendering), then regenerate.
- **Phase 8 → Phase 3/4:** Iteration discovered a new pattern needing data collection/analysis — cycle back before updating the narrative.
- **Any phase → Phase 1:** If the scope has fundamentally changed (new topic, new research question), restart from exploration.

**How to loop back:**
1. State which phase you're revisiting and why
2. Load that phase's sub-file
3. Make the fix
4. Re-verify downstream phases (e.g., if you changed Phase 5 content, re-run Phase 6 parity checks)
5. Do NOT mark the earlier phase as "incomplete" — it was valid at the time; the iteration creates a new version

**Experience note from global-heatwave project:** The research naturally spawned 3 follow-on openspec changes (database-notebook, knowledge-base, website-chapters). Each had independent tasks and lifecycle but shared the same source data and design decisions. This is the expected pattern when research depth exceeds what a single change can contain.

---

## Core Methodology Principles

These apply across ALL phases. Read them first.

### 1. Objective-Driven, Not Role-Driven

State what needs to be done. Do not assign personas or roles to the LLM. Role constraints consume attention tokens and cause "role capture" — the LLM performs confidence instead of actual reasoning. Short, direct instructions outperform elaborate personas.

Good: "Extract the three key metrics from this source and cite exact text."
Bad: "You are a senior research analyst at a top-tier think tank..."

### 2. Grounding (Anti-Hallucination)

Every factual output must cite **exact quoted text** from the source material. Paraphrasing introduces hallucination risk.

- Data extraction: include `"exact_quote": "the verbatim text"` in the output
- Source citation: include the specific sentence or paragraph, not just the URL
- If the source lacks evidence for a claim, mark it `[Data Gap]` — never fill in from memory

### 3. Code-First Analysis

For any quantitative task: **output code, not numbers.** The LLM writes Python that the human runs locally. Results come from actual execution, not LLM memory.

- Good: "Write a Pandas script to compute the correlation. Here is the CSV."
- Bad: "The correlation coefficient is approximately 0.87."

### 4. Binary Choice for Output Blocks

When the output spec offers multiple formats (JSON vs Python, HTML vs Markdown), the LLM must pick **one** per block. Mixing formats in the same block causes decoding errors.

### 5. Citation-First (Not Retrofitted)

Source citations must be embedded from Phase 2, not added in Phase 7 review. Every change proposal must specify the `data-source` IDs and confidence levels that findings will carry. This prevents the retrofitting pain experienced when adding `data-source` attributes to every claim block after all reports were written — a process that required 5+ scripts and multiple parity fixes.

### 6. Encoding Awareness (for CJK Content)

When generating Chinese/Japanese/Korean content on Windows systems, PowerShell encoding behavior corrupts files:
- `>` and `|` operators use the system code page, not UTF-8
- U+FFFD replacement characters appear when UTF-8 bytes are decoded as Windows-1252
- Fix: Always use Python `open(path, "w", encoding="utf-8")` or .NET `[System.IO.File]::WriteAllText()`
- Verify: After writing a ZH file, re-read it and check for `\uFFFD` characters

### 7. Bilateral Parity Verification

"Bilingual parity" is not a one-time goal — it requires automated verification at each phase boundary. For every EN file, the corresponding ZH file must pass:
- Same count of `<div class="finding">` blocks
- Same count of `data-source` attributes
- Same count of `data-confidence` attributes
- No `\uFFFD` encoding errors
- Consistent nav labels across all files in the language

### 8. Review Manifest (Optional, Phase-Dependent)

When the task is complex or the human needs a checkpoint:
- Use a short text summary (3-5 bullets), not a YAML block
- Include: what was done, how many sources/claims were processed, what gaps remain
- Skip when the human is actively guiding — the conversation log serves as the manifest

**Experience note:** In practice, the Review Manifest was never used during the HK research project. The human-in-the-loop workflow naturally provides checkpointing through conversation. Reserve manifests for fully autonomous sub-agent tasks.

### 9. Schema-as-Source-of-Truth

When research involves a database schema (SQLAlchemy, Django ORM, etc.), model files are the **single source of truth**. Migrations are derived from models, never hand-written or manually edited. Before any code that reads or writes the database, verify that field/column names in consuming code match the model definitions exactly — use `model.__table__.columns.keys()` or equivalent introspection to catch mismatches early.

- Good: "Run `python -c 'from app.models import Model; print([c.name for c in Model.__table__.columns])'` and confirm column names in your query match."
- Bad: "I think the column is called `city`" — then writing SQL with `city` when the model uses `city_name`.

### 10. Graceful Degradation (Fallback Consciousness)

Any interactive system consuming research data (dashboards, APIs, reports) must handle the case where data stores are empty, unreachable, or still being populated. Implement fallback states with representative sample data so the system is always demonstrable. This prevents "works on my machine" syndrome and ensures stakeholders can see the interface regardless of data pipeline status.

- At proposal time (Phase 2), define fallback strategy: what sample data will be used, how will the user know they're seeing fallback vs live data
- At implementation, separate data-fetching from rendering so each path can be tested independently
- Mark fallback data clearly so it's not mistaken for real findings

### 11. Post-Generation HTML Structural Validation

After generating HTML output (especially bilingual sites), validate DOM structure — not just element counts:

- **Div balance check**: Count `<div>` opens vs `</div>` closes across every HTML file. A mismatch means broken layout that the parity checker won't catch.
  ```
  import re
  with open(file) as f:
      c = f.read()
  opens = len(re.findall(r'<div\b', c))
  closes = len(re.findall(r'</div>', c))
  if opens != closes:  # fix before deploying
  ```
- **Replacement character scan**: Alongside U+FFFD, scan for literal `??` bytes (0x3F 0x3F) which appear when em dashes `—` (U+2014, UTF-8 bytes `E2 80 94`) are written through a non-UTF-8 pipe and degraded. These are invisible to the U+FFFD check.
  ```
  if '??' in open(file, encoding='utf-8').read():  # check for degraded UTF-8
  ```
- **Title tag check**: Every HTML page must have a non-empty `<title>` with the correct language prefix.
- **Footer freshness check**: Every page's footer must reference the current date or generation batch.

**Experience note (global-heatwave):** The parity checker counted finding blocks correctly (element-level), but a stray `</div>` in the ZH integrated-analysis chapter went undetected for days. The ZH file had 27 div opens but 28 closes. The DOM rendered incorrectly but no script flagged it. Add structural checks before any "all done" declaration.

### 12. Cross-Artifact Consistency Check

When a new finding, data point, or section is added to one output artifact, it must propagate to ALL artifacts where it belongs. This is not automatic — it requires explicit mapping.

**Checklist before marking any addition complete:**
- [ ] **Report chapters**: Is the finding reflected in the relevant chapter page(s)?
- [ ] **Executive summary / Synthesis**: If the finding is significant, does the synthesis or overview page reference it?
- [ ] **Knowledge base**: If the finding introduces a new entity or relation, is it added to the KB?
- [ ] **Dashboard / Interactive features**: If the finding produces new data (predictive thresholds, maps, time series), is the dashboard description or feature list updated?
- [ ] **Bilingual pair**: Is the ZH version of each updated artifact also updated?

**Experience note (global-heatwave):** After adding §9.0 Predictive Timing to the integrated analysis chapter, the dashboard description in `dashboard-intro.html` had no mention of it. The data existed in `output/data/` and the report chapter, but the "Interactive Features" list on the dashboard page was stale. A cross-artifact scan would have caught this before manual review.

### 13. Date Freshness Audit

Generated output accumulates stale timestamps. After any batch of changes:

1. **Scan every HTML file** for date patterns (`compiled|last updated|updated|20\d{2}-\d{2}-\d{2}`) and verify they match the current project epoch
2. **Check both EN and ZH versions** — ZH footers frequently diverge from EN dates
3. **Check version strings** in hero meta sections (e.g., `v0.1.0 &bull; May 2026`)
4. **Bump all stale dates in one pass** — use a script, not manual per-file edits

```python
# bump_dates.py — run after any content batch
import glob
for fp in glob.glob("output/**/*.html", recursive=True):
    with open(fp, encoding="utf-8") as f:
        c = f.read()
    orig = c
    c = c.replace("May 2026", "June 2026")  # adjust for current month
    c = c.replace("2026-05-29", "2026-06-01")
    if c != orig:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c)
```

**Experience note (global-heatwave):** When reviewed in June 2026, 17 EN pages still said "compiled May 2026" and 13 ZH pages said "2026-05-29". The four-month-old timestamps made the project look dormant. A date freshness audit in Phase 7 would have caught this.

### 14. Change Boundary Detection (When to Spin Off)

One change cannot contain infinite depth. The global-heatwave project demonstrated that research outputs naturally expand into multiple distinct work streams. Detecting when a single change has reached its limits — and when to spin off a new one — is a critical skill.

**Signals that a scope boundary has been reached:**

| Signal | Example | Action |
|--------|---------|--------|
| Tasks exceeding 15-20 total items | 39 tasks in extend-knowledge-base | Spin off the next layer (e.g., web pages for chapter content became a separate change) |
| Multiple independent output types | Knowledge base (fact cards) + website (chapter pages) | Split by output type: KB content in one change, website rendering in another |
| Different verification needs | Data pipeline needs CSV cross-checks; web output needs bilingual parity | Split so each change has its own verification script suited to its artifact type |
| Parallelizable work streams | KB chapter writing (content) vs website nav update (templating) | Spin off so each stream can proceed independently |
| Design decisions that affect downstream | KB fact card schema determines chapter page layout | Make the upstream change first (KB schema), then spin off the downstream (website) with the schema as a dependency |

**How to spin off:**
1. Complete current change's primary artifact (e.g., all fact cards written and validated)
2. Create a new change via `/opsx-propose` with its own proposal, design, specs, tasks
3. Reference the upstream change's artifacts and decisions in the new change's design.md
4. Archive the upstream change only after the downstream is complete (or in parallel if they're truly independent)

**Heuristic:** If a single task description runs over 2 lines or mixes two types of work (e.g., "Create fact cards AND generate chapter HTML"), it's already past the boundary. Split before writing the task.

---

## Phase Router

Load the sub-file matching your current task:

| Current Task | Load This File |
|---|---|
| Scoping topic, exploring ideas, discussing with human | `01-explore.md` |
| Creating change proposal, design, specs, tasks | `02-propose.md` |
| Collecting sources, data pipeline, building knowledge base | `03-collect.md` |
| Running analysis, writing notebooks, generating figures | `04-analyze.md` |
| Writing research document | `05-report.md` |
| Generating bilingual website, HTML pages, SVG map | `06-web-output.md` |
| Auditing for methodological weaknesses | `07-review.md` |
| Developing new point of view, reframing | `08-iterate.md` |
| Finalizing deliverables, archiving the change | `09-archive.md` |
| Building application from research (bridge phase) | `10-implement.md` |
| Switching machines, resuming interrupted work | `state-management.md` |
| Transitioning research output into an openspec implementation change | See "Post-Research → openspec Bridge" below |

## Post-Research → openspec Bridge

Research output (facts, findings, data sources, design decisions) often needs to be implemented as structured artifacts. This bridge connects deep-research output to openspec changes.

### When to Bridge

- Research has produced findings that need to be rendered as a bilingual website → create a new openspec change for web output
- Source documents have been collected and need a structured knowledge base → create a new openspec change for KB
- Analysis scripts need to be productionized as notebooks or dashboards → create a new openspec change for tooling

### What to Carry Forward

When creating an openspec change from research output, copy forward:

| From deep-research | To openspec change |
|---|---|
| Source index (`knowledge_base/sources/sources_index.md`) | `design.md` — data sources section |
| Fact cards / findings | `specs/<capability>/spec.md` — requirements per capability |
| Design decisions from research | `design.md` — architecture decisions |
| Verification scripts from research | `tasks.md` — adaptation/porting of scripts |
| Bilingual parity patterns | Parity verification tasks in the new change |

### What NOT to Carry Forward

- Do NOT copy raw source documents — link to them from `knowledge_base/sources/`
- Do NOT copy the research proposal — create a fresh proposal scoped to the implementation
- Do NOT re-debate design decisions already made in research — reference them as settled

### Example (from global-heatwave project)

```
Research output (deep-research skill)
    │
    ├──→ openspec: extend-database-notebook
    │     Source cache, analysis notebooks, bilingual output, parity checker
    │
    ├──→ openspec: extend-knowledge-base
    │     8-chapter fact cards, validator, knowledge graph entities
    │
    └──→ openspec: extend-website-chapters
          8 chapter pages, KB index page, nav update, parity checker update
```

Each openspec change added a new layer of value on top of the same research base, with independent task tracking and verification gates.

---

## Collaboration Model

| Task | LLM does | Human does |
|---|---|---|
| Data collection | Fetches, extracts, validates | Provides access, flags bias |
| Analysis | Writes code, runs computations | Interprets, redirects |
| Report writing | Drafts document, generates web pages | Reviews, adds nuance |
| Design | Proposes methodology, flags tradeoffs | Approves/rejects, sets priorities |
| Audit | Checks methodology, flags issues | Identifies non-obvious weaknesses |
| Decisions | Presents options with recommendations | **Makes the call** |

**Key principle:** LLM proposes, human disposes.

---

## Guardrails

- **Propose before implementing** — no data collection without a proposal
- **Log every source** — local copy in `knowledge-base/sources/` for fact-checking
- **Never silently fix** — surface methodological issues before fixing
- **Bilingual parity** — both languages must have same content and quality; verify with automated script, not manually
- **Verify encoding after generation** — especially CJK content on Windows; check for U+FFFD AND `??` (degraded em dash) before considering a file complete
- **Validate HTML structure** after every batch of page output — run div balance check; a single stray `</div>` breaks layout silently
- **Run cross-artifact consistency check** when adding new findings — verify they appear in all relevant output artifacts (chapters, synthesis, dashboard, knowledge base)
- **Audit date freshness** before declaring any phase complete — scan all HTML files for stale timestamps and bump in one pass
- **Don't delete old versions** — use `_v1`, `_v2` suffixes
- **Flag uncertainty** — distinguish facts, claims, hypotheses
- **Verify CSVs against authoritative sources** — do not assume web-scraped or LLM-generated data is correct; cross-check key numbers
- **Validate code by running it** — after generating any runnable code (scripts, dashboards, tests), execute it and verify zero errors before marking the phase complete
- **Seed before archiving** — research outputs must be seeded into the target database/knowledge graph before the change is archived; document seed scripts in the repository
