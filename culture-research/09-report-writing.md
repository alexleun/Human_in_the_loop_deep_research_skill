# Phase 9: Report Writing (REFINED in v3.2)

**Purpose:** Produce a science communication output from the synthesis document — science magazine article, research brief, slide deck, or executive summary.

**Execution pattern:** Run as sub-sessions (SS16+). One sub-agent per chapter/section, executed sequentially. Each agent writes to a shared directory.

---

## When to Use This Phase

- User wants a public-facing article (The Atlantic / Aeon / Sapiens style)
- User wants a research brief for stakeholders
- User wants an executive summary of findings
- User wants a presentation slide deck

If the user only wants the synthesis document, skip this phase.

---

## Core Principle: Discovery-First Framing (NEW in v3.2)

**The most common failure in report writing is producing output that reads as a methodology report or academic literature review rather than a science story.** This happens because the synthesis document (Phase 7) is structured around the research process, and carrying that structure into the communication output shifts the subject from "what we discovered" to "how we collected."

**The rule: the reader should feel they are learning about the [research topic], not about your research process.** Every paragraph should answer the question "what does this tell us about [the topic]?" not "what did we uncover in our literature search?"

**Concrete checks applied before every write:**
- Does the first sentence of each section open with a claim about the world, not a paper citation?
- Does the phrase "across X studies / Y papers" appear more than once in the entire document? (It should appear exactly once, in the endnote.)
- Is the collection methodology (search protocol, paper count, analysis rounds) in the main narrative, or relegated to a single endnote or "About this report" section?
- Are source papers introduced as supporting evidence for claims (not as the subject of each sentence)?

**If any check fails, restructure the section.** This single principle, if applied before drafting, prevents the most common and most time-consuming failure in this phase.

---

## Output Types

| Type | Target Audience | Length | Format |
|---|---|---|---|
| Science magazine article | Educated public | 3,000–10,000 words | Markdown + HTML |
| Research brief | Policy makers / practitioners | 1,000–1,500 words | Markdown |
| Executive summary | Project stakeholders | 500–800 words | Markdown |
| Slide deck | Conference / seminar | 10–15 slides | Markdown or HTML |

For science magazine articles, use the variable-length planning table below instead of the fixed 400-500 word chapter template from v3.0.

---

## Science Magazine Article Procedure

### Before Starting: Pre-Writing Section Plan Approval (NEW in v3.2)

Do NOT write any chapter content until the human approves a section plan. This prevents the "misaligned voice across all chapters" failure mode.

**Section plan document should contain:**
1. Article title (working)
2. Narrative arc (1 paragraph — the story of the article)
3. Target publication style (e.g., Aeon, The Atlantic, Quanta, Sapiens)
4. Chapter/section list with for each:
   - Working title
   - Narrative purpose (hook / build tension / reveal / reflect)
   - One-sentence claim (the single thing this section says)
   - Key sources (2-3 papers or findings)
   - Target word count
5. Opening and closing concept (how the article will open and close, ideally a circular structure)

**Gate:** The human approves the section plan before any chapter is written. The section plan is saved to `report/section-plan.md`. If the plan is rejected, revise the section plan — do not start writing.

### 1. Style Calibration (REFINED in v3.2)

Before writing, research the target publication's style. Produce a `report/style-guide.md` note.

**Calibration checklist (concrete features to analyze):**
- Sentence length profile: average words per sentence? variance? (short punchy? long flowing? mixed?)
- Paragraph length: typical range? (2-3 sentence impact paragraphs? 5-8 sentence exposition?)
- First-sentence pattern: do sections start with a scene, a question, a claim, or a citation?
- Citation style: inline citations? footnotes? endnotes? named ("Smith found") or numbered?
- Use of data: how are numbers presented? (raw stats? rounded? visualized in prose?)
- Use of narrative: case studies? named individuals? composite scenes?
- Metaphor/analogy density: roughly how often per 500 words?
- Tone markers: first person? "we" voice? authoritative vs speculative? hedging frequency?

**Heuristics for common styles (v3.2):**
| Style | Sentences | Paragraphs | Openings | Citations | Data |
|---|---|---|---|---|---|
| Aeon / Quanta | Mixed, 15-25 words avg | Variable (2-8 sentences) | Scene, question, or claim | Endnotes or light inline | Rounded, in prose |
| The Atlantic | Punchy, 12-18 words avg | Short (2-4 sentences) | Anecdote or provocative claim | Named ("Smith found") | Minimal, narrative-driven |
| Sapiens | Flowing, 18-28 words avg | Medium (3-6 sentences) | Cultural scene or historical context | Endnotes | Contextualized |
| Nature News | Concise, 10-15 words avg | Very short (1-3 sentences) | Data point or finding | Named + journal | Precise, cited |

