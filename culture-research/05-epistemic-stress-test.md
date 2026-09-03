# Phase 5: Epistemic Stress-Test & Systems Mapping (NEW in v3.3)

**Purpose:** Destructively verify all extracted evidence before any narrative reduction begins. Combats AI hallucinations, confirmation bias, and premature convergence by applying epistemic first principles, critical thinking, and systems thinking to the evidence base produced by the Knowledge Base phase.

**Position in workflow:** Immediately after Knowledge Base (Phase 4, SHUFFLE) and before Multi-Round Analysis (Phase 6, first REDUCE dispatch). The phase reads the shuffled `findings-index.json` + evidence library and outputs a validated `stress-tested-matrix.json` that downstream Reduce phases are **prohibited** from ignoring.

**Execution pattern:** Run as an Audit Sub-session when sub-session orchestration is active (>20 papers) — positioned between the Knowledge Base sub-sessions and the Multi-Round Analysis theme sub-sessions. For small projects, run inline as a single phase.

---

## 1. Overview & Objective

Traditional AI-driven qualitative research workflows suffer from three systemic failure modes during the synthesis phase:

1. **AI Hallucinations (Epistemic Drift):** Model-generated logical leaps or unsubstantiated claims created when bridging factual gaps between extracted findings.
2. **Confirmation Bias (Selective Synthesis):** Over-weighting evidence that supports the initial hypothesis while ignoring boundary conditions, edge cases, and counter-evidence.
3. **Premature Convergence (Imagination Bottleneck):** Defaulting to linear, trivial, or surface-level summaries instead of surfacing complex systemic dynamics.

Phase 5 acts as a **destructive verification and dynamic mapping gateway** between the Evidence Library (Phase 4) and Multi-Round Analysis (Phase 6). By applying **Epistemic First Principles**, **Critical Thinking (Red Teaming)**, and **Systems Thinking**, this phase stress-tests all extracted evidence before any final narrative is written.

```
┌──────────────────┐      ┌──────────────────────────────────────────────┐      ┌──────────────────┐
│ Phase 4: KB      │ ──►  │ Phase 5: Epistemic Stress-Test & Systems     │ ──►  │ Phase 6:         │
│ (SHUFFLE -       │      │            Mapping (Destructive Audit)       │      │ Multi-Round      │
│  findings-index) │      └──────────────────────────────────────────────┘      │ Analysis (REDUCE)│
└──────────────────┘                                                             └──────────────────┘
```

---

## 2. Core Methodological Framework

### Module 1: Axiomatic Audit (Epistemic First Principles)

**Goal:** Eliminate hallucinations and unsupported leaps.

**Mechanism:** Deconstruct every extracted insight into two atomic components:

- **Raw Evidential Axioms:** Direct quotes or hard data tied to concrete source tags (e.g., `[Paper_A: p.12]`).
- **Inference Chains:** The logical steps connecting axioms to conclusions.

**Classification:** Each claim is assigned one of three epistemic statuses:

| Status | Meaning | Action |
|---|---|---|
| **Verified_Axiom** | Traces directly to a verifiable raw evidential axiom with a complete inference chain | Eligible for primary evidence pool |
| **Inferred_Bridge** | Has some evidential support but requires intermediate logical steps not directly present in evidence | Eligible but with reduced confidence and an explicit flag |
| **Unsubstantiated_Speculation** | Lacks a verifiable axiom or contains a gap in its inference chain | **Excluded** from the primary evidence pool; flagged High-Risk Assumption |

**Example:**
- *Verified Axiom:* "Aggressive promotional discounts yield short-term revenue spikes but erode long-term customer lifetime value." → `[Doc_A: p.14]`, `[Doc_C: p.08]`
- *Inferred Bridge:* "Price sensitivity anchoring drives churn." (plausible but requires assumption not directly measured)
- *Unsubstantiated Speculation:* "Customers will return once discounts stop." (no source tag)

**Action:** Any statement lacking a verifiable axiom or containing a gap in its inference chain is flagged as a High-Risk Assumption and stripped from the primary evidence pool, remaining visible only in the synthesis directives as an excluded claim.

### Module 2: Steelman Red Teaming (Critical Thinking)

**Goal:** Eradicate confirmation bias.

**Mechanism:** Instantiate an adversarial analysis that constructs the strongest possible counter-arguments to emerging findings.

**Action:**
- Identify alternative explanations that fit the same data (competing hypotheses)
- Search specifically for edge cases, anomalies, and boundary conditions
- Formulate the **Steelman Counter-Hypothesis** — the strongest possible version of the opposing argument
- Ask the defining question: *"What data should be present if the primary claim holds true — and is it missing?"*

