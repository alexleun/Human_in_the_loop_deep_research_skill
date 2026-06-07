# Human-in-the-Loop Research Skills

A collection of structured, artifact-driven AI research skills for **OpenCode** environments. Every skill in this repository is built around a single principle: **the human stays in the loop, learns alongside the AI, and never receives a finished black box.**

This repository currently ships two skills, both validated through real research projects:

| Skill | Folder | Version | Best for |
|---|---|---|---|
| **deep-research** | `deep-research/` | v2.1 | Topic-agnostic, quantitative + qualitative research with code-first analysis, Jupyter notebooks, and bilingual website output |
| **culture-research** | `culture-research/` | v3.2 | Cultural / behavioral one-off studies: paper collection, deep reading, knowledge graph, multi-round qualitative analysis, Obsidian vault |

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

Both skills were upgraded after being used in production research. culture-research v3.2 incorporates lessons from a 38-paper, 3-region pain-and-culture study including a failed-first-draft report-writing cycle that drove the Discovery-First Framing principle. deep-research v2.1 absorbed methodological discipline from the same lineage.

### culture-research v3.2 Highlights (v3.0 → v3.1 → v3.2)

#### v3.0 Foundation
| Feature | What It Does |
|---|---|
| **Science Communication Phase** (`09-report-writing.md`) | Generates a science magazine article, research brief, executive summary, and slide deck from the synthesis — with style calibration, sub-agent chapter writing, and HTML export |
| **Dual Evidence Model** | Every finding is tagged with `#evidence/{level}` **and** `#access/{type}` (full-text, abstract-only, metadata-only). Downstream analysis uses both fields — no more indistinguishable findings. |
| **Findings Index** (`findings-index.json`) | Machine-readable index alongside markdown entity files. Analysis rounds use this instead of re-reading 92+ finding files manually. |
| **Cross-Appraisal Consistency** | `papers/appraisals/_cross-appraisal-check.md` must exist before deep-read phase is complete — a 5-point checklist prevents skipped validation. |
| **Director Observations** | Every sub-session batch note includes a Director Observations section — aggregated methodology patterns tracked and fed back into the skill. |
| **File Truncation Safeguard** | Every file read checks for the 50KB cap. Critical end-of-file content (data tables, references) is no longer silently missed. |
| **Windows Encoding & Non-ASCII** | `ï`, `é`, `ü` in filenames and CJK content no longer cause inaccessible files. |
| **Sub-Theme Derivation Procedure** | Round 1 uses a 3-step inductive procedure with granularity rules (4-8 per domain). |
| **Contradiction Identification Algorithm** | Round 3 replaced vague "find contradictions" with a deterministic matrix-scan → direction flag → entity verification pipeline. |
| **3-Tier Speculation Classification** | Checkpoint distinguishes evidence-derived, gap-derived, and speculative claims (replaces binary). |
| **state.json Synchronization** | Sub-sessions read `project-state.json` for current deliverable paths instead of trusting static prompt descriptions. |

#### v3.1 Additions
| Feature | What It Does |
|---|---|
| **Source Preservation** | Fetching any paper content requires saving a local copy (`papers/raw/`) before extraction — findings remain verifiable after URLs go offline. |
| **Sub-Session Execution Modes** | Two formal modes: human-executed (prompt written to disk, human launches) vs LLM-executed (agent launches via task tool). Decision tree included. |
| **PM Review Loop** | After each sub-session, PM reads batch note, spot-checks output, updates state, logs PROCEED/LOOP/PAUSE decision. Prevents undetected quality drift. |
| **Scale-Dependent MCP Guidance** | < 50 entities → MCP tools, 50–500 → write files + JSON, 500+ → add batch-import script. Prevents tool-bottleneck on large knowledge bases. |
| **Generational / Time-Period Dimension** | Optional `time_period` field on `cultural_context` entities; `#generation/{cohort}` tag taxonomy. Enables cross-generational comparison. |

#### v3.2 Additions
| Feature | What It Does |
|---|---|
| **Discovery-First Framing** | Report-writing outputs must lead with claims about the world, not the research process. Methodology relegated to a single endnote. Prevents the "reads as a lit review" failure mode. |
| **Human-Approval Gates** | Formal gates after Explore (question), Checkpoint (verdict), Synthesis (document), and Report Writing (section plan) require explicit human sign-off before proceeding. |
| **Pre-Writing Section Plan Gate** | Before drafting any chapter, the human must approve a section plan (titles, narrative arc, key claims). Catches misaligned voice before it propagates. |
| **Style Calibration Heuristics** | Concrete, checkable style profiles for Aeon, The Atlantic, Sapiens, and Nature News — sentence length, paragraph structure, opening patterns, citation style. |
| **Variable-Length Planning** | Long-form articles (5,000–10,000 words) use a density planning table (tight 200-word sections to expansive 1,000-word sections) instead of the fixed 400-500 word template. |
| **Unfindable Paper Protocol** | 5-minute timebox per unfindable paper; minimal appraisal with `no-abstract-available`; no replacement. Prevents time sinks while maintaining honest coverage. |
| **Project Sizing Guide** | Small (5 SS, 1–2 regions), Medium (13–15 SS, 3–4 regions, recommended), Large (18–22 SS, 5–6 regions), Exhaustive (25+ SS). Replaces the fixed 15-SS sequence. |
| **Calibration Run for Analysis Rounds** | Test Round 1 on one domain, Round 2 on 2–3 rows, Round 3 on 1–2 cells before scaling. Prevents format drift across large outputs. |

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
├── culture-research/     # Cultural / qualitative research skill (v3.2)
│   ├── SKILL.md
│   ├── 01-explore.md … 09-report-writing.md
│   └── 08-sub-session-orchestration.md (v3.2 update)
└── README.md
```

Each `SKILL.md` is the entry point; numbered `.md` files are phase-specific instructions the agent loads on demand.

---

## ✅ Prerequisites

1. **OpenCode** — the agent runtime. Initialize your local OpenCode environment first.

---

## 🚀 Quick Start

### Step 1 — Copy the skills into your OpenCode skills folder

**Windows (cmd/PowerShell)**

```powershell
Copy-Item -Recurse ".\deep-research" ".opencode\skills\deep-research"
Copy-Item -Recurse ".\culture-research" ".opencode\skills\culture-research"
```

**macOS / Linux (bash)**

```bash
cp -R ./deep-research     .opencode/skills/deep-research
cp -R ./culture-research  .opencode/skills/culture-research
```

### Step 2 — Trigger the skill from a prompt

**Example — culture research**

```text
analysis topic "study human daily behavior",
using skill .opencode\skills\culture-research
```

**Example — deep research**

```text
analysis topic "compare 10 open-source vector databases for production use",
using skill .opencode\skills\deep-research
```

The agent will load the skill's `SKILL.md`, walk through the phases halting at human-gated checkpoints, and write all intermediate artifacts to your local project folder.

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

> **Use at your own risk.** No guarantees or warranties are provided regarding stability, security, API cost / token management, or performance. OpenCode update frequently outside this project — breaking changes may occur. Anyone adapting or executing these skills in their own agent environments assumes full responsibility for any outcomes.

## 📄 License

MIT — see [LICENSE](LICENSE).
