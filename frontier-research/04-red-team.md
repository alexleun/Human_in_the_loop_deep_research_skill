# Phase 4: Critical Thinking & Red-Teaming

**Purpose:** Combat confirmation bias by verifying premises, attacking mainstream technical routes for their limits and failure modes, and steel-manning neglected alternative approaches.

**Core method:** Critical Thinking & Anti-Bias.

**Execution pattern:** Sub-sessions per technical route / hypothesis cluster. Output `evidence/04-red-team-analysis.md`.

---

## Procedure

1. **Premise Verification.** Challenge the assumptions the user, the mainstream literature, and the field take for granted. Ask:
   - Is this premise actually supported by the evidence, or just widely repeated?
   - What would have to be true for this premise to hold, and is that itself verified?
   - Which of our own framing assumptions (from Phase 1) might be wrong?

2. **Red-Team the mainstream route.** For each dominant technical route, actively try to break it:
   - **Physical limits** — does it hit a fundamental constraint (thermodynamic, information-theoretic, material, scaling)?
   - **Cost / performance bottlenecks** — where does it stop scaling economically or technically?
   - **Safety / security / reliability failure modes** — what breaks under edge conditions, fault injection, or adversarial use?
   - **Scaling failure** — what happens at sizes or rates beyond the demonstrated range?

3. **Steel-Man the alternatives.** Reconstruct the **strongest** case for neglected or non-mainstream technical approaches (the ones the field may be dismissing):
   - Identify the best rationale for each alternative
   - Apply the same rigor used to praise the mainstream route
   - Avoid straw-manning — improve the opposing argument, don't weaken it

4. **Record a counterfactual analysis.** Ask: *"If the dominant assumption fails, how should the system be architected?"* Capture the fallback / parallel paths.

5. **Respect the epistemic ledger.** Red-team findings must not upgrade any claim beyond what the Phase 3 ledger supports. A red-team counter-hypothesis that is pure reasoning (no evidential anchor) is explicitly labeled "reasoning-based, not evidence-anchored."

6. **Write `evidence/04-red-team-analysis.md`** with the premise review, red-team findings per route, steel-manned alternatives, and counterfactual scenarios.

---

## Output: evidence/04-red-team-analysis.md

```text
Premise Under Test: "GPU-rich parallelism is the only viable scaling path."
Verdict: Largely holds for dense compute, but warrants boundary conditions
  - Physical limit: interconnect bandwidth floors latency per step
Red-Team (mainstream):
  - Route A: cost ceiling at ~X$/TF due to power; scaling failure past Y nodes
  - Failure mode: contention collapse at high utilization (see ledger CLM-002)
Steel-Man (alternative): sparse/lower-precision + algorithmic efficiency
  - Strongest case: order-of-magnitude FLOP reduction amortizes over lifetime
  - Evidence anchor: [Hypothesis] repro of SRC-008, not yet [Fact]
Counterfactual: if dense scaling floors, architecture = heterogeneous + algorithmic
  - Fallback path: latency-insensitive batching + sparsity-aware kernels
```

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Premise verification performed and documented for the main assumptions
2. ✅ Red-team attack run on each dominant technical route with physical/cost/security/scaling failure modes
3. ✅ At least one non-mainstream alternative is steel-manned with its strongest case
4. ✅ Counterfactual analysis recorded ("if the core assumption fails, how to architecture?")
5. ✅ `evidence/04-red-team-analysis.md` exists
6. ✅ Red-team findings respect the epistemic ledger (no unauthorized claim upgrades)
7. ✅ Batch note appended if sub-sessions were used

---

## What NOT to Do

- Do NOT accept mainstream narratives without premise verification
- Do NOT straw-man alternatives — steel-man them
- Do NOT let red-team findings silently upgrade a claim's epistemic status beyond the Phase 3 ledger
- Do NOT proceed to Phase 5 before the red-team analysis is complete
