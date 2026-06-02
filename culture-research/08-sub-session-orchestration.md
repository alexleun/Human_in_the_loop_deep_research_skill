# Phase 8: Sub-Session Orchestration (NEW in v2.0)

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
┌────────────────────────────────────────────────────┐
│  MAIN SESSION (Project Manager)                    │
│  - Holds openspec change, tasks.md                 │
│  - Writes sub-session prompts                      │
│  - Verifies outputs from each sub-session          │
│  - Marks tasks complete                            │
│  - Decides: continue / loop / thin roster / pause  │
└────────────────────────────────────────────────────┘
                       │
                       │ writes sub-session prompt
                       ▼
┌────────────────────────────────────────────────────┐
│  SUB-SESSION (Worker) — fresh context               │
│  - Loads relevant skill file                       │
│  - Reads inputs from project directory             │
│  - Executes one tight task                         │
│  - Verifies end-conditions met                     │
│  - Returns single summary message                  │
└────────────────────────────────────────────────────┘
                       │
                       │ writes outputs to project directory
                       ▼
┌────────────────────────────────────────────────────┐
│  PROJECT DIRECTORY (persistent across sessions)    │
│  - papers/                                         │
│  - knowledge-base/                                 │
│  - sub-sessions/                                   │
└────────────────────────────────────────────────────┘
```

---

## Sub-Session Anatomy

Every sub-session prompt has these sections:

### 1. Project Context
- Project root path
- Skill file to load (e.g., `culture-research/03-deep-read.md`)
- Source data paths
- Output directory paths

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

### 5. What NOT to Do
- Scope guardrails
- Things the sub-session should NOT do (no new searches, no other phases, no entity creation, etc.)

### 6. Return Format
- Single final message with:
  - Counts of what was produced
  - Evidence status distribution (if applicable)
  - Open issues
  - Confirmation of file paths

---

## Sub-Session Sequence (15 SS for a 46-paper project)

| SS | Phase | Output | Depends On |
|---|---|---|---|
| SS1-SS6 | Deep reading (one per region) | 46 .appraisal.md | SS0 (search logs) |
| SS7 | Entity extraction | 5 entity types in `entities/` | SS1-SS6 |
| SS8 | Relations | `relations.json` + `summary.md` | SS7 |
| SS9 | Round 1 Thematic | `round1-thematic-map.md` | SS7-SS8 |
| SS10 | Round 2 Comparison | `round2-comparison-matrix.md` | SS9 |
| SS11 | Round 3 Contradictions | `round3-contradictions.md` | SS10 |
| SS12 | Round 4 Gaps | `round4-gaps.md` | SS10-SS11 |
| SS13 | Round 5 Questions | `round5-research-questions.md` | SS11-SS12 |
| SS14 | Checkpoint | `checkpoint-review.md` | SS9-SS13 |
| SS15 | Synthesis | `knowledge-base/synthesis.md` | SS14 |

For projects of different sizes, scale the deep-reading sub-sessions (more or fewer regions).

---

## Project Directory Layout

```
{project_root}/
├── openspec/                            # openspec change
│   └── changes/{change-name}/
│       ├── proposal.md
│       ├── design.md
│       ├── specs/...
│       └── tasks.md                     # updated as SS complete
├── papers/
│   ├── search-protocol.md
│   ├── raw/                             # search logs per region
│   │   ├── search-log-east-asia.md
│   │   └── ...
│   ├── meta/                            # optional metadata JSON
│   ├── appraisals/                      # 46 .appraisal.md
│   ├── unified-candidate-list.md
│   └── coverage-report.md
├── knowledge-base/
│   ├── entities/
│   │   ├── researcher/                  # 1 .md per researcher
│   │   ├── cultural_context/
│   │   ├── method/
│   │   ├── behavior_domain/
│   │   └── finding/
│   ├── relations.json
│   ├── summary.md
│   ├── analysis/                        # round1...round5 + checkpoint
│   └── synthesis.md                     # final
└── sub-sessions/                        # SS1-SSn prompt files
    ├── README.md
    ├── SS1-east-asia-deep-read.md
    ├── SS2-south-southeast-asia-deep-read.md
    ├── ...
    └── SS15-synthesis.md
