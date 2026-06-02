# Phase 1: Explore — Topic Scoping

**Purpose:** Understand the cultural domain, map what is known/unknown, define the research question.

**Execution pattern:** Conversational, run in main session with human.

---

## Procedure

1. **Load project context** — README, AGENTS.md, any archived changes, existing knowledge base
2. **Discuss with human:**
   - What is the cultural behavior or practice being studied?
   - What geographic regions and cultural contexts are relevant?
   - What disciplines should be included? (anthropology, sociology, psychology, urban studies, economics, etc.)
   - What is the time scope? (contemporary, historical, generational comparison)
   - What population segments matter? (age groups, urban/rural, gender, socioeconomic)
   - What languages does output need to support?
3. **Surface unknowns — explicitly ask:**
   - What assumptions are we making about this culture?
   - What blind spots might we have?
   - What would cause our conclusions to change?
4. **Define research question** — a single clear question that the study aims to answer
5. **Scope check** — estimate paper count and decide if sub-session architecture is needed (>20 papers → use SS)

---

## When to Switch to Sub-Session Architecture (NEW in v2.0)

If the expected paper count exceeds 20, or the project spans 5+ regions, plan for sub-sessions from the start:
- Create `sub-sessions/` directory early
- Draft sub-session prompts as you go through phases
- Main session becomes the project manager

If the project is small (<20 papers, <3 regions), single-session execution is fine.

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ A research question is defined in writing (1-3 sentences)
2. ✅ Geographic regions and disciplines are listed
3. ✅ Population segments and time scope are specified
4. ✅ Key unknowns/assumptions are surfaced and documented
5. ✅ Scope decision made: sub-session architecture vs single-session
6. ✅ If sub-sessions, the `sub-sessions/` directory is created and an `SS_TEMPLATE.md` is in place

---

## Output

Shared understanding between human and main session. Move to Phase 2 to formalize the search strategy.

---

## What NOT to Do

- Do NOT skip the scope check — the sub-session decision must be made early
- Do NOT commit to specific paper counts before searching
- Do NOT start the openspec change before research question is defined
