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
