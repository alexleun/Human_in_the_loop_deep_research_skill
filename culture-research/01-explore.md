# Phase 1: Explore — Topic Scoping & Intent Analysis

**Purpose:** Understand the cultural domain, determine global vs local scope, define the research question.

**Execution pattern:** Conversational, run in main session with human.

---

## Procedure

1. **Load project context** — README, AGENTS.md, any archived changes, existing knowledge base

2. **Topic-Intent Analysis (NEW in v3.0)** — Determine research scope:
   - **Global scope:** Question asks about human behavior across multiple cultures/regions. Requires region-parallel search (6+ regions), cross-cultural comparison matrix, multi-round analysis.
   - **Local scope:** Question asks about a specific region, culture, or population. Requires depth-first search within that region, region-specific analysis, may skip cross-cultural matrix.
   - Document the scope decision in writing. The skill supports both — adjust regions, search templates, and analysis dimensions accordingly.

3. **Discuss with human:**
   - What is the cultural behavior or practice being studied?
   - What geographic regions and cultural contexts are relevant?
   - What disciplines should be included? (anthropology, sociology, psychology, urban studies, economics, etc.)
   - What is the time scope? (contemporary, historical, generational comparison)
   - What population segments matter? (age groups, urban/rural, gender, socioeconomic)
   - What languages does output need to support?

4. **Surface unknowns** — explicitly ask:
   - What assumptions are we making about this culture?
   - What blind spots might we have?
   - What would cause our conclusions to change?

5. **Define research question** — a single clear question the study aims to answer

6. **Scope check** — estimate paper count and decide if sub-session architecture is needed (>20 papers → use SS)

7. **Initialize `project-state.json` (NEW in v3.0)** — Create at project root with initial state:
   ```json
   {
     "project": "study-name",
     "research_question": "...",
     "scope": "global | local",
     "total_papers": 0,
     "phases_complete": [],
     "current_phase": "explore",
     "deliverables": {}
   }
   ```

---

## When to Switch to Sub-Session Architecture

If expected paper count > 20, or project spans 5+ regions, plan for sub-sessions from the start:
- Create `sub-sessions/` directory early
- Draft sub-session prompts as you go through phases
- Main session becomes the project manager
- Create `messages/` directory for sub-session feedback

If the project is small (<20 papers, <3 regions), single-session execution is fine.

---

### Region-Count Sizing Guide (NEW in v3.2)

When defining regions, consider the relationship between region count and project depth:

| Regions | Typical Papers | Sub-Sessions | Best For |
|---------|---------------|--------------|----------|
| 1–2 (local scope) | 5–15 | 3–5 | Deep dive into single culture, pilot studies |
| 3–4 (focused global) | 20–50 | 10–15 | Balanced depth × breadth, one major comparison |
| 5–6 (broad global) | 40–80 | 15–20 | Comprehensive survey, shallow per region |
| 7+ (exhaustive) | 60+ | 20+ | Encyclopedia coverage; sub-session architecture essential |

Choose the smallest region count that answers the research question. **3–4 regions with 20–50 papers** typically yields the best depth-to-coverage ratio for cross-cultural comparison.

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Topic-intent analysis complete: scope documented as global or local
2. ✅ A research question is defined in writing (1-3 sentences) **AND approved by human**
3. ✅ Geographic regions and disciplines are listed
4. ✅ Population segments and time scope are specified
5. ✅ Key unknowns/assumptions are surfaced and documented
6. ✅ Region-count sizing guidance consulted; count justified
7. ✅ Scope decision made: sub-session architecture vs single-session
8. ✅ If sub-sessions, `sub-sessions/` and `messages/` directories created, `SS_TEMPLATE.md` in place
9. ✅ `project-state.json` created with initial state

---

## Output

Shared understanding between human and main session. Move to Phase 2 to formalize the search strategy.

---

## What NOT to Do

- Do NOT skip the topic-intent analysis — scope decision affects every downstream phase
- Do NOT skip the scope check — sub-session decision must be made early
- Do NOT commit to specific paper counts before searching
- Do NOT proceed to search (Phase 2) before research question is defined
