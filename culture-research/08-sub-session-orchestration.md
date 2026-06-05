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
│  - Holds openspec change, tasks.md                       │
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

## Calibration Run Pattern

**Before launching all 6 region deep-reading sub-sessions, run the smallest batch first** (e.g., Oceania with 5 papers or East Asia with 8 papers) as a calibration run:

1. Launch the smallest sub-session
2. The sub-agent returns appraisal files
3. Read 2-3 of them to verify format, quotes, evidence_status
4. If quality is acceptable, launch remaining sub-sessions
5. If quality is off, write **calibration guidance** to the next prompt

This pattern saves significant rework — the first batch reveals appraisal format adjustments before scaling up.

---

## Verifying Sub-Session Outputs

After each sub-session returns:

1. **Spot-check 1-2 output files** for the end-conditions checklist
2. **Read the batch note** to surface any open issues
3. **Read the Director Observations** to accumulate quality data
4. **Mark corresponding tasks complete** in `tasks.md`
5. **Update `project-state.json`** with new deliverable paths
6. **Save sub-session feedback** to `messages/SS{n}-to-management.md`
7. **Decide next action:**
   - PROCEED — launch next sub-session
   - LOOP — re-run current sub-session with corrections
   - PAUSE — surface to human for direction
8. **Update the project manager's status report** to human

---

## Cross-Phase Gates (NEW in v3.0)

Between phases, verify:

| Gate | After | What to Check | Artifact |
|---|---|---|---|
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

## Sub-Session Sequence (15 SS for a 46-paper project)

| SS | Phase | Output | Depends On |
|---|---|---|---|
| SS1-SS6 | Deep reading (one per region) | 46 .appraisal.md | SS0 (search logs) |
| SS7 | Entity extraction | 5 entity types + findings-index.json | SS1-SS6 |
| SS8 | Relations | relations.json + summary.md | SS7 |
| SS9 | Round 1 Thematic | round1-thematic-map.md | SS7-SS8 |
| SS10 | Round 2 Comparison | round2-comparison-matrix.md | SS9 |
| SS11 | Round 3 Contradictions | round3-contradictions.md | SS10 |
| SS12 | Round 4 Gaps | round4-gaps.md | SS10-SS11 |
| SS13 | Round 5 Questions | round5-research-questions.md | SS11-SS12 |
| SS14 | Checkpoint | checkpoint-review.md | SS9-SS13 |
| SS15 | Synthesis | synthesis.md | SS14 |
| SS16+ | Report writing | article/report | SS15 |
| SS17 | Retrospective + Archive | project-retrospective.md | All |

For projects of different sizes, scale the deep-reading sub-sessions (more or fewer regions).

---

## Project Directory Layout (REFINED in v3.0)

```
{project_root}/
├── openspec/
│   └── changes/{change-name}/
│       ├── proposal.md
│       ├── design.md
│       ├── specs/...
│       └── tasks.md
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

The `synthesis.md` is the terminal analytical deliverable. After it is written and verified, the openspec change can be archived.
