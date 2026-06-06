# Human-in-the-Loop Research Skills

A collection of structured, artifact-driven AI research skills for **OpenCode** + **OpenSpec** environments. Every skill in this repository is built around a single principle: **the human stays in the loop, learns alongside the AI, and never receives a finished black box.**

This repository currently ships two skills, both validated through real research projects:

| Skill | Folder | Version | Best for |
|---|---|---|---|
| **deep-research** | `deep-research/` | v2.0 | Topic-agnostic, quantitative + qualitative research with code-first analysis, Jupyter notebooks, and bilingual website output |
| **culture-research** | `culture-research/` | v3.0 | Cultural / behavioral one-off studies: paper collection, deep reading, knowledge graph, multi-round qualitative analysis, Obsidian vault |

---

## 🧠 The Philosophy: Co-Learning over Blind Automation

In a world where commercial tools (like OpenAI Deep Research or Perplexity Pro) try to automate everything away, humans are left in the dark. 
* **The Problem with Black Boxes:** If an AI does 100% of the work in secret and just hands you a finished file, **the human learns nothing.** A static report cannot help an independent developer truly understand how to build or evolve their project. 
* **The Solution (Co-Learning):** This skill treats research as a collaborative partnership. By forcing human-gated checkpoints, you are forced to review the data, analyze the gaps, and think critically. **As the AI conducts research, you develop your own skills alongside it.**

---

## 🧠 The Philosophy: Human Responsibility in the Age of Autonomous Agents

It is 2026, and the industry trend is hyper-focused on "Agent AI"—building fully autonomous, zero-human-in-the-loop systems designed to replace human workflows entirely. While this level of automation works for repetitive tasks, **deep research cannot and should not be fully outsourced to a black box.**

* **The Accountability Gap:** Autonomous agents can search, calculate, and compile, but they cannot hold responsibility. If an AI generates a flawed analysis, the AI suffers zero consequences. **The final accountability and liability always rest on the human developer.**
* **The Problem with Black Boxes:** If an AI does 100% of the work in secret and hands you a finished file, **the human learns nothing.** When human jobs and skills disappear behind automated screens, we stop growing. A static report cannot teach an independent developer how to truly lead their project.
* **The Solution (Co-Learning & Oversight):** This skill explicitly rejects the "zero-human" hype. It treats research as an augmented partnership. By forcing human-gated checkpoints, you retain absolute strategic control. You review the data, track the calculations in open Jupyter Notebooks, and **develop your own expertise alongside the machine.**

---

## 🔄 The Human-in-the-Loop Is Always Yours to Control

These skills halt at gated checkpoints by design — but you are never locked in. At **any point** during a research session, you can:

* **Suspend** a sub-session and inspect its batch notes
* **Add comments** or redirect the agent mid-phase
* **Modify** the process, schema, or artifacts before the next step
* **Override** findings, adjust scope, or change direction
* **Do nothing** and accept — that is also a valid decision

The loop is yours. The AI proposes; you dispose. Whether you actively steer every phase or passively approve all suggestions, the choice is always in your hands.

---

## 📦 What's New — Upgrades from Real Research

Both skills were upgraded after being used in production research. culture-research v3.0 was rewritten based on consolidated feedback from **17 sub-sessions across a 46-paper, 6-region cultural study** and produced a validated demo report. deep-research v2.0 absorbed the same methodological discipline.

### culture-research v3.0 Highlights

| Feature | What It Does |
|---|---|
| **Science Communication Phase** (`09-report-writing.md`) | Generates a science magazine article, research brief, executive summary, and slide deck from the synthesis — with style calibration, sub-agent chapter writing, and HTML export |
| **Dual Evidence Model** | Every finding is tagged with `#evidence/{level}` **and** `#access/{type}` (full-text, abstract-only, metadata-only). Downstream analysis uses both fields — no more indistinguishable findings. |
| **Findings Index** (`findings-index.json`) | Machine-readable index alongside markdown entity files. Analysis rounds use this instead of re-reading 92+ finding files manually. |
| **Cross-Appraisal Consistency** | `papers/appraisals/_cross-appraisal-check.md` must exist before deep-read phase is complete — a 5-point checklist prevents skipped validation. |
| **Director Observations** | Every sub-session batch note includes a Director Observations section — aggregated methodology patterns tracked and fed back into the skill. |
| **File Truncation Safeguard** | Every file read checks for the 50KB cap. Critical end-of-file content (data tables, references) is no longer silently missed. |
| **Windows Encoding & Non-ASCII** | `ï`, `é`, `ü` in filenames and CJK content no longer cause inaccessible files. |
| **Sub-Theme Derivation Procedure** | Round 1 of multi-round analysis now uses a 3-step inductive procedure with granularity rules (4-8 per domain). |
| **Contradiction Identification Algorithm** | Round 3 replaced vague "find contradictions" with a deterministic matrix-scan → direction flag → entity verification pipeline. |
| **3-Tier Speculation Classification** | Checkpoint distinguishes evidence-derived, gap-derived, and speculative claims (replaces binary "speculative vs not"). |
| **state.json Synchronization** | Sub-sessions read `project-state.json` for current deliverable paths instead of trusting static prompt descriptions. |

