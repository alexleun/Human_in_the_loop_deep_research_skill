# Deep Research Skill v2.1

A modular skill for structured deep research in collaboration with a human. Works on **any topic**.

**v2.0 changes:** Added End-Conditions Discipline to all 10 phases, formalized Cross-Phase Gates pattern, promoted `task_state.json` to first-class state synchronization, added File Truncation Safeguard and Non-ASCII Filename Handling, introduced Skill Evolution Log pattern, and added 5 new methodology principles (15–19). Based on cross-skill lessons from the culture-research v3.0 upgrade (17 sub-sessions, 46 papers, 6 regions).

**v2.1 changes:** Added Principle 20 (Source Preservation as formal methodology principle). Updated Post-Research → openspec Bridge with detailed artifact mapping table. Based on cross-skill lessons from a 67-paper, 8-region gift-giving project (culture-research v3.1).

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
     └──────────────────────────────────────────────────────┘
```

**Phase revisiting is normal.** Real research is not linear. You will discover encoding corruption during Phase 6 and need to fix Phase 5 output. You will spot structural issues during review (Phase 7) and need to regenerate Phase 6 pages. This is expected — do not feel pressure to complete each phase in one pass.

---

## Core Methodology Principles

These apply across ALL phases. Read them first.

### 1. Objective-Driven, Not Role-Driven

State what needs to be done. Do not assign personas or roles to the LLM. Role constraints consume attention tokens and cause "role capture" — the LLM performs confidence instead of actual reasoning. Short, direct instructions outperform elaborate personas.

### 2. Grounding (Anti-Hallucination)

Every factual output must cite **exact quoted text** from the source material. Paraphrasing introduces hallucination risk.

### 3. Code-First Analysis

For any quantitative task: **output code, not numbers.** The LLM writes Python that the human runs locally. Results come from actual execution, not LLM memory.

### 4. Binary Choice for Output Blocks

When the output spec offers multiple formats (JSON vs Python, HTML vs Markdown), the LLM must pick **one** per block. Mixing formats in the same block causes decoding errors.

### 5. Citation-First (Not Retrofitted)

Source citations must be embedded from Phase 2, not added in Phase 7 review. Every change proposal must specify the `data-source` IDs and confidence levels that findings will carry.

### 6. Encoding Awareness (for CJK Content)

When generating Chinese/Japanese/Korean content on Windows systems, PowerShell encoding behavior corrupts files. Always use Python `open(path, "w", encoding="utf-8")` or .NET `[System.IO.File]::WriteAllText()`. Verify after writing: check for U+FFFD and `??` (degraded em dashes).

### 7. Bilateral Parity Verification

"Bilingual parity" is not a one-time goal — it requires automated verification at each phase boundary.

### 8. Review Manifest (Optional, Phase-Dependent)

Use a short text summary (3-5 bullets) for checkpoints. Skip when the human is actively guiding.

### 9. Schema-as-Source-of-Truth

Model files are the **single source of truth** for database schemas. Migrations are derived from models. Before any code that reads or writes the database, verify field/column names match model definitions exactly.

### 10. Graceful Degradation (Fallback Consciousness)

Any interactive system consuming research data must handle empty/unreachable data stores with fallback states. Implement sample data so the system is always demonstrable.

### 11. Post-Generation HTML Structural Validation

After generating HTML output, validate DOM structure: div balance check, replacement character scan, title tag check, footer freshness check.

### 12. Cross-Artifact Consistency Check

When a new finding, data point, or section is added to one artifact, it must propagate to ALL artifacts where it belongs. Use the mapping checklist before marking any addition complete.

### 13. Date Freshness Audit

Generated output accumulates stale timestamps. After any batch of changes, scan every HTML file for date patterns and bump all stale dates in one pass.

### 14. Change Boundary Detection (When to Spin Off)

One change cannot contain infinite depth. Detect when a single change has reached its limits and spin off a new one.

### 15. End-Conditions Discipline (NEW in v2.0)

Every phase must define its **end conditions** as a checklist, not a description. The end-conditions pattern:

```markdown
## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ [Specific deliverable exists at specific path]
2. ✅ [Quality criterion met]
3. ✅ [Coverage criterion met]
4. ✅ [Format criterion met]
5. ✅ [Review manifest / batch note appended]
```

Without end-conditions, phases exit prematurely or drift. With end-conditions, both LLM and human can verify completion objectively.

### 16. Cross-Phase Gates (NEW in v2.0)

Between major phases, run automated verification gates that produce accountable artifacts:

| Gate | After Phase | What It Checks | Artifact |
|---|---|---|---|
| Source Verification | 3 (Collect) | Every URL/DOI resolves; no hallucinated sources | `verification_log.md` or batch note |
| Data Validation | 3 (Collect) | CSV key inflection points cross-checked vs authoritative sources | `verification_log.md` |
| Code Validation | 4 (Analyze) | Every script runs without errors | Console output logged |
| Encoding Check | 6 (Web Output) | Zero U+FFFD and no `??` degradation in all HTML files | Script output |
| Parity Check | 6 (Web Output) | EN/ZH finding counts match, attributes consistent | `check-parity.py` output |
| HTML Structure | 6 (Web Output) | Div balance, title tags, footer dates | `div_balance_check.py` output |
| Cross-Artifact | 6 (Web Output) | New findings propagate to all output artifacts | Mapping checklist |
| Archive Readiness | 9 (Archive) | All pre-archive checklist items confirmed | Checklist |

Gates are BLOCKING if they fail — fix before proceeding.

### 17. File Truncation Safeguard (NEW in v2.0)

All file reads may be capped at ~50KB by the read tool. After reading any file:

1. Check for truncation markers (`...truncated...` or "Full output saved to...")
2. If truncated, read the remainder with `offset=N`
3. **Batch notes, open questions, and footnotes at the end of each file are critical inputs** — always verify they are captured

This applies to ALL phases: source collection, data analysis, report writing, review.

### 18. Non-ASCII Filename Handling (NEW in v2.0)

Windows cmd/PowerShell treats non-ASCII characters in filenames inconsistently. `ï`, `é`, `ü`, `ñ`, `ç` are common in author surnames and CJK filenames.

**Detection:** If a `read` call fails with "PathNotFound" but `dir /b` shows the file exists, the filename likely contains a non-ASCII character.

**Workaround:** Use `cmd /c copy` with a wildcard (`?` in place of the special character) to copy to a temp path, then `read` the copy.

**Recommended:** Run a `_check_encoding.ps1` script before each file-heavy phase that renames non-ASCII filenames to ASCII equivalents and records the mapping in `_filename_map.json`.

### 19. State Synchronization with task_state.json (NEW in v2.0)

When research spans multiple sessions or machines, use `task_state.json` for state synchronization:

- Located at `openspec/changes/<change-name>/task_state.json`
- Updated after each meaningful action
- Read on session start to reconstruct context
- See `state-management.md` for the full workflow

This is promoted from an optional technique (v1.0) to a recommended pattern (v2.0) for any multi-session project.

### 20. Source Preservation (NEW in v2.1)

After fetching any source content (web page, PDF, API response, dataset), save a local copy BEFORE extracting findings:

- Web page → `knowledge-base/sources/YYYY-MM-DD-description.html`
- PDF → `knowledge-base/sources/YYYY-MM-DD-description.pdf`
- API response → `knowledge-base/sources/YYYY-MM-DD-description.json`
- Search log → already saved as part of the collection protocol

Without local copies, findings become unrecoverable if URLs change or sources go offline. This is a **mandatory** step, not optional. Add the saved filename to the source metadata as `local_copy: knowledge-base/sources/{filename}`.

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

---

## Post-Research → openspec Bridge (Updated in v2.1)

Research output (facts, findings, data sources, design decisions) often needs to be implemented as structured artifacts. Copy forward these artifacts:

| From Research | To Openspec Change |
|---|---|
| `explore/scope-definition.md` | `proposal.md` — research questions, scope |
| `knowledge-base/sources/sources_index.md` | `design.md` — data sources section |
| Data verification logs | `design.md` — data quality notes |
| Key findings / final report | `specs/<capability>/spec.md` — requirements |
| Design decisions from explore phase | `design.md` — architecture decisions |
| `skill-evolution-log.md` | Lessons for next change's `design.md` |

**What NOT to carry forward:**
- Do NOT copy raw source files — link to them from `knowledge-base/sources/`
- Do NOT re-debate settled design decisions — reference them
- Do NOT copy the entire knowledge base — link from the openspec change

**Key rule:** Link to source documents from the research project, don't copy them.

---

## Skill Evolution Log (NEW in v2.0)

After archiving a change, add an entry to `skill-evolution-log.md` in the project root:

```markdown
## YYYY-MM-DD — {change-name}

