# Phase 5: Multi-Round Iterative Analysis

**Purpose:** Five sequential analysis rounds, each producing a documented output that feeds the next. Run in order — each round depends on the previous.

**Execution pattern:** For 5 rounds with substantial output each, run each round as a sub-session (SS9-SS13). For smaller projects, can run in one session with sequential sub-agents.

---

## Cross-Cutting Rules (Apply to ALL Rounds)

### File Truncation Safeguard
All file reads may be capped at ~50KB. After reading any file:
1. Check for truncation markers (`...truncated...` or "Full output saved to...")
2. If truncated, read the remainder with `offset=N`
3. **Batch notes and open questions at the end of each file are critical inputs** — always verify they are captured

### Cross-Round Dependency Check (NEW in v3.0)
Before starting any round, verify the prior round's end conditions were met:
- Check the prior round's batch note for completion counts
- If any count is below the minimum end condition, flag and notify PM
- If the prior round's output is missing or incomplete, do NOT proceed

### Reading Strategy (NEW in v3.0)
To manage context budget, use this tiered reading approach:
- **Round 1:** MUST read all finding entity files (to derive sub-themes)
- **Round 2:** Can rely on Round 1's output (sub-themes already cluster findings)
- **Round 3:** Only need to re-read findings in contradiction-flagged sub-themes
- **Round 4:** Only need the Round 2 matrix + Round 3 contradictions
- **Round 5:** Only need the Round 4 gap list + Round 2 patterns

Use `findings-index.json` for programmatic access instead of re-reading all 92 finding files.

---

## Round 1: Thematic Categorization

**Input:** All finding entities in `knowledge-base/entities/finding/` and `knowledge-base/findings-index.json`.