```

---

## Calibration Run Pattern (NEW in v2.0)

**Before launching all 6 region deep-reading sub-sessions, run the smallest batch first** (e.g., Oceania with 5 papers or East Asia with 8 papers) as a calibration run:

1. The main session launches the smallest sub-session (SS6 = Oceania = 5 papers, or SS1 = East Asia = 8 papers)
2. The sub-agent returns 5-8 appraisal files
3. The main session reads 2-3 of them to verify:
   - YAML frontmatter correct
   - Sections match template
   - Verbatim quotes present (or `[inferred]` markers)
   - Evidence strength assessed
   - Batch note appended
4. If quality is acceptable, launch remaining sub-sessions (SS2-SS5 or SS2-SS6)
5. If quality is off, the main session writes **calibration guidance** to the next sub-session prompt and re-runs

**This pattern saved significant rework** in the study-human-daily-behavior project — the first batch revealed that the appraisal format needed slight adjustments before scaling up.

---

## Verifying Sub-Session Outputs

After each sub-session returns, the main session:

1. **Spot-check 1-2 output files** for the end-conditions checklist
2. **Read the batch note** to surface any open issues
3. **Mark corresponding tasks complete** in `tasks.md`
4. **Decide next action:**
   - PROCEED — launch next sub-session
   - LOOP — re-run current sub-session with corrections
   - PAUSE — surface to human for direction
5. **Update the project manager's status report** to human

---

## Common Sub-Session Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| Sub-session runs out of context mid-task | Task too large (e.g., "appraise 30 papers in one SS") | Split: one SS per region, or one SS per 5-10 papers |
| Sub-session exits before all end-conditions met | End-conditions not clear in prompt | Re-write end-conditions as a checkbox list |
| Sub-session drifts into other phases | Scope not bounded | Add explicit "What NOT to do" section |
| Sub-session fabricates quotes for paywalled paper | Verbatim rule not enforced | Re-emphasize: never paraphrase without quote; use `[inferred from abstract]` |
| Sub-session writes to wrong path | Path typos in prompt | Verify file path exists in main session after return |
| Sub-session output uses ad-hoc tags | Tag taxonomy not specified | Include the approved tag taxonomy in the prompt |

---

## Sub-Session Prompt Template

A reusable template is available at `sub-sessions/SS_TEMPLATE.md`. To create a new sub-session:

1. Copy the template
2. Fill in: region/paper count/output path/end-condition checkboxes
3. Save with sequential numbering
4. Add to the index in `sub-sessions/README.md`

---

## When the Sub-Session Architecture Is Overkill

- Single small paper (1-3): no SS needed
- Small project (5-10 papers, no synthesis): no SS needed
- A user who wants to do everything in one session: no SS needed

The SS architecture is a **scaling solution**, not a default. Apply it when context limits are a real concern.

---

## Director Observation Hooks (Placeholder for Future Director Role)

The current Worker-only architecture is intentional: finish this project first as proof-of-concept, then design Director/Manager hierarchy based on evidence.

To enable that future design, every sub-session's `# SS{n} Batch Note` should include a `## Director Observations` section. Even without a Director session actively reading these, the data accumulates.

When the time comes to design the Director role, the accumulated observations will answer questions like:

- Did sub-sessions produce consistent output? (quality variance)
- Did sub-sessions drift in scope? (boundary discipline)
- Did sub-sessions need clarification mid-task? (prompt clarity)
- What coordination overhead did the main session incur? (PM cost)
- What would a methodology-specialist Manager have caught that the main session missed? (specialist value)
- What generalizable lessons emerged that should become skill updates? (skill evolution)

### `## Director Observations` Section Template

Sub-sessions should append this to their batch note (in addition to the standard batch note content):

```markdown
## Director Observations (placeholder for future Director role)

### Quality variance
- {Did all sub-session outputs meet the same quality bar?}
- {Any outputs that were notably better/worse than others?}

### Scope discipline
- {Did any sub-session drift outside its defined scope?}
- {Any "What NOT to do" instructions that were violated?}

### Prompt clarity issues
- {Did the sub-session have to guess about anything?}
- {What part of the prompt was unclear or missing?}

### Coordination overhead
- {How much main-session attention did this SS require?}
- {Any blockers that required human intervention?}

### Generalizable lessons
- {What did this SS teach that should update the skill?}
- {Any new pattern discovered?}
```

This is **passive data collection** — sub-sessions do it as part of normal output, no extra work. When the Director role is designed, the observations can be aggregated into the Director's deliverables (skill evolution log, methodology report, generalizable lessons).

---

## Output

After all sub-sessions complete, the main session produces:
- All files in `papers/`, `knowledge-base/`, `sub-sessions/`
- `tasks.md` with all phases marked complete
- A final status report to the human

The `synthesis.md` is the terminal deliverable. After it is written and verified, the openspec change can be archived.
