# Phase 3: Deep Reading & Critical Appraisal

**Purpose:** Read each paper thoroughly, extract grounded findings, assess quality — before any knowledge base entry.

**Important:** Run this phase **in parallel** — one sub-agent per paper. Each agent reads one paper and produces its appraisal independently.

## Per-Paper Extraction

For each paper, extract and capture in `papers/appraisals/{paper-id}.appraisal.md`:

```
# Appraisal: {Author}_{Year}_{ShortTitle}

## Metadata
- Region: {region}
- Discipline: {discipline}
- Methodology: {type}
- Sample: {size, population description}
- Professor affiliation: {institution, department}

## Research Question
{verbatim or close paraphrase}

## Theoretical Framework
{what theory or lens guides this study?}

## Key Findings
- Finding 1: "{exact verbatim quote from paper}"
- Finding 2: "{exact verbatim quote from paper}"
  ...

## Author's Own Limitations
{what limitations does the paper itself acknowledge?}

## Critical Appraisal

### Methodology Quality
- Sample representativeness: HIGH / MEDIUM / LOW — {rationale}
- Bias controls: HIGH / MEDIUM / LOW — {rationale}
- Study duration adequacy: HIGH / MEDIUM / LOW — {rationale}

### Cultural Positioning
- Emic (insider) / Etic (outsider) / Mixed
- Researcher positionality noted? Yes / No
- Cultural bias risk: HIGH / MEDIUM / LOW

### Evidence Strength
Per finding:
- Finding 1: {direct evidence / inferred / claimed} — {rationale}
- Finding 2: {direct evidence / inferred / claimed} — {rationale}

### Verbatim Quotes for Knowledge Base
{key quotes that must be preserved verbatim — these are the grounding for all downstream claims}
```

## Cross-Appraisal Consistency Check

After all parallel appraisals complete:

- Were the same criteria applied uniformly?
- Any paper where methodology quality is so low it should be excluded?
- Flag any appraiser bias (e.g., favoring certain methodologies over others)

## Output

One `.appraisal.md` per paper in `papers/appraisals/`. These serve as the grounding source for all knowledge base entities and synthesis claims.