### What worked well
- {keep these patterns}

### What caused problems
- {rewrite these instructions}

### New patterns discovered
- {formalize these as skill updates}

### Cross-phase gate gaps
- {add gates that were missing}

### Next-project recommendations
- {what would make the next iteration better}
```

This turns every completed change into a skill improvement cycle. Over multiple projects, the log accumulates institutional knowledge about which methodology principles work for which research types.

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

## Guardrails (Updated in v2.0)

- **Propose before implementing** — no data collection without a proposal
- **Log every source** — mandatory local copy in `knowledge-base/sources/` before extraction (see Principle 20)
- **Never silently fix** — surface methodological issues before fixing
- **Bilingual parity** — both languages must have same content and quality; verify with automated script
- **Verify encoding after generation** — check for U+FFFD AND `??` before considering a file complete
- **Validate HTML structure** after every batch of page output — run div balance check
- **Run cross-artifact consistency check** when adding new findings
- **Audit date freshness** before declaring any phase complete
- **Don't delete old versions** — use `_v1`, `_v2` suffixes
- **Flag uncertainty** — distinguish facts, claims, hypotheses
- **Verify CSVs against authoritative sources** — cross-check key numbers
- **Validate code by running it** — execute and confirm zero errors before marking complete
- **Seed before archiving** — document seed scripts in the repository
- **Check end-conditions** before leaving any phase (NEW in v2.0)
- **Run cross-phase gates** at each phase boundary (NEW in v2.0)
- **Check file truncation** after every read (NEW in v2.0)
- **Update task_state.json** after every meaningful action (NEW in v2.0)
- **Map artifacts to openspec** before archiving (NEW in v2.1) — use the bridge table to seed downstream openspec changes