### deep-research v2.0 Highlights

| Feature | What It Does |
|---|---|
| **End-Conditions Discipline** | Every phase has an explicit completion checklist. No more "I think it's done" — verifiable criteria for all 10 phases. |
| **Cross-Phase Gates** | 7 formal verification gates between phases: source verification, data validation, code validation, encoding check, parity check, HTML structure, cross-artifact consistency. |
| **File Truncation Safeguard** | After every file read, check for the 50KB cap. Critical EOF content is no longer missed. |
| **Non-ASCII Filename Handling** | Source filenames with `é`, `ü`, `ñ`, `ç`, CJK characters handled via `_filename_map.json`. |
| **State Synchronization** | `task_state.json` promoted from optional to recommended. Every phase end-condition includes a state update step. |
| **Skill Evolution Log** | Post-archive step produces `skill-evolution-log.md` entries — each completed change feeds back into skill improvement. |

---

## 📦 Repository Structure

```
.
├── deep-research/        # Core deep-research skill (v2.0)
│   ├── SKILL.md
│   ├── 01-explore.md … 10-implement.md
│   └── state-management.md
├── culture-research/     # Cultural / qualitative research skill (v3.0)
│   ├── SKILL.md
│   ├── 01-explore.md … 09-report-writing.md
│   └── 08-sub-session-orchestration.md (v3.0 update)
└── README.md
```

Each `SKILL.md` is the entry point; numbered `.md` files are phase-specific instructions the agent loads on demand.

---

## ✅ Prerequisites

1. **OpenCode** — the agent runtime. Initialize your local OpenCode environment first.
2. **OpenSpec** — the change/spec/task workflow. Your agent workspace must be able to read OpenSpec schemas.

You will also need a terminal capable of running `openspec init` (PowerShell, bash, or zsh).

---

## 🚀 Quick Start

### Step 1 — Initialize OpenSpec in your project folder
Your agent workspace must be prepared to track research states before deploying the skills.
```bash
openspec init
```

### Step 2 — Create the OpenCode Skill Directories
OpenCode reads skills from independent, isolated subdirectories. Create the required directory trees:

**Windows (PowerShell)**
```powershell
New-Item -ItemType Directory -Path ".opencode\skills\deep-research", ".opencode\skills\culture-research" -Force
```

**macOS / Linux (bash)**
```bash
mkdir -p .opencode/skills/deep-research .opencode/skills/culture-research
```

### Step 3 — Populate the Skill Files and Components
Copy your skill files into their respective subdirectories. OpenCode's parser will strictly ignore folders that lack valid YAML frontmatter headers and `skill.json` files.

#### For Deep Research (`.opencode/skills/deep-research/`):
1. Copy all `deep-research/` files into `.opencode/skills/deep-research/`.
2. Ensure your `SKILL.md` file starts with this exact YAML block:
```markdown
---
name: deep-research
description: "Topic-agnostic quantitative and qualitative research with code-first analysis."
---
```
3. Create a `skill.json` file in that folder:
```json
{
  "id": "deep-research",
  "version": "2.1",
  "entrypoint": "SKILL.md"
}
```

#### For Culture Research (`.opencode/skills/culture-research/`):
1. Copy all `culture-research/` files into `.opencode/skills/culture-research/`.
2. Ensure your `SKILL.md` file starts with this exact YAML block:
```markdown
---
name: culture-research
description: "Cultural and behavioral qualitative studies with region-parallel search loops."
---
```
3. Create a `skill.json` file in that folder:
```json
{
  "id": "culture-research",
  "version": "3.1",
  "entrypoint": "SKILL.md"
}
```

