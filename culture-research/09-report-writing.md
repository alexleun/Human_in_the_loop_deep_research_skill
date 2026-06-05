# Phase 9: Report Writing (NEW in v3.0)

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

## Output Types

| Type | Target Audience | Length | Format |
|---|---|---|---|
| Science magazine article | Educated public | 3,000-4,000 words | Markdown + HTML |
| Research brief | Policy makers / practitioners | 1,000-1,500 words | Markdown |
| Executive summary | Project stakeholders | 500-800 words | Markdown |
| Slide deck | Conference / seminar | 10-15 slides | Markdown or HTML |

---

## Science Magazine Article Procedure

### 1. Style Calibration
Before writing, research the target publication's style:
- Fetch 2-3 sample articles from the publication
- Analyze: sentence length, paragraph structure, use of sub-headings, citation style, tone (formal vs conversational), use of data vs narrative
- Produce a brief "style guide" note for sub-agents

### 2. Article Structure Template
```
## Opening Hook (200-300 words)
- Anecdote, provocative question, or striking data point
- Establishes why the topic matters

## Chapter 1: {Theme} (400-500 words)
- Key cross-cultural pattern with examples
- Human narrative or case study

## Chapter 2: {Theme} (400-500 words)
- Second major pattern or contradiction
- Contrast between regions

## Chapter 3: {Theme} (400-500 words)
- Methodological insight or surprising finding
- What we thought we knew vs what the data shows

## Chapter 4: {Theme} (400-500 words)
- Gap or blind spot with real-world consequences
- Who is missing from the research

## Chapter 5: {Theme} (400-500 words)
- Novel research direction with practical implications
- What future studies should investigate

## Chapter 6: {Theme} or Synthesis (400-500 words)
- Pulling threads together
- Broader implications

## Closing (200-300 words)
- Return to opening hook
- Forward-looking statement
```

### 3. Sub-Agent Writing Pattern
Launch sub-agents **sequentially** (one per chapter) with:

**Per-chapter prompt contains:**
- Style guide (1-2 paragraphs)
- Source material: relevant section from synthesis.md, 2-3 supporting findings from findings-index.json
- Word count target (e.g., 450 words)
- Output path: `knowledge-base/article/chapter-{N}.md`
- Instructions: "Write 10% below the target word count. Sub-agents tend to overproduce."

**Checkpoints:**
- Review after chapters 1, 3, and 5 (or after 2-3 chapters when running sequentially)
- Check: voice consistency, data accuracy, repetition across chapters

### 4. Article Assembly
After all chapters are written:
1. Concatenate into `knowledge-base/article/final-article.md`
2. Verify: smooth transitions between chapters, no repetition, consistent voice
3. Verify all factual claims against source synthesis

### 5. HTML Export (Optional)
If HTML output is requested:
1. Use a basic CSS template for styling (fonts, colors, layout)
2. Embed CSS in the HTML file (standalone, no external dependencies)
3. Export images inline if applicable
4. Save to `knowledge-base/article/final-article.html`

**CSS template approach:** Minimal, clean typography. Use system fonts (Georgia/serif for body, Helvetica/sans-serif for headers). Single-column layout. Max width 720px. Responsive via viewport meta tag.

### 6. Quality Review Checklist
Before finalizing:
- [ ] Word count within target (within 10%)
- [ ] All factual claims traceable to synthesis.md
- [ ] No fabricated quotes
- [ ] No broken `[[wikilink]]` references
- [ ] Consistent voice across all chapters
- [ ] Opening and closing reference each other
- [ ] HTML validates (if HTML output)

---

## File Naming & Directory Conventions

```
knowledge-base/article/
├── chapter-1.md          # working draft
├── chapter-2.md
├── ...
├── chapter-7.md
├── final-article.md       # assembled markdown
├── final-article.html     # standalone HTML (optional)
└── style-guide.md         # calibration notes
```

---

## Research Brief Procedure

1. Extract top 3-5 findings from synthesis.md
2. Write 1-2 paragraphs per finding with actionable implications
3. Add "What this means for [stakeholder]" section
4. Keep under 1,500 words
5. No jargon without explanation

---

## Executive Summary Procedure

1. Extract from synthesis.md: scope, key findings, top 3 research directions
2. Write 3-5 short paragraphs
3. Keep under 800 words

---

## Slide Deck Procedure

1. Identify 10-15 key messages from synthesis.md
2. One slide per message: header + 1-2 bullet points + supporting data point
3. Slides 1-2: context and scope
4. Slides 3-10: major findings with visual suggestions (tables, maps, comparison charts)
5. Slides 11-13: gaps and future directions
6. Slide 14-15: acknowledgments and references

---

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Output file(s) exist at `knowledge-base/article/` or specified path
2. ✅ All factual claims are traceable to `synthesis.md` or underlying analysis
3. ✅ No fabricated quotes or data
4. ✅ Word count is within 10% of target (if applicable)
5. ✅ Consistent voice/style across all sections
6. ✅ HTML output (if produced) renders without errors
7. ✅ Batch note documents: sections produced, word count, data accuracy check, style calibration notes
8. ✅ Director Observations appended

---

## What NOT to Do

- Do NOT fabricate findings or quotes — always reference the synthesis
- Do NOT use the first sub-agent's chapter output without review
- Do NOT skip the style calibration — inconsistent voice is the most common failure mode
- Do NOT exceed word count targets by more than 10%
- Do NOT introduce claims not present in the synthesis

---

## Common Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| Inconsistent voice across chapters | No style guide shared | Include style guide in every chapter prompt |
| Chapters exceed word count | No explicit limit given | Instruct "write 10% below target" |
| Factual claim not in synthesis | Sub-agent extrapolated | Verify every claim against synthesis |
| Chapters repeat content | No cross-chapter awareness | After chapter 3 review, note what's covered |
| Repetitive sentence openings | Rushed writing | Review and vary sentence openings |
| HTML output has broken styling | CSS template issues | Test in browser before finalizing |