**Procedure:**
1. Collect all findings per domain using the `describes` relation in `relations.json`
2. **Sub-theme derivation method (NEW in v3.0):**
   a. **Initial pass:** Group findings by primary behavior domain tag (use the `describes` relation as authoritative grouping; don't double-count multi-tagged findings)
   b. **Affinity clustering:** Within each domain, group findings by shared topic (gender, age, method, geography, theoretical claim). Aim for groups of 2+ findings.
   c. **Sub-theme naming:** Use a noun phrase capturing the cluster's empirical content (e.g., "WFH and gender reversion" not "Remote work's impact on gender regimes")
   d. **Granularity rule:** Aim for 4-8 sub-themes per domain. If a sub-theme has only 1 finding, consider merging with an adjacent sub-theme unless it represents a region-specific phenomenon.
3. For each sub-theme, document: which papers address it, what cultural contexts are represented, range of findings
4. Note which sub-themes appear across multiple regions vs unique to one
5. **Multi-tagged findings (NEW):** Document multi-domain findings under their PRIMARY domain (first `describes` relation in `relations.json`). Cross-reference other domains inline.
6. **Method-only/theory-only findings (NEW):** Add a separate "Cross-cutting theoretical and methodological findings" section for papers that are primarily about method or theory, not behavior.

**Region-mapping table (NEW in v3.0):**
Define the canonical region set (e.g., East Asia, Europe, Americas, Middle East & Africa, South/Southeast Asia, Oceania) and map each `cultural_context` entity to one region. "Global" findings should be cross-cutting.

**Output:** `knowledge-base/analysis/round1-thematic-map.md` with `#behavior/{domain}` tags, `#region/{region}` tags, and `[[wikilink]]` references. Include complete batch note with: sub-theme count, most-studied list, cross-region patterns, open questions for Round 2, Director Observations.

**End conditions:** Every behavior domain documented; at least 2 sub-themes per domain where data supports; cross-region pattern notes for each sub-theme; multi-tagged findings handled via primary-domain rule; theory/method section included if applicable; batch note appended.

---

## Round 2: Cross-Cultural Comparison Matrix

**Input:** Round 1 output.

**Procedure:**
1. **Sub-theme filter (NEW in v3.0):** Not all sub-themes need to become matrix rows. Apply this filter:
   - **Cross-region filter (recommended):** Include only sub-themes with ≥2 regions of evidence OR ≥3 papers. This yields ~10-15 rows that are the actually cross-regionally interesting ones.
   - **Full inclusion:** Include all sub-themes (49 rows, 294 cells). Useful for audit but unreadable.
   - List excluded sub-themes in a "Single-region notes" appendix.
2. Build matrix: rows = filtered sub-themes, columns = cultural regions
3. Populate cells with key finding summary + source paper reference (`[[wikilink]]`)
4. **Annotate each cell (operationalized in v3.0):**
   - Evidence strength:
     - **HIGH:** ≥3 papers OR (≥2 papers AND multi-method/multi-country)
     - **MEDIUM:** 2 papers, single-method OR single-country
     - **LOW:** 1 paper, single-source
     - Note: If all supporting papers rely on the same dataset (e.g., MTUS), down-grade one level
   - Agreement level:
     - **consensus:** ≥2 papers in region, same direction/conclusion
     - **mixed:** ≥2 papers, opposite or qualified conclusions
     - **single-source:** 1 paper covers the cell
     - **silent-on-comparison:** papers exist but address different sub-questions
5. **Cell symbols (operationalized in v3.0):**
   - ✅ **strong cross-region pattern:** ≥3 regions show SAME direction on the same behavior
   - ⚠️ **regional divergence:** ≥2 regions have DIFFERENT directions/patterns
   - 📊 **single region has data:** exactly 1 region, optionally with evidence qualifier (📊H/📊M/📊L)
   - ❓ **empty / sparse:** 0 regions have data
6. Highlight: cross-region patterns, regional divergences, empty/sparse cells

**Output:** `knowledge-base/analysis/round2-comparison-matrix.md` with compact table + cell-detail section (table first, prose second). Include batch note with coverage statistics.

**End conditions:** Matrix has rows for filtered sub-themes; columns for all cultural regions; each populated cell has at least one `[[wikilink]]`; cross-region patterns (≥2), divergences (≥2), and gaps (≥5) sections populated; evidence strength and agreement defined per operational rules; batch note appended.

---

## Round 3: Contradiction & Methodology Deep-Dive

**Input:** Round 2 output, findings-index.json, finding entities and appraisal files.

**Procedure:**
1. **Contradiction-identification algorithm (NEW in v3.0):**
   a. For each matrix cell with ≥2 papers, extract the direction/sign of each finding (increasing/decreasing, high/low, persistent/narrowing)
   b. Flag cells where papers have opposite-direction claims
   c. For each flagged cell, read the finding entities to verify methodological/cultural comparability
   d. This produces reproducible contradiction selection
2. For each contradiction, analyze: methodological differences, cultural sub-context differences, temporal differences, definitional differences
3. **Cultural-context similarity threshold (NEW):** Pair findings from the SAME region (e.g., East Asia-East Asia) or comparable development level (e.g., post-industrial OECD). Flag cross-region pairs as "exploratory" rather than confirmed.
4. **Assess resolvability (REFINED in v3.0):** Three categories:
   - **Resolvable:** Contradiction disappears when methods are controlled for
   - **Genuine:** Contradiction persists across studies using the same method
   - **Partially resolvable (NEW):** Contradiction reflects a real sub-context difference (urban vs rural, young vs old, pre-COVID vs post-COVID)
5. Identify methodology patterns where methodology choice systematically influences findings (self-report vs observation, short vs long duration, small vs large sample, WEIRD vs non-WEIRD, quantitative vs qualitative)

**Output:** `knowledge-base/analysis/round3-contradictions.md` with `#status/contradicted` tags and `[[wikilink]]` pairs.

**Tag application (NEW in v3.0):** Instead of editing each finding file individually, use a batch-tag script or include the tagging in the contradiction document as a mapping table. The PM can apply tags centrally.

**End conditions:** At least 4 distinct contradiction pairs documented (raised from 3); each contradiction has findings-in-tension, methodology analysis, cultural sub-context, and assessment; at least 2 methodology patterns identified; resolvable/genuine/partially-resolvable classification used; research question leads noted for Round 5; batch note appended.

---

## Round 4: Gap Analysis & Blind Spot Mapping

**Input:** Rounds 2-3 outputs, unified candidate list, coverage report, findings-index.json.

**Procedure:**
1. **Gap derivation method (NEW in v3.0):** For each behavior domain in the matrix, count empty cells per region. Any region with 0 populated cells for that domain = a gap. Cross-reference with Round 2's gap list. Verify all Round 2 gaps are included as a superset.
2. Region × behavior domain gaps
3. Under-studied populations: children, elderly, disabled, rural, informal economy, indigenous, migrants, LGBTQ+, working class
4. Methodological blind spots: over-reliance on self-report, short durations, WEIRD bias, cross-sectional vs longitudinal, quantitative vs qualitative
5. Temporal gaps: weekday vs weekend, seasonal, holiday vs routine, life-stage transitions, pre/during/post COVID — if the dataset has no coverage for a dimension, note this as a "gap-on-gap" finding (valid)
6. Disciplinary blind spots: which behavior domains are studied by which disciplines, missing cross-disciplinary connections — use provided discipline-reference table if available

**Entity-existence check (NEW):** Before writing wikilinks to `[[population/...]]` or `[[behavior/...]]` entities, verify they exist or will be created. If they don't exist, flag as "proposed entity."

**Output:** `knowledge-base/analysis/round4-gaps.md` with `#status/gap` tags and `[[behavior/{domain}]]` wikilinks.

**End conditions:** All 5 sections documented; at least 15 distinct gaps identified (raised from 10); at least 3 gaps per section; each gap uses `[[wikilink]]` where possible; `#status/gap` tags applied; cross-round verification passed (Round 2 gaps are a subset); priority gaps for Round 5 flagged; batch note appended.

---

## Round 5: Novel Research Question Generation

**Input:** Rounds 1-4 outputs.

**Procedure (REFINED in v3.0):**
1. From Round 2 cross-region patterns: formulate hypothesis question + local variation question
2. From Round 3 contradictions: formulate resolution questions
3. From Round 4 gaps: formulate gap-filling questions (with population, behavior, methodology specified)
4. Interdisciplinary bridge questions: 3-5 questions explicitly cross-disciplinary — note that some questions will naturally overlap with gap-filling. Classify by PRIMARY source (the source that provides the stronger motivation). Document cross-source classification.
5. **Deduplication step (NEW):** After generating all questions, scan for overlap. If two questions ask about the same phenomenon from different framings, merge into a single question with both motivations, or keep only the stronger one. Mark the merge in the batch note.
6. Assess each question: novelty, feasibility, potential impact
7. Prioritize top 10

**Question counting (NEW):** Use sequential numbering (A1-A9, not A1, A1b, A7) to prevent miscounts. After writing, run: `powershell -Command "(Select-String -Path 'output.md' -Pattern '^### [A-D]').Count"` to verify the total.

**Output:** `knowledge-base/analysis/round5-research-questions.md` with `[[wikilink]]` references to the gap/contradiction/pattern that motivated each question. Batch note includes: total question count, by-source breakdown, deduplication log, top 10 rationale.

**End conditions:** At least 4 sections (pattern-derived, contradiction-derived, gap-derived, bridge); at least 15 total questions; each question has motivation (with `[[wikilink]]`), methodology suggestion, novelty/feasibility/impact assessment; top 10 prioritized with rationale; deduplication done and documented; question count verified by command; batch note appended.

---

## Why Sequential (Not Parallel)?

The rounds are sequential by design because each builds on the previous:
- Gaps (Round 4) are meaningful only after patterns (Rounds 1-2) are established
- Contradictions (Round 3) require knowing what exists
- Research questions (Round 5) require knowing gaps, contradictions, and patterns

**Exception:** Within each round, sub-tasks can be parallelized (e.g., one sub-agent per behavior domain for Round 1).

---

## Paywall-Weighted Discipline (REFINED in v3.0)

Use the dual evidence model (`#access/{type}` + `#evidence/{level}`) throughout:
- Findings from `access/abstract-only` papers contribute less to:
  - Cross-region patterns (lower confidence)
  - Contradiction identification (less able to verify claims)
  - Research question grounding (questions derived solely from abstract-only findings are "speculative")
- In Round 5, classify questions as:
  - **Evidence-derived** — grounded in verified findings (access/full-text + evidence/high or medium)
  - **Gap-derived** — grounded in documented gaps (legitimate, not speculative)
  - **Speculative** — grounded in neither findings nor gaps (pure extrapolation)
- Note the proportion of abstract-only papers in the corpus and how this affects confidence

---

## What NOT to Do

- Do NOT skip rounds — each builds on the previous
- Do NOT run rounds in parallel — they depend on each other
- Do NOT fabricate findings — pull only from entities and appraisal files
- Do NOT create new entities during analysis (use what is in the knowledge base)
- Do NOT proceed to synthesis (Phase 7) without the checkpoint (Phase 6)
- Do NOT ignore truncation warnings — re-read the truncated portion
- Do NOT skip the cross-round dependency check
