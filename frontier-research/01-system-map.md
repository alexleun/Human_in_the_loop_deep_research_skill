# Phase 1: Topic Deconstruction & System Mapping

**Purpose:** Decompose the technical/scientific topic into its core variables, boundary conditions, and physical/engineering constraints, then build an initial systems map (causal loops, feedback, bottlenecks, emergent behavior).

**Core method:** Systems Thinking.

**Execution pattern:** Conversational, run in the main session with the human. Output `access/01-system-map.md`.

---

## Procedure

1. **Load project context** — topic, target deliverable, special focus, accepted sources from `project-state.json` (or from the user if this is the first phase).

2. **Deconstruct the problem**
   - Identify the **core variables** that determine system behavior
   - Establish **boundary conditions** (what is in scope / out of scope, spatial/temporal/economic limits)
   - Enumerate **physical/engineering constraints** (conservation laws, material limits, scaling laws, latency/bandwidth/cost ceilings)

3. **Build the system architecture / causal-loop map**
   - Map how the core variables interact
   - Identify **Reinforcing Loops (R)** — compounding mechanisms
   - Identify **Balancing Loops (B)** — stabilizing/resisting mechanisms
   - Note **time delays** between causes and effects
   - Flag **bottlenecks** and **emergent behaviors** that are not obvious from any single variable

4. **Surface unknowns and blind spots**
   - What assumptions are we making about the system?
   - What data/signals would change our model?
   - Which loops are most sensitive to uncertainty?

5. **Initialize `project-state.json`** (if not already present) with the topic, domain, current_phase (`01-system-map.md`), user_constraints, and an empty epistemic_ledger.

6. **Write `access/01-system-map.md`** as the phase deliverable.

---

## Output: access/01-system-map.md

The system map deliverable MUST capture:

- Core variables and boundary conditions
- Physical/engineering constraints
- Causal-loop diagram (R / B loops with labeled nodes)
- Identified bottlenecks and emergent behaviors
- Open questions about system sensitivity

```text
R1_Adoption_Flywheel: [Users] → [Network Effect] → [Value Per User] → [More Users]
B1_Cost_Ceiling: [Scale] → [Infra Cost] → [Margin Pressure] → [Capacity Cap]
Bottleneck: [Single-vendor GPU supply] caps scale-up rate
Emergence: [Contention collapses throughput non-linearly past a utilization threshold]
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ `access/01-system-map.md` exists and captures variables, boundaries, constraints, R/B loops, bottlenecks, and emergent behavior
2. ✅ Core variables and boundary conditions are defined in writing
3. ✅ At least one feedback loop (R or B) is identified and labeled
4. ✅ Key unknowns/assumptions are surfaced and documented
5. ✅ `project-state.json` initialized (or updated) with topic, domain, current_phase, and empty epistemic_ledger
6. ✅ Human has reviewed and approved the system map

---

## What NOT to Do

- Do NOT skip the systems map — Phase 2 harvesting and every later phase depend on it
- Do NOT collect data before the variables/boundaries are defined
- Do NOT settle for a linear cause-and-effect description; look for loops, delays, and emergence
- Do NOT proceed to Phase 2 before the system map is approved by the human