### 2. Variable-Length Planning (NEW in v3.2)

Long-form articles (5,000–10,000 words) need variable pacing — some sections tight (400 words), others expansive (900 words). Use the density planning table:

| Section Role | Typical Word Count | Density | Purpose |
|---|---|---|---|
| Opening hook / scene | 200–400 | Tight | Grab reader, establish stakes |
| Context / background | 300–500 | Medium | Orienting information |
| Core finding (major) | 600–1,000 | Expansive | Deep dive, evidence, narrative |
| Core finding (minor) | 300–500 | Medium | Supporting pattern |
| Contradiction / tension | 500–800 | Medium/expansive | Build uncertainty |
| Gap / blind spot | 300–500 | Tight | Frustrate, motivate |
| Future directions | 400–600 | Medium | Forward-looking |
| Closing reflection | 200–400 | Tight | Circular return, resonance |

Plan total: 3,000–10,000 words depending on depth. Document the density plan in the section plan before writing.

### 3. Article Structure Template (REFINED in v3.2)

```
## Opening Hook (200-400 words)
- Anecdote, provocative question, or striking data point
- Establishes why the topic matters
- No methodology, no paper citations

## Part I: {Theme} (variable length)
- Core cross-cultural pattern with examples
- Narrative or case study
- Sources as evidence for claims, not subject of sentences

## Part II: {Theme} (variable length)
- Second major pattern or contradiction
- Contrast between regions or populations

## Part III: {Theme} (variable length)
- Methodological insight or surprising finding
- What we thought we knew vs what the data shows

## Part IV: {Theme} (variable length)
- Gap or blind spot with real-world consequences
- Who is missing from the research

## Part V: {Theme} (variable length)
- Novel research direction with practical implications
- What future studies should investigate

## Closing (200-400 words)
- Return to opening hook
- Forward-looking statement

## About this report / Methodology (single endnote)
- Collection method described ONCE
- Paper count, regions, search approach
- Link to full knowledge base
```

### 4. Sub-Agent Writing Pattern (REFINED in v3.2)

Launch sub-agents **sequentially** (one per chapter) with explicit discovery-first framing instructions in every prompt.

**Per-chapter prompt contains:**
- Style guide (1-2 paragraphs, from section 1 above)
- Discovery-first reminder: "Lead with a claim about the world, not a paper citation"
- Source material: relevant section from synthesis.md, 2-3 supporting findings from findings-index.json
- Word count target (from density plan)
- Output path: `report/chapter-{N}-{title}.md`
- Instructions: "Write 10% below the target word count. Sub-agents tend to overproduce."

**Checkpoints:**
- Review after chapters 1, 3, and 5 (or after 2-3 chapters when running sequentially)
- Check: voice consistency, data accuracy, repetition across chapters, discovery-first compliance

**Alternative: collaboration-first pattern (v3.2):** For complex topics, instead of launching sub-agents, draft each section yourself and present it for human approval before proceeding. This catches framing issues earlier and allows fine-grained style calibration per section. Use this pattern when:
- The topic has a strong narrative arc that benefits from unified voice
- The user has strong editorial preferences
- The first sub-agent draft fails the discovery-first check

### 5. Article Assembly
After all chapters are written:
1. Concatenate into `report/combined-report.md`
2. Verify: smooth transitions between chapters, no repetition, consistent voice
3. Verify all factual claims against source synthesis
4. Verify discovery-first compliance: no methodology in main narrative, opening sentence per section is a claim about the world

### 6. HTML Export (Optional)
If HTML output is requested:
1. Use a basic CSS template for styling (fonts, colors, layout)
2. Embed CSS in the HTML file (standalone, no external dependencies)
3. Export images inline if applicable
4. Save to `report/final-article.html`

**CSS template approach:** Minimal, clean typography. Use system fonts (Georgia/serif for body, Helvetica/sans-serif for headers). Single-column layout. Max width 720px. Responsive via viewport meta tag.

### 7. Quality Review Checklist (REFINED in v3.2)
Before finalizing:
- [ ] Word count within target (within 10%)
- [ ] **Discovery-first framing check: no section opens with methodology or paper citation**
- [ ] **Methodology appears exactly once — in an endnote or "About this report" section**
- [ ] All factual claims traceable to synthesis.md
- [ ] No fabricated quotes
- [ ] No broken `[[wikilink]]` references
- [ ] Consistent voice across all chapters
- [ ] Opening and closing reference each other (circular structure)
- [ ] HTML validates (if HTML output)

