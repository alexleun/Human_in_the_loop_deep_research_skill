---
name: frontier-research
description: "A large-scale, multi-session research workflow for engineering, science, and frontier/emerging technology topics, applying Systems Thinking, Critical Thinking & Anti-Bias, and Epistemic First Principles & Triangulation to combat AI hallucination, confirmation bias, and premature convergence."
---

# Frontier Research Skill

A large-scale research workflow purpose-built for **engineering, science, and frontier/emerging technology** studies. Uses multi-agent sub-session orchestration on spec-driven platforms (e.g. opencode), integrating **Systems Thinking**, **Critical Thinking & Anti-Bias**, and **Epistemic First Principles & Triangulation** to combat AI hallucinations, confirmation bias, and premature convergence — producing high-credibility, forward-looking technical reports.

**v1.0 (NEW):** First release. Ten-phase protocol with an explicit **Phase 5: Epistemic Stress-Test & Systems Mapping** gate (reusing the culture-research v3.3 methodology — Axiomatic Audit, Steelman Red Team, Causal Loop & Emergence Mapping, CCS routing) plus a **Phase 7: Mid-Term Alignment & User Calibration** gate. Introduces three core mental frameworks, source-agnostic harvesting with trust weighting, and three anti-hallucination guardrails. See `05-epistemic-stress-test.md` and the v1.0 CHANGELOG entry.

---

## When to Use This Skill

- Topic is **engineering, science, or frontier/emerging technology** — e.g. scaling laws, thermal management, hardware architectures, new protocols, materials, algorithms
- Goal is a **comprehensive technical report** with forward-looking trajectory, trade-off analysis, and engineering recommendations
- The analysis can benefit from **systems thinking** and **first-principles** reasoning, not just literature review
- Evidence must be **multi-source triangulated** (papers + code + datasets + patents + web)

**How this differs from the sibling skills:**

| Skill | Best For | Failure Modes Targeted |
|---|---|---|
| **culture-research** | Cultural / behavioral qualitative studies (papers + Obsidian vault) | Unexamined cultural assumptions, thin synthesis |
| **deep-research** | Code-first quantitative research with Jupyter notebooks + website output | Encoding/parity bugs, memorized numbers |
| **frontier-research** | Engineering / science / frontier-tech technical reports | **AI hallucination, confirmation bias, premature convergence** |

Not for: single-fact Q&A, purely cultural/qualitative studies (use culture-research), or quantitative pipelines that must produce runnable notebooks/dashboards (use deep-research).

---

## Core Mental Frameworks

The skill forces three complementary thinking models into every phase. Together they form the **Frontier Research Cognitive Engine**.

```
+----------------------------------------------------------------------------------+
|                       Frontier Research Cognitive Engine                         |
+----------------------------------------------------------------------------------+
| 1. SYSTEMS THINKING                                                              |
|    - Causal Loop Diagrams (reinforcing R / balancing B feedback)                 |
|    - Stocks & Flows (accumulation/depletion dynamics)                            |
|    - Feedback Loops, Bottlenecks & Emergent Behavior                             |
+----------------------------------------------------------------------------------+
| 2. CRITICAL THINKING & ANTI-BIAS                                                |
|    - Premise Verification (do not trust user/paper assumptions blindly)          |
|    - Red Teaming / Steel-Manning (attack the mainstream; strengthen the ignored)  |
|    - Counterfactual Analysis (what if a core assumption fails?)                  |
+----------------------------------------------------------------------------------+
| 3. EPISTEMIC FIRST PRINCIPLES & TRIANGULATION                                   |
|    - Epistemic Status Labeling: [Fact] / [Hypothesis] / [Speculation]           |
|    - Physical & Mathematical Consistency (feasibility constraints)              |
|    - Multi-Source Triangulation (>= 2 independent sources per technical claim)    |
+----------------------------------------------------------------------------------+
```

- **Systems Thinking** drives Phases 1 (system mapping), 5 (causal-loop mapping in the stress-test), and 8 (convergence trade-offs).
- **Critical Thinking & Anti-Bias** drives Phases 4 (red-teaming), 5 (steelman module), and 10 (self-audit).
- **Epistemic First Principles & Triangulation** drives Phases 3 (epistemic ledger) and 5 (axiomatic audit).

---

## Anti-Hallucination Guardrails

These are **mandatory, cross-session** constraints that apply to every sub-session regardless of phase:

1. **Calculations First.** Any mathematical, physical, or economic derivation/unit-conversion must be computed in an explicit standalone step. Do **not** output an uncomputed value as if it were derived.
2. **Citation Requirement.** Every performance metric or technical claim in the final output must carry a citation with source and an epistemic tag (e.g. `[Fact: ArXiv 2401.xxxx]` or `[Hypothesis: Lab Benchmark]`).
3. **Uncertainty Quantification.** When data is missing or contradictory, do **not** sycophantically guess. Explicitly output `[DATA DEFICIT: Requires Empirical Testing]` and mark the claim unverified.

---

## Phase Router

