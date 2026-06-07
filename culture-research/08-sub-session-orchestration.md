# Phase 8: Sub-Session Orchestration (REFINED in v3.0)

**Purpose:** Coordinate multi-session execution of the culture-research workflow when total work exceeds single-session context capacity.

**When to use:**
- Project has >20 papers to appraise, OR
- Project has 5+ analysis rounds with substantial output each, OR
- Total expected output exceeds ~50,000 tokens

**When NOT to use:**
- Small projects (<10 papers, <3 analysis rounds) — single session is fine
- Projects where the user wants to do everything in one go

---

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│  MAIN SESSION (Project Manager)                          │
│  - Holds project state, tasks.md                        │
│  - Writes sub-session prompts                            │
│  - Verifies outputs from each sub-session                │
│  - Updates project-state.json                            │
│  - Collects Director Observations                        │
│  - Decides: continue / loop / thin roster / pause        │
└──────────────────────────────────────────────────────────┘
                           │
                           │ writes sub-session prompt
                           ▼
┌──────────────────────────────────────────────────────────┐
│  SUB-SESSION (Worker) — fresh context                     │
│  - Reads project-state.json for context                   │
│  - Loads relevant skill file                              │
│  - Reads inputs from project directory                    │
│  - Executes one tight task                                │
│  - Verifies end-conditions met                            │
│  - Writes batch note + Director Observations              │
│  - Returns single summary message                         │
└──────────────────────────────────────────────────────────┘
                           │
                           │ writes outputs to project directory
                           ▼
┌──────────────────────────────────────────────────────────┐
│  PROJECT DIRECTORY (persistent across sessions)          │
│  - papers/                                               │
│  - knowledge-base/                                       │
│  - sub-sessions/                                         │
│  - project-state.json  ← (NEW) single source of truth    │
│  - messages/            ← (NEW) sub-session feedback      │
└──────────────────────────────────────────────────────────┘
```

---

## State Synchronization: project-state.json (NEW in v3.0)

Each sub-session prompt references `project-state.json` for context instead of relying on static descriptions. The PM updates this file after each sub-session completes.

```json
{
  "project": "study-human-daily-behavior",
  "research_question": "How do humans spend their daily time across cultures?",
  "scope": "global",
  "total_papers": 46,
  "phases_complete": ["explore", "search", "deep-read", "knowledge-base", "analysis-r1", "analysis-r2", "analysis-r3", "analysis-r4", "analysis-r5", "checkpoint", "synthesis"],
  "current_phase": "report-writing",
  "deliverables": {
    "appraisals": "papers/appraisals/",
    "entities": "knowledge-base/entities/",
    "findings_index": "knowledge-base/findings-index.json",
    "relations": "knowledge-base/relations.json",
    "synthesis": "knowledge-base/synthesis.md",
    "article": "knowledge-base/article/final-article.md"
  }
}
```

Sub-sessions read this file first to discover what actually exists. The PM updates it after each SS returns.

---

## Sub-Session Anatomy

Every sub-session prompt has these sections:

### 1. Project Context
- Project root path
- Skill file to load (e.g., `culture-research/03-deep-read.md`)
- Source data paths
- Output directory paths
- Reference to `project-state.json` for current state

### 2. Input
- What to read (specific files, specific regions, specific entities)
- What data the sub-session will process

### 3. Task
- What to produce (specific deliverables, specific format)
- The skill's per-phase instructions apply

### 4. End Conditions (CHECKLIST)
- Specific deliverables exist at specific paths
- Quality criteria met (frontmatter, sections, quotes, tags)
- Coverage criteria met (all N papers processed)
- Format criteria met (wikilinks verified, tags conform)
- Batch note appended
- Director Observations appended

### 5. What NOT to Do
- Scope guardrails
- Things the sub-session should NOT do

### 6. Return Format
- Single final message with:
  - Counts of what was produced
  - Evidence/access distribution (if applicable)
  - Open issues
  - Confirmation of file paths
  - Summary of Director Observations

---

## `task_id` Convention (NEW in v3.0)

When using the `task` tool to launch sub-agents, all `task_id` values must start with `"ses"` (lowercase), e.g., `"ses16"`. The format is validated by the system. Do NOT use the sub-session number directly (e.g., `"SS16"` is rejected).

**Parallel execution note:** Sequential sub-agent execution (`task` tool, one at a time) is more reliable than parallel. For parallel attempts, use distinct `task_id` values like `"ses16-ch1"`, `"ses16-ch2"`, etc.

---

## Execution Modes (NEW in v3.1)

Sub-sessions can execute in two modes. Choose before launching:

| Mode | Prompt Creation | Who Launches | Best For |
|---|---|---|---|
| **Human-executed** | LLM writes prompt to `sub-sessions/SS{n}-*.md` | Human reads, approves, copies into new session | Complex tasks, first-time users, calibration runs |
| **LLM-executed** | LLM builds prompt internally, launches via `task` tool | Main session LLM launches directly | Routine tasks, experienced users, speed |

**Decision tree:**
1. Is the task complex or unfamiliar? → **Human-executed**
2. Is this a calibration run (first region batch)? → **Human-executed**
3. Is the task routine and well-understood? → **LLM-executed**
4. Does the human want to review before execution? → **Human-executed**

Both modes produce the same output. The difference is the review/approval step before execution.

---

## Calibration Run Pattern

**Before launching all 6 region deep-reading sub-sessions, run the smallest batch first** (e.g., Oceania with 5 papers or East Asia with 8 papers) as a calibration run:

1. Launch the smallest sub-session
2. The sub-agent returns appraisal files
3. Read 2-3 of them to verify format, quotes, evidence_status
4. If quality is acceptable, launch remaining sub-sessions
5. If quality is off, write **calibration guidance** to the next prompt

This pattern saves significant rework — the first batch reveals appraisal format adjustments before scaling up.

---

## PM Review Loop (Enforced in v3.1)

After each sub-session returns, the PM must execute this review loop BEFORE launching the next sub-session:

1. **Read the batch note** (including Director Observations)
2. **Spot-check 1-2 output files** for the end-conditions checklist
3. **Update `project-state.json`** with new deliverable paths
4. **Save sub-session feedback** to `messages/SS{n}-to-management.md`
5. **Mark corresponding tasks complete** in `tasks.md`
6. **Document the PM Review decision** in `skill-evolution-log.md`
7. **Decide next action:**
   - **PROCEED** — launch next sub-session
   - **LOOP** — re-run current sub-session with corrections (document why)
   - **PAUSE** — surface to human for direction
8. **Update the status report** to human

Without this loop, quality issues propagate undetected until the cross-appraisal check. Loop decisions must be documented in `skill-evolution-log.md` so the retrospective can trace every course-correction.

---

## Cross-Phase Gates (NEW in v3.0)

Between phases, verify:

| Gate | After | What to Check | Artifact |
|---|---|---|---|---|
| PM Review Loop (NEW in v3.1) | Each Sub-Session | Batch note read + output spot-check + decision logged | `skill-evolution-log.md` entry |
| Cross-Appraisal Consistency | Deep Reading | Same criteria applied across regions? | `papers/appraisals/_cross-appraisal-check.md` |
| Directory Structure | Each SS | Files exist where project-state.json says they should | PM spot-check |
| Cross-Round Dependency | Rounds 2-5 | Prior round's end conditions met | Batch note review |
| Synthesis Readiness | Checkpoint | Verdict is PROCEED or PROCEED WITH NOTES | `checkpoint-review.md` |

---

## Director Role (Active in v3.0)

No longer a placeholder. The Director is an active role (can be the PM or a dedicated sub-session) that:

1. **Receives Director Observations** from every sub-session's batch note
2. **Aggregates** observations into a `knowledge-base/director-report-{round}.md` after each major phase
3. **Identifies methodology patterns** — which methods produce the most robust findings, which regions have systematic weaknesses
4. **Tracks quality variance** — are some sub-sessions consistently better or worse than others?
5. **Proposes skill updates** based on accumulated experience
6. **Maintains `skill-evolution-log.md`** in the project root

The Director Observations template (appended to every batch note):

```markdown
## Director Observations