**Integration with the dual evidence model (Principle 10):** Red team output must respect `#access/{type}` and `#evidence/{level}`. A Steelman counter-hypothesis grounded in an `access/abstract-only` paper carries `evidence/low` weight; a counter-hypothesis derived purely from reasoning with no evidential anchor is labeled explicitly as "reasoning-based, not evidence-anchored."

**Example:**
- *Dominant hypothesis:* "Brand equity degrades due to price sensitivity anchoring."
- *Steelman counter-hypothesis:* "Churn is driven by operational onboarding failures during promotional rushes, not price anchoring."
- *Boundary condition:* "Applies only to B2B SaaS models with onboarding times > 14 days."

### Module 3: Causal Loop & Emergence Mapping (Systems Thinking)

**Goal:** Overcome premature convergence and surface non-intuitive insights.

**Mechanism:** Shift from linear causality (*A*→*B*) to feedback dynamics.

**Action:**
- Identify **Reinforcing Loops (*R*)** — compounding mechanisms (e.g., `R1_Discount_Dependency`)
- Identify **Balancing Loops (*B*)** — stabilizing/resisting mechanisms (e.g., `B1_Support_Capacity_Cap`)
- Pinpoint **Time Delays** between causes and systemic effects
- Locate **Non-Intuitive Leverage Points** where small interventions yield disproportionate systemic shifts

**Labeling convention:** Use `R1`, `R2`, `B1`, `B2` with descriptive suffixes. Each loop maps a set of `nodes` (variables) connected in a feedback cycle. Incentivize the auditor to look beyond single-loop linear reasoning.

**Example:**
```
R1_Discount_Dependency: [Promotions] → [Short-term Sales Target] → [Baseline Price Fatigue] → [Higher Promo Need] → [Promotions]
B1_Support_Capacity_Cap: [Promo Traffic] → [Support Ticket Volume] → [Customer Satisfaction Drop] → [Churn]
Leverage point: "Shift incentive structure from user acquisition volume to Day-90 active retention."
```

---

## 3. Step-by-Step Execution Protocol

```
                       [ Execute Phase 5 Audit ]
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │ Calculate Cognitive Complexity   │
                    │ Score (CCS: 1 - 10)              │
                    └──────────────────────────────────┘
                                     │
                    ┌────────────────┴─────────────────┐
                    ▼                                  ▼
        CCS < 6 OR Auto Mode               CCS ≥ 6 AND Interactive
     ┌───────────────────────────┐        ┌───────────────────────────┐
     │     MODE A: AUTOMATED     │        │    MODE B: STRATEGIC HITL │
     │ - Seal Matrix             │        │ - Present 2-3 Forks       │
     │ - Append Limitations      │        │ - User Selects Route      │
     └─────────────┬─────────────┘        └─────────────┬─────────────┘
                   │                                    │
                   └─────────────────┬──────────────────┘
                                     │
                                     ▼
                      [ Write stress-tested-matrix.json ]
                                     │
                                     ▼
                   [ Proceed to Phase 6: Multi-Round Analysis ]
```

### Step 1: Input Ingestion

Read all extracted evidence files from `knowledge-base/findings-index.json` and the `knowledge-base/entities/finding/` evidence library generated during Phase 4. Do **NOT** re-read raw paper appraisals or search logs — the shuffled findings index is the authoritative input.

### Step 2: Automated Tri-Analysis Pipeline

Run the three analysis modules in sequence:

1. **Axiomatic Deconstruction:**
   - Validate all claims against evidence source tags
   - Classify evidence into: Verified_Axiom, Inferred_Bridge, or Unsubstantiated_Speculation
   - Record `inference_confidence` per claim (0.0–1.0)

2. **Steelman Counter-Analysis:**
   - Generate counter-hypotheses for every major cluster
   - Evaluate what data *should* be present if the main hypothesis is true, and flag missing signals

3. **Systems Loop Mapping:**
   - Build a dynamic system map outlining feedback loops (*R1*, *R2*, *B1*, *B2*), time delays, and systemic bottlenecks

### Step 3: Compute Cognitive Complexity Score (CCS)

Calculate the **Cognitive Complexity Score (CCS)** on a scale from 1 to 10 based on three metrics:

| Metric | Definition | Weight |
|---|---|---|
| **Contradiction Density** | Ratio of conflicting data points vs. aligned data points | ×3.5 |
| **Chain Length** | Average inferential steps required to link raw data to core conclusions | ×0.3 |
| **Systemic Coupling** | Number of feedback loops identified across variables | ×0.8 |