| Current Task | Load This File |
|---|---|
| Decomposing the topic, mapping variables/causal loops/boundaries | `01-system-map.md` |
| Ingesting multi-source data (papers/code/datasets/patents/web) + trust manifest | `02-harvest.md` |
| Fact-checking, triangulating, labeling [Fact]/[Hypothesis]/[Speculation] into ledger | `03-epistemic-ledger.md` |
| Verifying premises, red-teaming mainstream routes, steel-manning alternatives | `04-red-team.md` |
| **Running the epistemic stress-test: axiomatic audit + steelman + systems mapping (gate)** | **`05-epistemic-stress-test.md`** |
| Generating divergent/cross-domain/counterfactual innovation candidates | `06-generative-synthesis.md` |
| Presenting intermediate findings, calibrating to user constraints | `07-calibration.md` |
| First-principles derivation + quantified trade-off matrix | `08-deep-convergence.md` |
| Drafting the full report with Discovery-First narrative + grounded citation | `09-report-drafting.md` |
| Self-correcting: scanning for speculation-mislabeled-as-fact, finalizing deliverable | `10-self-audit.md` |

---

## State Model (project-state.json)

Large projects maintain cross-session state in a `project-state.json` at the project root:

```json
{
  "project_id": "frontier-res-001",
  "topic": "frontier tech research topic",
  "domain": "Engineering/Physics/AI/BioTech",
  "current_phase": "03-epistemic-ledger.md",
  "user_constraints": {
    "target_deliverable": "Comprehensive Technical Report",
    "special_focus": ["Scaling Laws", "Thermal Management"],
    "accepted_sources": ["ArXiv", "Patents", "Code Repos", "Raw CSV", "Web"]
  },
  "epistemic_ledger": {
    "verified_facts": [],
    "unverified_claims": [],
    "falsified_hypotheses": []
  },
  "sub_sessions": [
    {
      "phase_id": 1,
      "name": "Problem Space & System Mapping",
      "status": "completed",
      "outputs": ["access/01-system-map.md"]
    }
  ]
}
```

- **`user_constraints`** is updated at the **Phase 7 calibration gate** based on real-world conditions (budget, timeline, engineering preference).
- **`epistemic_ledger`** tracks `verified_facts`, `unverified_claims`, and `falsified_hypotheses` across sessions; downstream phases must honor these statuses.
- Multi-session resume reads `current_phase` and the ledger to continue without re-deriving prior decisions.

---

## Workflow Overview

```
Topic-Intent & Sector Analysis (frontier / engineering / science)
       │
       ▼
Phase 1: Topic Deconstruction & System Mapping   (SYSTEMS THINKING)
       │  → access/01-system-map.md
       ▼
Phase 2: Multi-Source Data Harvesting           (SOURCE-AGNOSTIC)
       │  → raw_data/ + access/02-source-manifest.json
       ▼
Phase 3: Epistemic Fact-Checking & Triangulation (EPISTEMIC FIRST PRINCIPLES)
       │  → evidence/03-epistemic-ledger.md  ([Fact]/[Hypothesis]/[Speculation])
       ▼
Phase 4: Critical Thinking & Red-Teaming        (CRITICAL THINKING & ANTI-BIAS)
       │  → evidence/04-red-team-analysis.md
       ▼
Phase 5: EPISTEMIC STRESS-TEST & SYSTEMS MAPPING  ←── DESTRUCTIVE GATE
          (Axiomatic Audit + Steelman + Causal Loops; CCS routing → Mode A/B)
       │  → evidence/05-stress-tested-matrix.json  (authoritative Reduce input)
       ▼
Phase 6: Generative Synthesis & Divergent Thinking (LATERAL / CROSS-DOMAIN)
       │  → evidence/06-innovative-synthesis.md
       ▼
Phase 7: Mid-Term Alignment & User Calibration    ←── HUMAN CALIBRATION GATE
       │  → project-state.json (user_constraints updated)
       ▼
Phase 8: Deep Analytical Convergence             (FIRST PRINCIPLES + TRADE-OFFS)
       │  → evidence/08-deep-convergence.md
       ▼
Phase 9: Comprehensive Report Drafting           (DISCOVERY-FIRST + CITED)
       │  → drafts/09-full-report-draft.md
       ▼
Phase 10: Self-Correction Audit & Finalization   (ADVERSARIAL PROOFREADING)
          → FINAL_DELIVERABLE_REPORT.md
```

Guardrails (Calculations First, Citation Requirement, Uncertainty Quantification) apply at every phase, including every sub-session.

---

## End-Conditions Discipline & Sub-Session Orchestration

Every phase and every sub-session defines its **end conditions** as a checklist, not a description:

```markdown
## End Conditions
This phase is **complete** when ALL of the following are true:
1. ✅ [Specific deliverable exists at specific path]
2. ✅ [Quality criterion met]
3. ✅ [Coverage criterion met]
4. ✅ [Format/validation criterion met]
5. ✅ [Batch note appended]
```

- **Sub-sessions** are used for large/parallel work (>20 sources or heavy token loads). Each sub-session has tight scope, explicit end conditions, and appends a **batch note** (what was produced, open issues, honest quality assessment).
- The main session acts as **project manager**: reads batch notes, spot-checks outputs, and logs a PROCEED / LOOP / PAUSE decision.
- Cross-phase gates produce **accountable artifacts** (e.g., the stress-tested matrix, the calibration sign-off) that downstream phases reference rather than trusting static prompts.