### Quality variance
- Did all sub-session outputs meet the same quality bar? {Yes/No — note outliers}
- Any outputs notably better/worse than others? {list}

### Scope discipline
- Did any sub-session drift outside its defined scope? {Yes/No}
- Any "What NOT to do" instructions violated? {list}

### Prompt clarity issues
- Did the sub-session have to guess about anything? {Yes/No}
- What part of the prompt was unclear or missing? {specifics}

### Coordination overhead
- How much main-session attention did this SS require? {low/medium/high}
- Any blockers that required human intervention? {list}

### Generalizable lessons
- What did this SS teach that should update the skill? {specifics}
- Any new pattern discovered? {description}
```

---

## Skill Evolution Phase (NEW in v3.0)

After the project retrospective, produce a `skill-evolution-log.md` entry:

1. Which skill instructions were followed successfully? (keep as-is)
2. Which skill instructions were ambiguous or violated? (rewrite)
3. Which new patterns emerged that should be formalized? (add to skill)
4. What cross-phase gates were missing? (add)
5. What would the next project need that this project didn't? (add)

This turns the retrospective into a living improvement cycle.

---

## Project Sizing Guide (NEW in v3.2)

The sub-session sequence scales with project size. Use this guide to select the right template:

### Small: 1–2 regions, 5–15 papers (Local scope)

| SS | Phase | Output |
|---|---|---|
| SS1 | Deep reading (all papers) | N .appraisal.md |
| SS2 | Entity extraction + relations | Entities, findings-index.json, relations.json |
| SS3 | Round 1–2 (thematic + comparison, combined) | Thematic map + matrix |
| SS4 | Round 3–4 (contradictions + gaps, combined) | Contradictions + gaps |
| SS5 | Round 5 + Checkpoint + Synthesis (combined) | Questions + checkpoint + synthesis |

Total: 5 sub-sessions. Rounds can be combined because fewer findings means smaller context per round.

### Medium: 3–4 regions, 20–50 papers (Focused global) — RECOMMENDED

| SS | Phase | Output |
|---|---|---|
| SS1-SS4 | Deep reading (one per region) | N .appraisal.md |
| SS5 | Entity extraction | Entities + findings-index.json |
| SS6 | Relations | relations.json + summary.md |
| SS7 | Round 1 Thematic | round1-thematic-map.md |
| SS8 | Round 2 Comparison | round2-comparison-matrix.md |
| SS9 | Round 3 Contradictions | round3-contradictions.md |
| SS10 | Round 4 Gaps | round4-gaps.md |
| SS11 | Round 5 Questions | round5-research-questions.md |
| SS12 | Checkpoint | checkpoint-review.md |
| SS13 | Synthesis | synthesis.md |
| SS14+ | Report writing | report/ |
| SS15+ | Retrospective | skill-evolution-log.md |

Total: 13–15 sub-sessions. Each round gets its own session. Report writing is optional.

### Large: 5–6 regions, 40–80 papers (Broad global)

Same as Medium, but:
- Deep reading: 1 SS per region (SS1-SS6)
- Entity extraction: split into 2 SS (SS7a East + South, SS7b West)
- Relations: 1 SS (SS8)
- Analysis: same 5 rounds, but each round may need sub-splitting (SS10a/SS10b/SS10c for Round 2)
- Report writing: 2+ SS if long-form article

Total: 18–22 sub-sessions.

### Exhaustive: 7+ regions, 60+ papers

Same as Large, but:
- Deep reading: 1 SS per region (SS1-SS7+)
- Entity extraction: 3 SS (East, West, South)
- Analysis rounds may each need 2-3 sub-sessions
- A dedicated PM sub-session may be needed for state tracking

Total: 25+ sub-sessions. Consider whether exhaustive coverage is necessary — 3-4 regions at 30-50 papers typically yields the best depth-to-coverage ratio.

---

## Project Directory Layout (REFINED in v3.0)

```
{project_root}/
├── papers/
│   ├── search-protocol.md
│   ├── raw/                             # search logs per region
│   ├── appraisals/                      # .appraisal.md per paper
│   │   └── _cross-appraisal-check.md    # (NEW) consistency artifact
│   ├── unified-candidate-list.md
│   └── coverage-report.md
├── knowledge-base/
│   ├── entities/                        # 5 entity type subdirs
│   ├── findings-index.json              # (NEW) machine-readable
│   ├── relations.json
│   ├── summary.md
│   ├── analysis/                        # round1...round5 + checkpoint
│   ├── synthesis.md
│   └── article/                         # (NEW) report-writing outputs
├── sub-sessions/
│   ├── README.md
│   ├── SS_TEMPLATE.md
│   └── SS{n}-*.md
├── messages/                            # (NEW) SS feedback
│   └── SS{n}-to-management.md
├── project-state.json                   # (NEW) state sync
└── skill-evolution-log.md               # (NEW) improvement record
```

---

## Common Sub-Session Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| Sub-session runs out of context mid-task | Task too large | Split: one SS per region, or one SS per 5-10 papers |
| Sub-session exits before all end-conditions met | End-conditions not clear | Write end-conditions as a checkbox list |
| Sub-session drifts into other phases | Scope not bounded | Add explicit "What NOT to do" section |
| Sub-session fabricates quotes for paywalled paper | Verbatim rule not enforced | Re-emphasize: never paraphrase; use `[inferred]` |
| Sub-session writes to wrong path | Path typos in prompt | Verify file path exists after return; use project-state.json |
| Sub-session output uses ad-hoc tags | Tag taxonomy not specified | Include approved taxonomy in prompt |
| Sub-session hits 50KB truncation (NEW) | File too large | Add truncation warning to prompt; instruct offset reading |
| Sub-session can't read file with non-ASCII name (NEW) | Encoding issue on Windows | Run `_check_encoding.ps1` first; use `_filename_map.json` |

---

## Sub-Session Prompt Template

A reusable template is available at `sub-sessions/SS_TEMPLATE.md`. To create a new sub-session:

1. Copy the template
2. Fill in: region/paper count/output path/end-condition checkboxes
3. Save with sequential numbering
4. Add to the index in `sub-sessions/README.md`
5. Update `project-state.json` if adding a new deliverable path

---

## When the Sub-Session Architecture Is Overkill

- Single small paper (1-3): no SS needed
- Small project (5-10 papers, no synthesis): no SS needed
- A user who wants to do everything in one session: no SS needed

The SS architecture is a **scaling solution**, not a default. Apply it when context limits are a real concern.

---

## Output

After all sub-sessions complete:
- All files in `papers/`, `knowledge-base/`, `sub-sessions/`, `messages/`
- `project-state.json` with all phases marked complete
- `skill-evolution-log.md` with accumulated lessons
- `tasks.md` with all phases marked complete
- A final status report to the human

The `synthesis.md` is the terminal analytical deliverable. After it is written and verified, all phases are marked complete in `project-state.json` and the project directory serves as the persistent record.