**Formula:** `CCS = min(10, Contradiction_Density × 3.5 + Chain_Length × 0.3 + Loop_Count × 0.8)`

**Worked example:** With Contradiction_Density = 1.2, Chain_Length = 4, and Loop_Count = 3:
`CCS = min(10, 1.2×3.5 + 4×0.3 + 3×0.8) = min(10, 4.2 + 1.2 + 2.4) = min(10, 7.8) = 7.8`

> **Note:** The CCS is a **routing heuristic**, deciding only *how* interaction happens (automated vs. strategic HITL), not a measure of correctness. For qualitative research it is reasonably estimated by the auditor; for quantitative workflows (see deep-research adaptation) it should be computed by script.

### Step 4: Routing & Execution (Adaptive Human-in-the-Loop)

#### Condition A: Fully Automated Mode (Mode A)

**Trigger:** *CCS* < 6, OR user explicitly sets `--mode=auto`, OR the task complexity exceeds standard human cognitive processing limits without domain expertise.

**Execution:**
1. The AI automatically resolves minor logical conflicts using maximum evidential rigor
2. Generates `stress-tested-matrix.json`
3. Mandates that the Synthesis phase (Phase 8) include a dedicated **"Epistemic Limitations & Systemic Blindspots"** chapter

#### Condition B: Strategic Human-in-the-Loop (Mode B)

**Trigger:** *CCS* ≥ 6 AND interactive mode enabled.

**Execution Rule:** **Do NOT present micro-level edits or raw data validation requests.** Present only high-level **Strategic Narrative Forks**. The user is selecting a *routing/strategy* decision, never making micro-level content edits.

**Interaction Template Prompt:**

```
================================================================================
Phase 5 Epistemic Audit Complete
Cognitive Complexity Score: [CCS Value]/10
Execution Mode: Strategic_HITL
================================================================================

A structural contradiction was detected in the evidence base.

- Dominant Finding: [Summary of mainstream interpretation]
- Systemic Blindspot / Counter-Evidence: [Summary of Red Team finding & feedback loops]

Please select the strategic direction for final synthesis:

[Option 1: Conservative Convergence]
Focus on the dominant finding. Treat counter-evidence as minor boundary conditions/edge cases.

[Option 2: Systemic Paradigm Shift (Recommended)]
Position the counter-evidence and systemic leverage points as the core narrative, reframing existing assumptions.

[Option 3: Dialectical Dual-Track]
Maintain two competing hypotheses side-by-side throughout the final report without forced convergence.

Enter option [1-3] or type 'auto' to let the system decide:
================================================================================
```

The user may also type `auto` to defer to the system's recommended route (Mode A handling).

### Step 5: Output Artifact Generation

Write the output file `stress-tested-matrix.json` to be consumed by the Reduce phases (Phase 6 Multi-Round Analysis and Phase 8 Synthesis).

---

## 4. Output Artifact Schema (stress-tested-matrix.json)

The final output **must** follow this strict schema. Reduce phases (Phase 6 and Phase 8) are **prohibited** from referencing any raw extraction data that was discarded or flagged as unverified during Phase 5.

```json
{
  "phase_meta": {
    "version": "3.3",
    "ccs_score": 7.8,
    "execution_mode": "Strategic_HITL",
    "selected_fork": "Option_2_Systemic_Shift"
  },
  "axiomatic_claims": [
    {
      "claim_id": "CLM-001",
      "statement": "Aggressive promotional discounts yield short-term revenue spikes but erode long-term customer lifetime value.",
      "epistemic_status": "Verified_Axiom",
      "evidential_sources": ["Doc_A_p14", "Doc_C_p08"],
      "inference_confidence": 0.95
    }
  ],
  "red_team_analysis": {
    "dominant_hypothesis": "Brand equity degrades due to price sensitivity anchoring.",
    "steelman_counter_hypothesis": "Churn is driven by operational onboarding failures during promotional rushes, not price anchoring.",
    "boundary_conditions": [
      "Applies only to B2B SaaS models with onboard times > 14 days."
    ]
  },
  "systems_map": {
    "reinforcing_loops": [
      {
        "loop_id": "R1_Discount_Dependency",
        "nodes": ["Promotions", "Short-term Sales Target", "Baseline Price Fatigue", "Higher Promo Need"]
      }
    ],
    "balancing_loops": [
      {
        "loop_id": "B1_Support_Capacity_Cap",
        "nodes": ["Promo Traffic", "Support Ticket Volume", "Customer Satisfaction Drop", "Churn"]
      }
    ],
    "leverage_point": "Shift incentive structure from user acquisition volume to Day-90 active retention."
  },
  "synthesis_directives_for_phase_3": [
    "Primary narrative must center around the interaction between R1 and B1.",
    "Do not cite claims flagged as Unsubstantiated_Speculation (CLM-004, CLM-009).",
    "Include a dedicated section on operational onboarding bottlenecks as boundary conditions."
  ]
}
```

