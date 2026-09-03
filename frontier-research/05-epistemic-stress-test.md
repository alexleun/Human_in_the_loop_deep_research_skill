# Phase 5: Epistemic Stress-Test & Systems Mapping (NEW in v1.0)

**Purpose:** Destructively verify all claims in the epistemic ledger before any generative synthesis or convergent analysis begins. Combats AI hallucinations, confirmation bias, and premature convergence by applying epistemic first principles, critical thinking, and systems thinking to the engineering evidence base.

**Position in workflow:** Immediately after Critical Thinking & Red-Teaming (Phase 4) and before Generative Synthesis & Divergent Thinking (Phase 6). This is a **dedicated destructive gate** — downstream phases (Phase 6 and Phase 8) are **prohibited** from presenting any claim flagged as unverified as established fact.

**Reuse note:** This phase **reuses the shared epistemic stress-test methodology** introduced in culture-research v3.3 (Axiomatic Audit, Steelman Red Team, Causal Loop & Emergence Mapping, CCS routing) rather than redefining it. The only changes are the input paths (this skill's `evidence/03-epistemic-ledger.md` + `raw_data/` sources) and the downstream phase references (Phase 6 / Phase 8 / Phase 10 of THIS skill). Keep the two skills' stress-test definitions aligned.

**Execution pattern:** Run as a sub-session (Epistemic Red Team & Systems Auditor) when sub-session orchestration is active (>20 sources); run inline for smaller projects.

---

## 1. Overview & Objective

Frontier research suffers from three systemic failure modes:

1. **AI Hallucinations (Epistemic Drift):** Model-generated logical leaps or unsubstantiated technical claims created when bridging gaps between sources.
2. **Confirmation Bias (Selective Synthesis):** Over-weighting evidence that supports the mainstream/initial technical route while ignoring boundary conditions, edge cases, and counter-evidence.
3. **Premature Convergence (Imagination Bottleneck):** Defaulting to the dominant technical narrative instead of surfacing complex systemic dynamics, trade-offs, or non-mainstream alternatives.

Phase 5 acts as a **destructive verification and dynamic mapping gateway** between Red-Teaming (Phase 4) and Generative Synthesis (Phase 6). By applying **Epistemic First Principles**, **Critical Thinking (Red Teaming)**, and **Systems Thinking**, this phase stress-tests all claims before any report narrative is written.

```
┌──────────────────┐      ┌──────────────────────────────────────────────┐      ┌──────────────────┐
│ Phase 4: Red-    │ ──►  │ Phase 5: Epistemic Stress-Test & Systems     │ ──►  │ Phase 6:         │
│ Team (premises,  │      │            Mapping (Destructive Gate)        │      │ Generative       │
│  ledger CLM-x)   │      └──────────────────────────────────────────────┘      │ Synthesis        │
└──────────────────┘                                                             └──────────────────┘
```

---

## 2. Core Methodological Framework

### Module 1: Axiomatic Audit (Epistemic First Principles)

**Goal:** Eliminate hallucinations and unsupported leaps.

**Mechanism:** Deconstruct every claim into two atomic components:

- **Raw Evidential Axioms:** Direct quotes or hard data tied to concrete source tags (e.g., `[SRC-001]`, `raw_data/...`).
- **Inference Chains:** The logical steps connecting axioms to conclusions.

**Classification:** Each claim is assigned one of three epistemic statuses:

| Status | Meaning | Action |
|---|---|---|
| **Verified_Axiom** | Traces directly to a verifiable raw evidential axiom with a complete inference chain | Eligible for primary evidence pool |
| **Inferred_Bridge** | Has some evidential support but requires intermediate logical steps not directly present in evidence | Eligible but with reduced confidence and an explicit flag |
| **Unsubstantiated_Speculation** | Lacks a verifiable axiom or contains a gap in its inference chain | **Excluded** from the primary evidence pool; flagged High-Risk Assumption |

**Example:**
- *Verified Axiom:* "FP8 matmul delivers ~2x raw FLOPs throughput vs FP16 on this silicon." → `[SRC-001: benchmark]`, `[SRC-003: reproduction]`
- *Inferred Bridge:* "Therefore end-to-end training is ~2x faster." (plausible but requires the assumption that matmul is the training bottleneck)
- *Unsubstantiated Speculation:* "Vendor will fully replace legacy accelerators by 2027." (no source tag, single low-trust web claim)

**Action:** Any claim lacking a verifiable axiom or containing a gap in its inference chain is flagged as a High-Risk Assumption and stripped from the primary evidence pool, remaining visible only in the synthesis directives as an excluded claim.

### Module 2: Steelman Red Teaming (Critical Thinking)

**Goal:** Eradicate confirmation bias.

**Mechanism:** Instantiate an adversarial analysis that constructs the strongest possible counter-arguments to emerging conclusions.

**Action:**
- Identify alternative explanations that fit the same data (competing hypotheses)
- Search specifically for edge cases, anomalies, and boundary conditions
- Formulate the **Steelman Counter-Hypothesis** — the strongest possible version of the opposing argument
- Ask the defining question: *"What data should be present if the primary claim holds true — and is it missing?"*

**Integration with the epistemic ledger (Phase 3):** Steelman output must respect the `[Fact]/[Hypothesis]/[Speculation]` labels. A counter-hypothesis grounded in an actual source carries evidential weight; a counter-hypothesis derived purely from reasoning with no evidential anchor is explicitly labeled "reasoning-based, not evidence-anchored."

**Example:**
- *Dominant hypothesis:* "Dense GPU parallelism is the only viable scaling path."
- *Steelman counter-hypothesis:* "Algorithmic efficiency + sparsity delivers comparable throughput at a fraction of the power."
- *Boundary condition:* "Applies only where workload sparsity > 50% and latency isn't the binding constraint."

### Module 3: Causal Loop & Emergence Mapping (Systems Thinking)

**Goal:** Overcome premature convergence and surface non-intuitive insights.

**Mechanism:** Shift from linear causality (*A*→*B*) to feedback dynamics.

**Action:**
- Identify **Reinforcing Loops (*R*)** — compounding mechanisms (e.g., `R1_Adoption_Flywheel`)
- Identify **Balancing Loops (*B*)** — stabilizing/resisting mechanisms (e.g., `B1_Cost_Ceiling`)
- Pinpoint **Time Delays** between causes and systemic effects
- Locate **Non-Intuitive Leverage Points** where small interventions yield disproportionate systemic shifts

**Labeling convention:** Use `R1`, `R2`, `B1`, `B2` with descriptive suffixes. Each loop maps a set of `nodes` (variables) connected in a feedback cycle. Incentivize the auditor to look beyond single-loop linear reasoning.

**Example:**
```
R1_Adoption_Flywheel: [Users] → [Network Effect] → [Value Per User] → [More Users]
B1_Cost_Ceiling: [Scale] → [Infra Cost] → [Margin Pressure] → [Capacity Cap]
Leverage point: "Shift from raw-throughput scaling to latency-insensitive batching + sparsity-aware kernels."
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
                      ┌─────────────────┴─────────────────┐
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
               [ Proceed to Phase 6: Generative Synthesis ]
```

### Step 1: Input Ingestion

Read all claims from `evidence/03-epistemic-ledger.md` and the `epistemic_ledger` in `project-state.json`. Do **NOT** re-read raw source artifacts — the ledger is the authoritative input (if a claim is missing from the ledger, treat it as unverified).

### Step 2: Automated Tri-Analysis Pipeline

Run the three analysis modules in sequence:

1. **Axiomatic Deconstruction:** validate all claims against source tags; classify as Verified_Axiom / Inferred_Bridge / Unsubstantiated_Speculation; record `inference_confidence` per claim (0.0–1.0).
2. **Steelman Counter-Analysis:** generate counter-hypotheses for every major conclusion cluster; evaluate what data *should* be present if the main hypothesis is true, and flag missing signals.
3. **Systems Loop Mapping:** build a dynamic system map outlining feedback loops (*R1*, *R2*, *B1*, *B2*), time delays, and systemic bottlenecks.

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

> **Note:** The CCS is a **routing heuristic**, deciding only *how* interaction happens (automated vs. strategic HITL), not a measure of correctness. For engineering/scientific claims with quantitative data, compute it by script rather than estimating (per the Calculations First guardrail).

### Step 4: Routing & Execution (Adaptive Human-in-the-Loop)

#### Condition A: Fully Automated Mode (Mode A)

**Trigger:** *CCS* < 6, OR user explicitly sets `--mode=auto`, OR the task complexity exceeds standard human cognitive processing limits without domain expertise.

**Execution:**
1. The AI automatically resolves minor logical conflicts using maximum evidential rigor
2. Generates `evidence/05-stress-tested-matrix.json`
3. Mandates that the report (Phase 9) include a dedicated **"Epistemic Limitations & Systemic Blindspots"** chapter

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

- Dominant Finding: [Summary of mainstream technical interpretation]
- Systemic Blindspot / Counter-Evidence: [Summary of Red Team finding & feedback loops]

Please select the strategic direction for final synthesis:

[Option 1: Conservative Convergence]
Focus on the dominant technical route. Treat counter-evidence as minor boundary conditions/edge cases.

[Option 2: Systemic Paradigm Shift (Recommended)]
Position the counter-evidence and systemic leverage points as the core narrative, reframing existing assumptions.

[Option 3: Dialectical Dual-Track]
Maintain two competing technical hypotheses side-by-side throughout the final report without forced convergence.

Enter option [1-3] or type 'auto' to let the system decide:
================================================================================
```

The user may also type `auto` to defer to the system's recommended route (Mode A handling).

### Step 5: Output Artifact Generation

Write the output file `evidence/05-stress-tested-matrix.json` to be consumed by the generative synthesis (Phase 6) and convergence (Phase 8) phases.

---

## 4. Output Artifact Schema (stress-tested-matrix.json)

The final output **must** follow this strict schema. Downstream phases (Phase 6 and Phase 8) are **prohibited** from referencing any raw claim that was discarded or flagged as unverified during Phase 5.

```json
{
  "phase_meta": {
    "skill": "frontier-research",
    "version": "1.0",
    "ccs_score": 7.8,
    "execution_mode": "Strategic_HITL",
    "selected_fork": "Option_2_Systemic_Shift"
  },
  "axiomatic_claims": [
    {
      "claim_id": "CLM-001",
      "statement": "FP8 matmul delivers ~2x raw FLOPs throughput vs FP16 on this silicon.",
      "epistemic_status": "Verified_Axiom",
      "evidential_sources": ["SRC-001", "SRC-003"],
      "inference_confidence": 0.95
    }
  ],
  "red_team_analysis": {
    "dominant_hypothesis": "Dense GPU parallelism is the only viable scaling path.",
    "steelman_counter_hypothesis": "Algorithmic efficiency + sparsity delivers comparable throughput at a fraction of the power.",
    "boundary_conditions": [
      "Applies only where workload sparsity > 50% and latency is not the binding constraint."
    ]
  },
  "systems_map": {
    "reinforcing_loops": [
      {
        "loop_id": "R1_Adoption_Flywheel",
        "nodes": ["Users", "Network Effect", "Value Per User", "More Users"]
      }
    ],
    "balancing_loops": [
      {
        "loop_id": "B1_Cost_Ceiling",
        "nodes": ["Scale", "Infra Cost", "Margin Pressure", "Capacity Cap"]
      }
    ],
    "leverage_point": "Shift from raw-throughput scaling to latency-insensitive batching + sparsity-aware kernels."
  },
  "synthesis_directives": [
    "Primary narrative must center around the interaction between R1 and B1.",
    "Do not cite claims flagged as Unsubstantiated_Speculation (CLM-003).",
    "Include a dedicated section on non-mainstream alternative routes as boundary conditions."
  ]
}
```

> **Schema note:** The `synthesis_directives` key (integer-less) is used here for the frontier skill; the culture-research skill retains its own `synthesis_directives_for_phase_3` key to preserve that skill's serialized compatibility. Keep the two skills' matrices aligned in spirit but allow the key-name difference.

---

## 5. Sub-Agent Prompt Specifications

### System Prompt: Epistemic Red Team & Systems Auditor

```
You are an expert Epistemic Auditor and Systems Theorist specializing in engineering/scientific research verification.

Your sole responsibility is to stress-test extracted claims to eliminate AI hallucinations, confirmation bias, and
premature convergence before final synthesis.

CRITICAL INSTRUCTIONS:
1. AXIOMATIC AUDIT: Strip away any claim that cannot be traced directly to an explicit source tag. Identify logical
   jumps and mark them as unverified assumptions.
2. STEELMAN RED TEAMING: Actively construct the strongest possible counter-arguments to emerging conclusions. Ask:
   "What data is missing if the primary claim holds true?"
3. SYSTEMS THINKING: Map feedback loops (Reinforcing & Balancing), time delays, and non-intuitive leverage points.
   Do not settle for linear cause-and-effect relationships.
4. ADAPTIVE INTERACTION: If complexity is high, present 2-3 high-level strategic narrative choices to the user. Do not
   force micro-management or granular decision-making onto the user.

Input: evidence/03-epistemic-ledger.md + epistemic_ledger in project-state.json.
Output: evidence/05-stress-tested-matrix.json adhering to the required schema.
```

### Input/Output Contract

- **Input:** `evidence/03-epistemic-ledger.md` + `epistemic_ledger` in `project-state.json` (from Phase 3)
- **Output:** `evidence/05-stress-tested-matrix.json` (schema above)
- **Do NOT read:** raw source artifacts — the ledger is the authoritative input; anything missing from the ledger is unverified

---

## 6. Integration with Sub-Session Orchestration

When sub-session orchestration is active (>20 sources), Phase 5 runs as an **Audit Sub-session** positioned between the red-team sub-sessions and the generative-synthesis sub-sessions.

The Audit Sub-session:
- Receives: the epistemic ledger + `project-state.json` epistemic_ledger
- Produces: `evidence/05-stress-tested-matrix.json`
- Applies the standard sub-session protocols: end-conditions checklist, batch note, Director Observations
- Is subject to the PM Review Loop: the PM reads the batch note, spot-checks the matrix, and logs a PROCEED/LOOP/PAUSE decision

---

## 7. End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `evidence/05-stress-tested-matrix.json` exists and conforms to the schema in Section 4
2. ✅ All three modules run: Axiomatic Audit, Steelman Red Teaming, Causal Loop Mapping
3. ✅ Every claim in the ledger has an `epistemic_status` (Verified_Axiom / Inferred_Bridge / Unsubstantiated_Speculation)
4. ✅ CCS score computed using the formula in Section 3, Step 3 (by script for quantitative data)
5. ✅ Execution mode recorded (Mode A or Mode B) with trigger justification
6. ✅ If Mode B, the user selected a strategic fork (or typed `auto`)
7. ✅ `synthesis_directives` explicitly prohibits citing Unsubstantiated_Speculation claims
8. ✅ Batch note appended documenting: matrix path, CCS, execution mode, selected fork, Director Observations

---

## 8. What NOT to Do

- Do NOT run this phase before Phase 4 is complete — it needs the red-team analysis and the complete ledger
- Do NOT re-read raw source artifacts; operate on the epistemic ledger
- Do NOT present micro-level edits or raw data validation to the user in Mode B — only high-level strategic forks
- Do NOT let downstream phases ignore the matrix — enforce the synthesis directives
- Do NOT reframe CCS as a correctness measure — it is a routing heuristic only
- Do NOT skip a module to save time — all three must run for the gate to be meaningful