---

## Methodology Placement Rule (NEW in v3.2)

**Collection methodology (search protocol, paper count, N findings, analysis rounds) appears exactly once — in a single endnote or "About this report" callout box.** It is never part of the main narrative.

Example endnote:
```
**About this report:** This essay synthesises findings from 38 peer-reviewed studies
published between 2005 and 2025, covering experimental pain tolerance, clinical pain
catastrophizing, pain expression norms, pain coping strategies, and pain disparities
across East Asian, North American, and European populations. The evidence was
organised through a structured knowledge base methodology — 112 individual findings
extracted, categorised by behaviour domain, cultural context, and method type — and
analysed through five iterative rounds of cross-region comparison, contradiction
analysis, gap identification, and research question generation.
```

This rule is the single most important structural difference between a synthesis document (Phase 7) and a communication output (Phase 9).

---

## File Naming & Directory Conventions

```
report/
├── report-charter.md         # editor-in-chief charter (see 08-sub-session-orchestration)
├── section-plan.md           # pre-writing plan approved by human (NEW in v3.2)
├── style-guide.md            # calibration notes
├── chapter-01-{title}.md     # working draft per chapter
├── chapter-02-{title}.md
├── ...
├── chapter-08-{title}.md
├── combined-report.md        # assembled markdown
├── final-article.html        # standalone HTML (optional)
└── rewrite/                  # revision drafts (if needed)
    ├── director-observations.md
    └── pain-cultures-report.md
```

---

## Research Brief Procedure

1. Extract top 3-5 findings from synthesis.md
2. Write 1-2 paragraphs per finding with actionable implications
3. Add "What this means for [stakeholder]" section
4. Keep under 1,500 words
5. No jargon without explanation
6. Apply discovery-first framing: open with the problem, not the research method

---

## Executive Summary Procedure

1. Extract from synthesis.md: scope, key findings, top 3 research directions
2. Write 3-5 short paragraphs
3. Keep under 800 words
4. Methodology appears only in a one-line note at the bottom

---

## Slide Deck Procedure

1. Identify 10-15 key messages from synthesis.md
2. One slide per message: header + 1-2 bullet points + supporting data point
3. Slides 1-2: context and scope
4. Slides 3-10: major findings with visual suggestions (tables, maps, comparison charts)
5. Slides 11-13: gaps and future directions
6. Slide 14-15: acknowledgments and references
7. Slide deck 0: one slide for methodology (skip during presentation if audience doesn't need it)

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Section plan approved by human before drafting began (gate documented)
2. ✅ Output file(s) exist at `report/` or specified path
3. ✅ All factual claims are traceable to `synthesis.md` or underlying analysis
4. ✅ No fabricated quotes or data
5. ✅ Word count is within 10% of target (if applicable)
6. ✅ Consistent voice/style across all sections
7. **Discovery-first framing check: no section opens with methodology or paper citation (NEW in v3.2)**
8. **Methodology appears exactly once: in an endnote or "About this report" section (NEW in v3.2)**
9. ✅ HTML output (if produced) renders without errors
10. ✅ Batch note documents: sections produced, word count, data accuracy check, style calibration notes
11. ✅ Director Observations appended

---

## What NOT to Do

- Do NOT fabricate findings or quotes — always reference the synthesis
- Do NOT use the first sub-agent's chapter output without review
- Do NOT skip the style calibration — inconsistent voice is the most common failure mode
- Do NOT exceed word count targets by more than 10%
- Do NOT introduce claims not present in the synthesis
- **Do NOT write without discovery-first framing — restructure if methodology creeps into the main narrative (NEW in v3.2)**
- **Do NOT skip the pre-writing section plan approval gate (NEW in v3.2)**

---

## Common Failure Modes (EXPANDED in v3.2)

| Failure | Cause | Fix |
|---|---|---|
| **Article reads as methodology report / literature review (NEW)** | No discovery-first framing | Lead every section with a claim about the world, support with evidence. Relegate methodology to single endnote. |
| Inconsistent voice across chapters | No style guide shared | Include style guide in every chapter prompt |
| Chapters exceed word count | No explicit limit given | Instruct "write 10% below target" |
| Factual claim not in synthesis | Sub-agent extrapolated | Verify every claim against synthesis |
| Chapters repeat content | No cross-chapter awareness | After chapter 3 review, note what's covered |
| Repetitive sentence openings | Rushed writing | Review and vary sentence openings |
| HTML output has broken styling | CSS template issues | Test in browser before finalizing |