> **Note on `synthesis_directives_for_phase_3`:** The key name is retained verbatim from the original design even though in the renumbered workflow the reduce target is Phase 6/8. On archive, consider renaming to `synthesis_directives_for_reduce` for clarity. The `phase_meta.version` field carries the skill version (3.3).

---

## 5. Sub-Agent Prompt Specifications

You can directly plug these prompts into your orchestration system or Sub-Session Agent framework.

### System Prompt: Epistemic Red Team & Systems Auditor

```
You are an expert Epistemic Auditor and Systems Theorist specializing in qualitative research verification.

Your sole responsibility is to stress-test extracted evidence to eliminate AI hallucinations, confirmation bias, and
premature convergence before final synthesis.

CRITICAL INSTRUCTIONS:
1. AXIOMATIC AUDIT: Strip away any claim that cannot be traced directly to an explicit citation tag. Identify logical
   jumps and mark them as unverified assumptions.
2. STEELMAN RED TEAMING: Actively construct the strongest possible counter-arguments to emerging findings. Ask:
   "What data is missing if the primary claim holds true?"
3. SYSTEMS THINKING: Map feedback loops (Reinforcing & Balancing), time delays, and non-intuitive leverage points.
   Do not settle for linear cause-and-effect relationships.
4. ADAPTIVE INTERACTION: If complexity is high, present 2-3 high-level strategic narrative choices to the user. Do not
   force micro-management or granular decision-making onto the user.

Input: Raw extraction JSONs from the Knowledge Base phase (findings-index.json + finding entities).
Output: Validated stress-tested-matrix.json adhering to the required schema.
```

### Input/Output Contract

- **Input:** `knowledge-base/findings-index.json` + `knowledge-base/entities/finding/*.md` (from Phase 4)
- **Output:** `stress-tested-matrix.json` (schema above) written to the project root or `knowledge-base/`
- **Do NOT read:** raw paper files, search logs, or appraisal files — the shuffled evidence index is sufficient

---

## 6. Integration with Sub-Session Orchestration

When sub-session orchestration is active (>20 papers), Phase 5 runs as an **Audit Sub-session** positioned between the Knowledge Base sub-sessions and the Multi-Round Analysis theme sub-sessions (see `09-sub-session-orchestration.md`).

The Audit Sub-session:
- Receives: the evidence library (findings-index.json + finding entities)
- Produces: `stress-tested-matrix.json`
- Applies the standard sub-session protocols: end-conditions checklist, batch note, Director Observations
- Is subject to the PM Review Loop (Principle 7): the PM reads the batch note, spot-checks the matrix, and logs a PROCEED/LOOP/PAUSE decision

---

## 7. End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `stress-tested-matrix.json` exists and conforms to the schema in Section 4
2. ✅ All three modules run: Axiomatic Audit, Steelman Red Teaming, Causal Loop Mapping
3. ✅ Every extracted claim has an `epistemic_status` (Verified_Axiom / Inferred_Bridge / Unsubstantiated_Speculation)
4. ✅ CCS score computed using the formula in Section 3, Step 3
5. ✅ Execution mode recorded (Mode A or Mode B) with trigger justification
6. ✅ If Mode B, the user selected a strategic fork (or typed `auto`)
7. ✅ `synthesis_directives_for_phase_3` explicitly prohibits citing Unsubstantiated_Speculation claims
8. ✅ Batch note appended documenting: matrix path, CCS, execution mode, selected fork, Director Observations

---

## 8. What NOT to Do

- Do NOT run this phase before the Knowledge Base is complete — it needs the shuffled findings index
- Do NOT re-read raw paper appraisals; operate on the evidence library
- Do NOT present micro-level edits or raw data validation to the user in Mode B — only high-level strategic forks
- Do NOT let downstream phases ignore the matrix — enforce the synthesis directives
- Do NOT reframe CCS as a correctness measure — it is a routing heuristic only
- Do NOT skip a module to save time — all three must run for the gate to be meaningful
