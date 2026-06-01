# Phase 5: Multi-Round Iterative Analysis

**Purpose:** Five sequential analysis rounds, each producing a documented output that feeds the next. Run in order — each round depends on the previous.

---

## Round 1: Thematic Categorization

Group all findings by behavior domain, then inductively identify sub-themes within each domain.

**Procedure:**
1. Collect all findings per domain (work, family, leisure, sleep, mobility, eating, hygiene, social, religious, etc.)
2. Within each domain, identify emergent sub-themes (e.g., within "work": hours variation, gender division, remote work, work-life boundary, job satisfaction)
3. For each sub-theme, document: which papers address it, what cultural contexts are represented, range of findings
4. Note which sub-themes appear across multiple regions vs unique to one

**Output:** `knowledge-base/analysis/round1-thematic-map.md` with `#behavior/{domain}` tags and `[[wikilink]]` references to paper appraisals.

---

## Round 2: Cross-Cultural Comparison Matrix

Build a structured comparison matrix.

**Procedure:**
1. Rows = behavior domains and sub-themes (from Round 1)
2. Columns = cultural regions
3. Cells = key finding summary + source paper reference
4. Annotate each cell: evidence strength (HIGH/MEDIUM/LOW), agreement level across papers in same region
5. Highlight: strong cross-region patterns, regional divergences, empty/sparse cells

**Output:** `knowledge-base/analysis/round2-comparison-matrix.md` with `#region/{region}` column tags, `#behavior/{domain}` row tags, `[[wikilink]]` cells to finding entity notes.

---

## Round 3: Contradiction & Methodology Deep-Dive

Identify and analyze contradictory findings.

**Procedure:**
1. Find all pairs/triples of findings that contradict each other (opposite conclusions on same behavior in similar cultural contexts)
2. For each contradiction, analyze: methodological differences (sample, duration, instrument), cultural sub-context differences (urban vs rural, generational), temporal difference (year of study)
3. Assess: is this contradiction resolvable (methodological artifact) or genuine (real cultural variation)?
4. Identify patterns where methodology choice systematically influences findings (self-report vs observation, short vs long duration, small vs large sample)

**Output:** `knowledge-base/analysis/round3-contradictions.md` with `#status/contradicted` tags and `[[wikilink]]` pairs linking contradictory findings.

---

## Round 4: Gap Analysis & Blind Spot Mapping

Systematically document what is missing.

**Procedure:**
1. From coverage report: regions and behavior domains with zero or minimal coverage
2. Under-studied populations: children, elderly, disabled, rural, informal workers, indigenous, migrants
3. Methodological blind spots: over-reliance on self-report, short durations, WEIRD bias
4. Temporal gaps: weekday vs weekend, seasonal variation, holiday vs routine, life-stage transitions
5. Disciplinary silos: which domains are studied by which disciplines, what cross-disciplinary links are missing

**Output:** `knowledge-base/analysis/round4-gaps.md` with `#status/gap` tags and `[[behavior/{domain}]]` wikilinks to behavior notes with insufficient coverage.

---

## Round 5: Research Question Generation

Derive novel, evidence-grounded research questions from all prior rounds.

**Procedure:**
1. From cross-region patterns (Round 2): formulate hypotheses about universal drivers AND questions about local variations
2. From contradictions (Round 3): formulate targeted studies that could resolve each contradiction
3. From gaps (Round 4): formulate questions for each blind spot — specify missing population, behavior domain, methodology needed
4. Generate interdisciplinary bridge questions: domains that cross discipline boundaries (sleep + urban design, eating + economics, family + technology)
5. For each question, assess: novelty (already studied?), feasibility (can it be studied?), potential impact (what would it reveal?)

**Output:** `knowledge-base/analysis/round5-research-questions.md` with `[[wikilink]]` references back to the gap, contradiction, or pattern that motivated each question.
