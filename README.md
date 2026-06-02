# Human-in-the-Loop Deep Research Skills

A collection of structured, artifact-driven AI research skills for **OpenCode** + **OpenSpec** environments. Every skill in this repository is built around a single principle: **the human stays in the loop, learns alongside the AI, and never receives a finished black box.**

This repository currently ships two skills:

| Skill | Folder | Best for |
|---|---|---|
| **deep-research** | `deep-research/` | Topic-agnostic, quantitative + qualitative research with code-first analysis, Jupyter notebooks, and bilingual website output |
| **culture-research** | `culture-research/` | Cultural / behavioral one-off studies: paper collection, deep reading, knowledge graph, multi-round qualitative analysis, Obsidian vault |

---

## 🧠 Core Philosophy

In an industry racing toward "zero-human-in-the-loop" autonomous agents, these skills intentionally reject that pattern.

* **No black boxes.** Every factual output cites verbatim source text. Every calculation is executed in code you can inspect. Every schema is a checkpoint you can revise.
* **Human-gated checkpoints.** The AI proposes, the human disposes. The skill halts at decision points (proposal review, schema approval, iteration checkpoint) and waits for you.
* **Co-learning by design.** Because you review the data, tweak the schema, and adjust the analysis cells, you develop real expertise — not just a deliverable file.
* **Full data ownership.** All sources, notebooks, and intermediate artifacts stay in your local folder. Nothing is locked in a vendor cloud.

---

## 📦 Repository Structure

```
.
├── deep-research/        # Core deep-research skill (v4.1)
│   ├── SKILL.md
│   ├── 01-explore.md … 10-implement.md
│   └── state-management.md
├── culture-research/     # Cultural / qualitative research skill (v2.0)
│   ├── SKILL.md
│   └── 01-explore.md … 08-sub-session-orchestration.md
└── README.md             # ← you are here
```

Each `SKILL.md` is the entry point; numbered `.md` files are phase-specific instructions the agent loads on demand.

---

## ✅ Prerequisites

Install the two external projects this skill depends on. **Always follow their official docs for the latest setup steps** — both move fast.

1. **OpenCode** — the agent runtime. Initialize your local OpenCode environment first.
2. **OpenSpec** — the change/spec/task workflow. Your agent workspace must be able to read OpenSpec schemas.

You will also need a terminal capable of running `openspec init` (PowerShell, bash, or zsh).

---

## 🚀 Quick Start

### Step 1 — Initialize OpenSpec in your project folder

Open a terminal **inside the folder where you want the research to live** and run:

```bash
openspec init
```

This creates the `openspec/` directory, scaffolds the change/spec/task structure, and registers the workflow with your OpenCode agent.

### Step 2 — Copy the skills into your OpenCode skills folder

Copy **whichever skill(s) you need** into `.opencode\skills\` (Windows) or `.opencode/skills/` (macOS/Linux) at the root of your project:

**Windows (PowerShell)**

```powershell
# Copy both skills
Copy-Item -Recurse ".\deep-research" ".opencode\skills\deep-research"
Copy-Item -Recurse ".\culture-research" ".opencode\skills\culture-research"

# Or just one
Copy-Item -Recurse ".\culture-research" ".opencode\skills\culture-research"
```

**macOS / Linux (bash)**

```bash
# Copy both skills
cp -R ./deep-research      .opencode/skills/deep-research
cp -R ./culture-research  .opencode/skills/culture-research

# Or just one
cp -R ./culture-research  .opencode/skills/culture-research
```

After copying, your project tree should look like:

```
your-project/
├── .opencode/
│   └── skills/
│       ├── deep-research/
│       └── culture-research/
├── openspec/                # ← created by `openspec init`
└── ...
```

### Step 3 — Trigger the skill from a prompt

Open your OpenCode agent and send a prompt that names the skill and the topic. The agent will load the skill's `SKILL.md` and route phase by phase.

**Example A — culture research**

```text
analysis topic "study human daily behavior",
1. using skill .opencode\skills\culture-research
2. using skill openspec to initial the project.
```

**Example B — deep research (topic-agnostic)**

```text
analysis topic "compare 10 open-source vector databases for production use",
1. using skill .opencode\skills\deep-research
2. using skill openspec to initial the project.
3. stop at the schema/spec gate — I want to review the comparison matrix before you collect data.
```

The agent will:

1. Run `openspec init` if not already done.
2. Load the named skill's `SKILL.md`.
3. Walk through the phases, halting at human-gated checkpoints.
4. Write all intermediate artifacts (sources, notebooks, knowledge base, proposals, specs) into your local project folder.

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
```

Designed for projects with >20 papers via sub-session orchestration — each sub-session has explicit end-conditions, batch notes, and file persistence to the same project directory.

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
