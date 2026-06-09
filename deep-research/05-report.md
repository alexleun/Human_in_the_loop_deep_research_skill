# Phase 5: Apply — Report Writing

**Purpose:** Turn findings into a well-structured research document.

## Optional: Discovery-First Framing (for narrative-style reports)

For public-facing or narrative-style reports, apply the **Discovery-First Framing** principle from the culture-research skill instead of the standard template below. Key rules:

- Every section opens with a **claim about the world**, not a claim about your research process.
- **Methodology appears exactly once** — in a single "About this report" endnote, never in the main narrative.
- The report reads as a story about the topic, not a documentation of the analysis process.
- Use an **opening hook** (anecdote, scene, striking data point) to establish stakes before presenting findings.

This framing is recommended when the audience is stakeholders, the public, or cross-disciplinary readers. Use the standard template below when the audience is researchers or technical peers.

## Report Template

```
# Title: <Topic> — <Subtitle>

## Executive Summary
Top findings in plain language (5-7 bullets max). One-sentence takeaway.

## Methodology
Data sources, analytical approach, limitations, reproducibility instructions.

## 1. Background & Context
Why this matters, historical context, key concepts.

## 2. Findings (one section per major finding)
Claim → Evidence (exact source quote) → Analysis → Confidence.

## 3. Synthesis / Phase Model (if applicable)
Periodization or model with visual representation.

## 4. Policy Implications / Significance
What do findings mean? For whom? What would change them?

## 5. Limitations
Data limits, methodological caveats, direction of potential bias.

## 6. Future Research
Unanswered questions, what new data would help, out-of-scope items.

## 7. References
Every source cited with exact quote references. Cross-reference to sources_index.md.
```

## Output Structure: Cards vs Prose

**Do NOT default to card format.** Choose the output structure based on where the content appears:

| Context | Recommended Format | Rationale |
|---|---|---|
| **Standalone chapter page** (e.g., `chapters/health/index.html`) | Card: `<div class="finding">` with claim/evidence/analysis divs | Each finding is self-contained; readers may jump between sections |
| **Executive Summary** in a report page | Prose: flowing `<p>` with inline citations and badges | Cards break the narrative flow; a summary should read as one paragraph |
| **Knowledge-base index page** with embedded chapter content | Prose: each chapter rendered as a `<h3>` heading followed by flowing `<p>` | Readers scan vertically; cards create visual noise at this density |
| **Integrated analysis** where findings build on each other | Prose: sequential paragraphs with transition sentences | Cards isolate findings that need to be read as a cumulative argument |
| **Data gap deep-dive** with Known/Gaps structure | Cards OK, but merge Known+Gaps into the analysis paragraph | The two halves (known, gaps) are read together |

### Card Format (for standalone chapter pages)

```html
<div class="finding" data-confidence="HIGH|MEDIUM|LOW" data-source="SOURCE-ID">
  <h3>Finding Title</h3>
  <div class="claim">The core claim, stated directly.</div>
  <div class="evidence">
    "Exact quoted text from the source material."
    <em>— Issuing Body, Date</em>
  </div>
  <div class="analysis">
    Interpretation, cross-references to other findings, caveats.
  </div>
  <div><span class="confidence-badge confidence-HIGH">HIGH</span></div>
</div>
```

### Prose Format (for summaries, integrated pages, knowledge-base)

```html
<h3>Finding Title</h3>
<p>The core claim, stated directly, with the supporting quote integrated inline: "Exact quoted text" (Source, Date). The analysis continues as part of the same paragraph flow. <strong>Data Gap:</strong> Description of gap. <span class="confidence-badge confidence-HIGH" data-tip="...">HIGH</span></p>
```

Rules for prose format:
- Merge claim + evidence quote + analysis into 1-2 `<p>` tags per finding
- Keep the quote in quotation marks with attribution in parentheses
- Keep `<strong>Data Gap:</strong>` inline within the paragraph (not a separate `<p>`)
- Confidence badge goes at the end of the paragraph
- Do NOT use `<div class="finding">`, `<div class="claim">`, `<div class="evidence">`, or `<div class="analysis">` wrappers — they add no value in prose mode and complicate responsive layout
- Transition paragraphs (`<p class="transition">`) between findings maintain narrative flow in prose mode

### Attribute Rules (apply to both formats)

