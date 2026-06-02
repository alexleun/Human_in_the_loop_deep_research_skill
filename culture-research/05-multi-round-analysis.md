# Phase 5: Multi-Round Iterative Analysis

**Purpose:** Five sequential analysis rounds, each producing a documented output that feeds the next. Run in order — each round depends on the previous.

**Execution pattern:** For 5 rounds with substantial output each, run each round as a sub-session (SS9-SS13). For smaller projects, can run in one session with sequential sub-agents.

---

## Round 1: Thematic Categorization

**Input:** All finding entities in `knowledge-base/entities/finding/` and all behavior domain entities.

**Procedure:**
1. Collect all findings per domain (work, family, leisure, sleep, mobility, eating, hygiene, social, religious, care, etc.) using the `describes` relation
2. Within each domain, inductively identify sub-themes (e.g., within "work": work hours, gender division, remote work, work-life boundary, job satisfaction)
3. For each sub-theme, document: which papers address it, what cultural contexts are represented, range of findings
4. Note which sub-themes appear across multiple regions vs unique to one

**Output:** `knowledge-base/analysis/round1-thematic-map.md` with `#behavior/{domain}` tags and `[[wikilink]]` references.

**End conditions:** Every behavior domain documented; at least 2 sub-themes per domain where data supports; cross-region pattern notes for each sub-theme; batch note appended.

---

## Round 2: Cross-Cultural Comparison Matrix

**Input:** Round 1 output.

**Procedure:**
1. Build matrix: rows = behavior domains/sub-themes, columns = cultural regions
2. Populate cells with key finding summary + source paper reference (`[[wikilink]]`)
3. Annotate each cell: evidence strength (HIGH/MEDIUM/LOW), agreement level across papers in same region
4. Highlight: cross-region patterns, regional divergences, empty/sparse cells

**Cell symbols:**
- ✅ = strong cross-region pattern
- ⚠️ = regional divergence
- ❓ = empty / sparse coverage
- 📊 = single region has data

**Output:** `knowledge-base/analysis/round2-comparison-matrix.md` with `#region/{region}` column tags, `#behavior/{domain}` row tags, and `[[wikilink]]` cells.

**End conditions:** Matrix has rows for all behavior domains/sub-themes from Round 1; columns for all 6 cultural regions; each populated cell has at least one `[[wikilink]]`; cross-region patterns (≥2), divergences (≥2), and gaps (≥5) sections populated; batch note appended.

---

## Round 3: Contradiction & Methodology Deep-Dive

**Input:** Round 2 output, all finding entities and appraisal files.

**Procedure:**
1. Find all pairs (or triples) of findings that reach opposite/contradictory conclusions on the same behavior in similar cultural contexts
2. For each contradiction, analyze: methodological differences, cultural sub-context differences, temporal differences, definitional differences
3. Assess resolvability: **resolvable (methodological artifact)** vs **genuine (real cultural variation)**
4. Identify methodology patterns where methodology choice systematically influences findings (self-report vs observation, short vs long duration, small vs large sample, WEIRD vs non-WEIRD, quantitative vs qualitative)

**Output:** `knowledge-base/analysis/round3-contradictions.md` with `#status/contradicted` tags and `[[wikilink]]` pairs.

**End conditions:** At least 3 distinct contradiction pairs documented; each contradiction has findings-in-tension, methodological analysis, cultural sub-context, and assessment; at least 2 methodology patterns identified; research question leads noted for Round 5; batch note appended.

---

## Round 4: Gap Analysis & Blind Spot Mapping

**Input:** Rounds 2-3 outputs, unified candidate list, coverage report.

**Procedure:**
1. Region × behavior domain gaps (from Round 2 empty/sparse cells)
2. Under-studied populations: children, elderly, disabled, rural, informal economy, indigenous, migrants, LGBTQ+, working class
3. Methodological blind spots: over-reliance on self-report, short durations, WEIRD bias, cross-sectional vs longitudinal, quantitative vs qualitative
4. Temporal gaps: weekday vs weekend, seasonal, holiday vs routine, life-stage transitions, pre/during/post COVID
5. Disciplinary blind spots: which behavior domains are studied by which disciplines, missing cross-disciplinary connections

**Output:** `knowledge-base/analysis/round4-gaps.md` with `#status/gap` tags and `[[behavior/{domain}]]` wikilinks.

**End conditions:** All 5 sections documented; at least 10 distinct gaps identified; each gap uses `[[wikilink]]` where possible; `#status/gap` tags applied; priority gaps for Round 5 flagged; batch note appended.

---

## Round 5: Novel Research Question Generation

**Input:** Rounds 1-4 outputs.

**Procedure:**
1. From Round 2 cross-region patterns: for each strong pattern, formulate hypothesis question + local variation question
2. From Round 3 contradictions: formulate resolution questions
3. From Round 4 gaps: formulate gap-filling questions (with population, behavior, methodology specified)
4. Interdisciplinary bridge questions: 3-5 questions explicitly cross-disciplinary (sleep + urban design, eating + economics, family + technology, etc.)
5. Assess each question: novelty, feasibility, potential impact
6. Prioritize top 10

**Output:** `knowledge-base/analysis/round5-research-questions.md` with `[[wikilink]]` references to the gap/contradiction/pattern that motivated each question.

**End conditions:** At least 4 sections (pattern-derived, contradiction-derived, gap-derived, bridge); at least 15 total questions; each question has motivation (with `[[wikilink]]`), methodology suggestion, novelty/feasibility/impact assessment; top 10 prioritized with rationale; batch note appended.

---

## Why Sequential (Not Parallel)?

The rounds are sequential by design because each builds on the previous:
- Gaps (Round 4) are meaningful only after patterns (Rounds 1-2) are established
- Contradictions (Round 3) require knowing what exists
- Research questions (Round 5) require knowing gaps, contradictions, and patterns

**Exception:** Within each round, sub-tasks can be parallelized (e.g., one sub-agent per behavior domain for Round 1).

---

## Paywall-Weighted Discipline (NEW in v2.0)

When analyzing findings, note which findings come from `evidence_status: abstract-only` papers. These contribute less to:
- Cross-region patterns (lower confidence)
- Contradiction identification (less able to verify a claim against an alternative finding)
- Research question grounding (questions derived solely from abstract-only findings are "speculative")

In Round 5, flag research questions as **evidence-derived** (grounded in verified findings) vs **speculative** (grounded only in inferred findings).

---

## What NOT to Do

- Do NOT skip rounds — each builds on the previous
- Do NOT run rounds in parallel — they depend on each other
- Do NOT fabricate findings — pull only from entities and appraisal files
- Do NOT create new entities during analysis (use what is in the knowledge base)
- Do NOT proceed to synthesis (Phase 7) without the checkpoint (Phase 6)