### Step 4 — Authorize Execution Permissions
Open your local `opencode.json` configuration file and explicitly allow your newly added custom skill IDs to bypass agent security filters:
```json
{
  "agent": {
    "allowed_skills": [
      "deep-research",
      "culture-research"
    ]
  }
}
```

### Step 5 — Trigger the Skill
Restart your active OpenCode TUI or terminal environment to flush the index cache. You can now invoke your custom research workflows directly using explicit skill targeting flags:

**Example — Run Culture Research Workflow:**
> "Initialize a research project on 'human daily behavior variations' using skill: culture-research"

**Example — Run Deep Research Workflow:**
> "Analyze 'open-source vector database performance matrices' using skill: deep-research"


---

## 🔄 The 6-Phase Pattern (deep-research)

```
[ User Query ]
    │
    ▼
┌──────────────┐   ┌──────────────┐   ┌─────────────────┐   ┌────────────────┐
│  proposal.md │ → │    specs/    │ → │ notebooks/*.ipynb│ → │  /dist/        │
└──────────────┘   └──────────────┘   └─────────────────┘   └────────────────┘
 (The Strategy)     (The Schema)       (Trackable Labs)      (index.html Web)
                          │                  ▲                     ▲
                          ▼                  │                     │
                [ HUMAN INTERACTION ] ───────┴─────────────────────┘
               (Verify & Learn Schema)    (Manual adjustments anytime)
```

1. **Query Deconstruction** — parse intent, isolate variables, surface knowledge gaps.
2. **Strategy Proposal** — high-level blueprint of domains, sources, and investigation paths.
3. **Schema & Spec Mapping** — build the target grid. **🛑 Human gate.**
4. **Targeted Web Discovery** — parallel search agents index sources into a local Knowledge Base.
5. **Notebook-Driven Analysis** — fully transparent Jupyter notebooks. You can read and re-run every cell.
6. **Artifact Synthesis** — a self-contained, browser-openable `index.html` report.

---

## 🧭 The Culture-Research Pattern

```
Explore → Search Design → Region-Parallel Search → Acquisition
                                              │
                                              ▼
                                Deep Reading (1 sub-session per region)
                                              │
                                              ▼
                              Knowledge Base (entities + relations)
                                              │
                                              ▼
                          Round 1: Thematic  →  Round 2: Cross-Cultural
                          Round 3: Contradictions →  Round 4: Gaps
                          Round 5: Research Questions
                                              │
                                              ▼
                              Iteration Checkpoint  ←── loop back if weak
                                              │
                                              ▼
                                  Synthesis Document
                                                  │
                                                  ▼
                              Science Communication
                              (article, brief, summary, slide deck)
                              ←── NEW in v3.0
```

Supports projects with 20+ papers via sub-session orchestration — each sub-session has explicit end-conditions, batch notes, and file persistence to the same project directory.

---

## 🧭 Ongoing Evolution

These skills are not static. Every research project that uses them generates feedback:

- **Weak spots** found during review are fixed at the phase level
- **Methodology gaps** discovered during analysis are codified into new principles
- **Director Observations** from sub-sessions accumulate into `skill-evolution-log.md` entries
- Each post-archive step produces documented improvements that feed back into the skill itself

The more you research with these skills, the sharper they become.

---

## 🎯 When to Use vs. When to Skip

### ✅ Great fit
- Market / competitor matrix mapping
- New technology or protocol deep-dive
- Literature and documentation audits
- Cultural / behavioral qualitative studies
- Bilingual (EN/ZH) research reports with website output

### ❌ Not a fit
- Single-fact Q&A ("what is the capital of X?")
- Creative writing, brainstorming, naming
- Quick debugging or instant code fixes
- Time-critical answers (the human gate is intentional, not a bug)

---

## ⚠️ Disclaimer

This project is an **experimental, independent-developer** project shared publicly for educational and collaborative purposes.

> **Use at your own risk.** No guarantees or warranties are provided regarding stability, security, API cost / token management, or performance. OpenCode and OpenSpec update frequently outside this project — breaking changes may occur. Anyone adapting or executing these skills in their own agent environments assumes full responsibility for any outcomes.

## 📄 License

MIT — see [LICENSE](LICENSE).