- **`data-confidence`**: Required on every finding. Values: `HIGH` (multiple independent sources), `MEDIUM` (single source or indirect), `LOW` (extrapolation or limited evidence). Use a single attribute — do NOT duplicate as both `data-confidence` and `confidence`.
- **`data-source`**: Required on every finding div (card format) or optional but recommended in prose format (reference source in the attribution).
- **Confidence badge**: Each finding must have a visible `<span class="confidence-badge">` matching its confidence level.
- These attributes enable the bilingual parity verification script (`final_verify.py`) to detect missing citations.

### Structural Rules

- No inline styles (`style="..."`) — use semantic classes only
- No scripts (`<script>`)
- Every finding needs a unique `data-source` (can share IDs across findings)
- The `<h3>` title should match across EN/ZH versions for structural parity
- **Attribute consistency**: After writing, scan for `confidence="` (without `data-` prefix) — this is a common typo that silently breaks parity checks. Use a single attribute name.

## Writing Principles

- **Claim → Evidence → Analysis → Confidence**: every finding follows this sequence
- **Plain language first**: executive summary accessible to non-specialists
- **Visual anchor**: key finding gets a table/chart/diagram within 3 paragraphs
- **Cross-reference findings**: synthesize across domains, don't silo
- **Source IDs in findings enable automated verification**: without them, parity and grounding cannot be checked at scale

## Visuals Matching Findings

| Finding Type | Best Visual | Location |
|---|---|---|
| Overview / geography | SVG map | `project/web/images/` |
| Time-series trends | Line chart | `project/web/images/` |
| Correlations | Heatmap / scatter | `project/web/images/` |
| Event impacts | Before/after bars | `project/web/images/` |
| Comparisons | Grouped bars / radar | `project/web/images/` |
| Phases | Colored cards / timeline | Inline or SVG |

## Fallback Consciousness in Reports

If the report describes a system that consumes data (dashboard, API, interactive map), include a **fallback state** description: what the system shows when the data store is empty, and how the user distinguishes fallback from live data. This is especially important for executive demos where the data pipeline may not be fully populated.

## Cross-Phase Integration

**Important:** The `data-source` attributes written here feed directly into the Phase 6 encoding verification and Phase 7 bilingual parity checks. If a finding lacks `data-source`, it will appear as a gap in the automated verification script (`final_verify.py`). Write citations first — do not plan to add them later.

## Cross-Platform Parity Test Requirement

The bilingual parity checker script (`check-parity.py`) must be tested on the **target OS** (Windows/macOS/Linux) before considering parity verified. A script that passes on the LLM's platform may fail on yours due to:

- **Encoding defaults**: Windows PowerShell defaults to ANSI/cp950; Python `print()` may raise `UnicodeEncodeError` when outputting Chinese characters to the console
- **Path separators**: `\` vs `/` in glob patterns
- **Line endings**: CRLF vs LF may affect regex matching

**Verification protocol:**
1. Generate the parity checker script during Phase 6
2. Before marking Phase 6 or Phase 7 complete, run the script on the target OS
3. Fix any OS-specific issues (stdout encoding wrappers, path normalization) immediately
4. Add the OS-specific fix to the script's `__main__` guard, not as a wrapper script

**Experience note (global-heatwave):** `check-parity.py` worked perfectly on the LLM's Linux environment but crashed on Windows with `UnicodeEncodeError: 'charmap' codec can't encode character '\u5317'`. The fix (`sys.stdout.reconfigure(encoding='utf-8')` wrapped in a try/except for Linux compat) was only discovered when the user ran the script. Always test parity on the actual deployment OS.

---

## File Truncation Safeguard (NEW in v2.0)

Long report files may exceed 50KB. After reading any report draft or source material, check for truncation markers. Read critical sections (methodology, references) with offset parameters.

---

## End Conditions (NEW in v2.0)

This phase is **complete** when ALL of the following are true:

1. ✅ All report sections drafted (executive summary, methodology, findings, synthesis, limitations, future research, references)
2. ✅ Every finding has: claim → evidence (exact quote) → analysis → confidence
3. ✅ Every finding carries `data-source` and `data-confidence` attributes (or equivalent citation)
4. ✅ Format chosen (cards vs prose) is consistent per page type
5. ✅ No inline styles — semantic CSS classes only
6. ✅ Visuals matched to findings per the mapping table
7. ✅ Cross-phase integration verified — citations exist before Phase 6
8. ✅ task_state.json updated if spanning multiple sessions
