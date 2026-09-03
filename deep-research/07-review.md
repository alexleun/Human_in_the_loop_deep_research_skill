# Phase 7: Review — Weak Point Audit

**Purpose:** Critically examine the research for methodological flaws, weak evidence, unstated assumptions.

## Audit Checklist

For each dimension of the research, check:

**Data & Sources**
- [ ] Is every claim grounded in exact source quotes (not paraphrases)?
- [ ] Are all sources cached in `knowledge-base/sources/` for verification?
- [ ] Are there single-source claims presented as established facts?
- [ ] Are sources from the correct hierarchy level? (gov't > academic > news)

**Analysis**
- [ ] Is any conclusion based on LLM-memorized numbers rather than computed output?
- [ ] Were statistical corrections applied where needed?
- [ ] Are there data sparsity issues that limit confidence?
- [ ] Are causal claims appropriately cautious?

**Methodology**
- [ ] Are results sensitive to arbitrary parameter choices?
- [ ] Are alternative explanations discussed?
- [ ] Are limitations disclosed with direction of bias?
- [ ] Do conclusions outrun what the data supports?

**Output — Bilingual & Web**
- [ ] Is the web output consistent across languages?
- [ ] Are all navigation links functional? Check every page individually.
- [ ] Are all source citations present and correctly formatted?
- [ ] **Encoding check**: Search all ZH files for U+FFFD (�) — zero occurrences required. Also scan for literal `??` bytes indicating degraded em dashes.
- [ ] **Structural parity**: EN and ZH versions of each report must have identical counts of `<div class="finding">` blocks, `data-source` attributes, and `data-confidence` attributes.
- [ ] **DOM structure check**: Run div balance check (opens vs closes) on every HTML file — a stray `</div>` breaks layout without affecting element counts.
- [ ] **Title tag check**: Every HTML `<title>` must be non-empty and include the correct language prefix/suffix.
- [ ] **Footer date check**: Every HTML page must have a date in its footer matching the current project epoch. Scan for stale dates (e.g., "May 2026" when it's June 2026).
- [ ] **Nav text consistency**: All EN pages must have identical nav labels. All ZH pages must have identical nav labels (no variant translations like 情景 vs 情境 across different files).
- [ ] **Image path check**: ZH pages use `../images/` prefix (not `images/`).

**Output — Cross-Artifact Consistency**
- [ ] **Cross-artifact mapping**: For every new finding or data point added, verify it appears in ALL relevant artifacts:
  - [ ] Report chapter(s)
  - [ ] Executive summary / Synthesis page (if significant)
  - [ ] Knowledge base (if new entity/relation)
  - [ ] Dashboard / Interactive features description (if new data type)
  - [ ] Data file (if computed data — check JSON/CSV)
  - [ ] Bilingual pair (ZH version of each updated artifact)

**Quantitative Data Verification** (Lesson from HK project)
- [ ] Are CSV values verified against authoritative sources? (Do NOT assume web-scraped or LLM-generated data is correct.)
- [ ] Are key inflection points manually cross-checked? (e.g., population end-2025, GDP per capita ratio, land premium collapse)
- [ ] Is there a correction log documenting what was wrong and how it was fixed?
- [ ] Were all corrections propagated to figures and report text?

## Audit Script Pattern

For bilingual parity checks, use a script like this rather than manual inspection:

```python
import re, os, glob

base = "project/web"
issues = []

for zh_file in glob.glob(os.path.join(base, "zh", "*.html")):
    en_file = os.path.join(base, os.path.basename(zh_file))
    if not os.path.exists(en_file):
        continue

    zh_text = open(zh_file, encoding="utf-8").read()
    en_text = open(en_file, encoding="utf-8").read()

    # Encoding
    if '\ufffd' in zh_text:
        issues.append(f"CORRUPT: {zh_file}")

    # Structural parity
    zh_findings = zh_text.count('<div class="finding"')
    en_findings = en_text.count('<div class="finding"')
    if zh_findings != en_findings:
        issues.append(f"Finding count mismatch: {zh_file} ({zh_findings} vs {en_findings})")

    # Source attribute parity
    zh_ds = zh_text.count('data-source="')
    en_ds = en_text.count('data-source="')
    if zh_ds != en_ds:
        issues.append(f"data-source count mismatch: {zh_file} ({zh_ds} vs {en_ds})")

    # Confidence attribute parity
    zh_conf = zh_text.count('data-confidence="')
    en_conf = en_text.count('data-confidence="')
    if zh_conf != en_conf:
        issues.append(f"data-confidence count mismatch: {zh_file} ({zh_conf} vs {en_conf})")

if issues:
    for i in issues:
        print(f"✗ {i}")
else:
    print("✓ All checks passed")
```

## Review Manifest

When reporting audit results, use a concise text summary rather than a YAML block:

```
Audit: Sources & Grounding
Issues found: 2
- HIGH: Claim X has no source quote — only a paraphrase (final-report.html)
- MEDIUM: Source Y not cached in knowledge-base/sources/
Passed: All conclusions appropriately cautious, figure legends verified
Action: Propose new change to fix citation gaps
```

Reserve full YAML manifests for autonomous sub-agent tasks where the human cannot review inline.

**If significant issues found → propose a new change to fix them.**

---

## Phase 7 Epistemic Audit (NEW in v2.3)

Adapted from the culture-research Phase 5 Epistemic Stress-Test (see Principle 21 in SKILL.md). This audit operates on the **code-driven analysis artifacts** (notebooks, generated figures, computed JSON/CSV), not raw LLM output. It runs before the report is finalized.

### Module 1: Axiomatic Audit (citation validation)

For every finding that will appear in the report, verify:
- [ ] Does the finding carry a `data-source` ID (from Phase 2 citation-first embedding)?
- [ ] Is there a confidence level, not just an assertion?
- [ ] Can the finding be traced to a cached source in `knowledge-base/sources/` (P20)?
- [ ] Does any "inference bridge" (a claim needing intermediate steps not in the data) get flagged, not presented as established?

If a finding fails, flag it as `Unsubstantiated_Speculation` and exclude it from the primary evidence pool.

### Module 2: Steelman Red Teaming (anti-confirmation-bias)

- [ ] For each dominant conclusion, construct the **strongest** counter-hypothesis that fits the same data
- [ ] Identify what data should be present if the primary claim holds — and whether it is absent
- [ ] Capture boundary conditions: under what circumstances does the conclusion fail?
- [ ] Note alternative explanations, especially single-source conclusions presented as facts

### Module 3: Causal Loop & Emergence Mapping (anti-premature-convergence)

- [ ] Go beyond linear cause-and-effect (*A*→*B*): map reinforcing (R) and balancing (B) feedback loops
- [ ] Identify time delays between causes and systemic effects
- [ ] Locate non-intuitive leverage points (small intervention → disproportionate shift)
- [ ] **Produce a machine-readable systems map** (JSON/DOT) when code-first analysis applies
- [ ] **Compute the CCS by script** when quantitative data is available, rather than LLM estimation

### CCS Script Pattern

When quantitative contradictions/chain-length data exist, compute the Cognitive Complexity Score with a script rather than estimating:

```python
def ccs(contradiction_density, chain_length, loop_count):
    return min(10.0, contradiction_density * 3.5 + chain_length * 0.3 + loop_count * 0.8)
```

### Manifest Output

Fold the audit results into the review manifest. Add an `Epistemic Audit` line, e.g.:

```
Audit: Epistemic Stress-Test & Systems Mapping
Issues found: 1
- HIGH: Finding X is an unsupported inference bridge (systems-map → final-report)
Passed: All citations grounded, CCS computed by script = 4.2 (auto mode)
Action: Propose change to add source grounding for Finding X
```

---

## File Truncation Safeguard (NEW in v2.0)

Report files and source documents may exceed 50KB. After reading any file during audit, check for truncation. A truncated data table or reference section could hide methodological weaknesses.

---

## End Conditions (NEW in v2.0, +Epistemic Audit in v2.3)

This phase is **complete** when ALL of the following are true:

1. ✅ Data & Sources checklist completed — all claims grounded, sources cached
2. ✅ Analysis checklist completed — no LLM-memorized numbers, causal claims appropriately cautious
3. ✅ Methodology checklist completed — limitations disclosed, conclusions don't outrun data
4. ✅ Output checklist completed — parity, encoding, structure, nav, dates, images verified
5. ✅ Cross-artifact consistency checklist completed for all recent additions
6. ✅ Quantitative data verification completed — CSV values cross-checked, correction log propagated
7. ✅ **Epistemic Audit completed (v2.3):** Axiomatic (all findings cited + confidence), Steelman (counter-hypotheses + boundary conditions), Systems map (loops + leverage point); CCS computed by script when quantitative data available
8. ✅ Audit results summarized (issues found, severity, recommended changes)
9. ✅ If significant issues → new change proposed to fix them, or tasks added to current change
10. ✅ `task_state.json` updated if spanning multiple sessions
