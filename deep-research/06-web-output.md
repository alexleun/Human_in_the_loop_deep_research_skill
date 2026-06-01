# Phase 6: Apply — Web Output Generation

**Purpose:** Produce a bilingual website presenting the research professionally.

## Site Architecture (Template)

```
output/
├── index.html                  ← Landing page (English)
├── final-report.html           ← Comprehensive final report
├── synthesis.html              ← Integrated cross-domain analysis (if depth warrants)
├── methodology.html            ← Data pipeline, correction log, confidence framework
├── data.html                   ← Data sources and access (if applicable)
├── solutions.html              ← Solutions overview (if applicable)
├── chapters/                   ← Knowledge base chapters (optional, if KB exists)
│   ├── health/index.html
│   ├── uhi/index.html
│   └── ... (one per KB chapter)
├── knowledge-base.html         ← KB index page (optional)
├── zh/                         ← Target language mirror (zh, ja, ko, etc.)
│   ├── index.html
│   ├── final-report.html
│   ├── synthesis.html
│   ├── methodology.html
│   ├── data.html
│   ├── solutions.html
│   ├── chapters/
│   │   ├── health/index.html
│   │   ├── uhi/index.html
│   │   └── ...
│   └── knowledge-base.html
├── css/
│   └── style.css               ← Shared stylesheet
└── images/                    ← Generated PNG/SVG figures
    ├── figure-01.png
    └── ...
```

**Architecture rules:**
- ZH pages live in a `zh/` subdirectory, not separate `*-zh.html` files
- Image paths in ZH pages use `../images/` prefix
- Nav links within `zh/` stay within the same language (no `../`); language switcher alone crosses the boundary
- Chapter subdirectory pages use deeper relative paths (e.g., `../../css/style.css` from `zh/chapters/health/index.html`)
- For static HTML sites, use the `zh/` subdirectory pattern; for framework-based sites (Next.js, SvelteKit), use i18n routing

## Design System

### Color Palette (recommended base)

```css
:root {
  --primary: #1a365d;       /* Nav, headers */
  --primary-light: #2b6cb0; /* Links, accents */
  --accent: #c53030;        /* Warnings */
  --gold: #d69e2e;          /* Highlights */
  --bg: #fafafa;            /* Background */
  --text: #2d3748;
  --text-light: #718096;
}
```

Customize for the topic: use warmer tones for climate research, cooler tones for technical/datasets.

- **English UI**: sans-serif (`Inter`, `Segoe UI`)
- **Target language text**: appropriate serif (e.g., `Noto Serif TC` for Chinese, `Noto Serif JP` for Japanese)
- **Paper body**: serif (`Georgia`, `Times New Roman`)
- **Cards**: white, rounded, shadow, hover lift
- **Highlight boxes**: colored left-border (blue=finding, red=critical, gold=key)

## Navigation Pattern

All pages share a consistent nav structure with language switcher:

```html
<nav class="top-nav">
  <span class="nav-brand">Project Name</span>
  <span class="nav-sep">|</span>
  <span class="nav-group">
    <a href="index.html">Home</a>
    <a href="final-report.html">Report</a>
    <a href="synthesis.html">Synthesis</a>
    <a href="methodology.html">Methodology</a>
  </span>
  <span style="margin-left:auto;">
    <a href="../index.html">EN</a> / <strong>繁</strong>
  </span>
</nav>
```

**Critical nav rules from experience:**
- EN nav at root: all `href` paths are flat (`href="final-report.html"`)
- ZH nav at root: all `href` paths within the same language are flat (`href="final-report.html"`)
- ZH nav at root: ONLY the language switcher uses `../` to cross into English (`href="../index.html"`)
- Chapter subdirectory pages (e.g., `zh/chapters/health/`): nav paths use `../../../zh/final-report.html` to stay in ZH, language switcher uses `../../../index.html` for EN
- Every page pair (EN + ZH) must have identical nav labels — no variant translations across files

### Page Registry Pattern (Managing Nav at Scale)

When the website exceeds 6-8 pages, maintaining nav links on every page manually becomes error-prone. Use a **Page Registry**:

1. Define all pages in a single source of truth (e.g., a JSON file or Python dict):

```python
# page_registry.py — single source of truth for nav + verification
PAGES = [
    "index.html",
    "final-report.html",
    "synthesis.html",
    "methodology.html",
    "data.html",
    "solutions.html",
]

CHAPTER_PAGES = [
    "chapters/health/index.html",
    "chapters/uhi/index.html",
    "chapters/economic/index.html",
    "chapters/solutions/index.html",
]

KB_PAGES = ["knowledge-base.html"]

ALL_EN_PAGES = PAGES + KB_PAGES + CHAPTER_PAGES

EN_NAV_LABELS = ["Home", "Report", "Synthesis", "Methodology", "Data", "Solutions", "Knowledge Base"]
ZH_NAV_LABELS = ["首页", "报告", "综合分析", "方法", "数据", "解决方案", "知识库"]
```

2. Use the registry in both:
   - **Nav generation**: to produce consistent nav HTML for every page depth level
   - **Parity checker**: to verify every page pair without hardcoding paths

**Experience note from global-heatwave project:** With 15 page pairs (30 files), manual nav updates required editing every file. The Page Registry pattern (added retroactively) would have caught a nav label mismatch and reduced verification time. Define the registry before writing pages, not after.

## Parallel Execution Strategy (for Large Sites)

When generating 10+ page pairs (20+ files), parallelism is essential but introduces consistency risks.

### When to parallelize
- Chapter pages are independent (each chapter has its own content, no cross-references)
- EN and ZH versions can be generated in parallel (separate sub-agents)
- SVGs and CSS are generated once, shared across pages

### How to parallelize safely

1. **Define the Page Registry first** (see above). This is the single source of truth for nav links and page lists.
2. **Generate shared assets first** (CSS, SVGs, JS) — these must exist before pages reference them.
3. **Dispatch by depth level**, not by language:
   - Batch 1: All root-level pages (EN + ZH + nav template)
   - Batch 2: All chapter pages (EN + ZH with deeper relative paths)
   - Batch 3: Knowledge-base and other special pages
4. **Each sub-agent must receive:**
   - The Page Registry (so nav links are consistent)
   - The nav HTML template for the correct depth level
   - The output structure format (cards vs prose) for each page type
   - The confidence badge HTML template (exact `<span>` syntax)
5. **After all sub-agents complete:**
   - Run the encoding check (Gate 1) on every ZH file
   - Run the parity checker across all EN/ZH pairs
   - Spot-check nav links across 3 depth levels (root, `zh/`, `zh/chapters/<name>/`)

### Consistency risks with parallelism
| Risk | Mitigation |
|---|---|
| Different sub-agents use different translation variants for nav labels | Pass the exact ZH nav label list to every sub-agent |
| Different depth level paths (`../../` vs `../../../`) | Pass the exact depth prefix to each sub-agent based on its target directory |
| Confidence badge HTML varies | Pass the exact `<span>` template to every sub-agent |
| Some sub-agents use card format, others prose | Specify format per page type in the task prompt |

## Landing Page Structure

```
NAV: sticky bar
HERO: title + subtitle + metadata
STATS GRID: key metrics in colored cards (if applicable)
DOMAIN CARDS: each linking to its domain report or chapter
FIGURES GALLERY: charts with captions (optional)
FOOTER: source citation, disclaimer, last updated
```

## Report / Chapter Page Structure

### Choose Card or Prose Format

**Do NOT default to card format.** The pre-deployment parity checker (below) must be updated to handle whichever format you choose, because it counts `<div class="finding">` elements — which don't exist in prose mode.

| Context | Recommended | Why |
|---|---|---|
| Standalone chapter page | Card format | Readers jump between sections; cards keep findings self-contained |
| Executive summary | Prose format | Summary should read as one flowing paragraph |
| Knowledge-base with embedded chapters | Prose format | Dense vertical content reads better without card borders |
| Integrated analysis chapter | Prose format | Findings build on each other; prose shows the accumulation |
| Knowledge-base index page with chapter grid | Grid of chapter cards + prose entries | Chapter cards for navigation, prose for content |

See Phase 5 (`05-report.md`) for exact HTML of each format.

**Card format:**
```html
<div class="finding" data-confidence="HIGH|MEDIUM|LOW" data-source="SOURCE-ID">
  <h3>Finding Title</h3>
  <div class="claim">Core claim stated directly.</div>
  <div class="evidence">"Exact quoted text from source."</div>
  <div class="analysis">Interpretation and cross-referencing.</div>
  <div><span class="confidence-badge confidence-HIGH">HIGH</span></div>
</div>
```

**Prose format (no `div.finding` wrappers):**
```html
<h3>Finding Title</h3>
<p>Core claim with "exact quoted text" (Source, Date) integrated inline. Analysis continues in the same paragraph. <strong>Data Gap:</strong> Description. <span class="confidence-badge confidence-HIGH" data-tip="...">HIGH</span></p>
```

**Critical: when using prose format, update the parity checker.** Remove the `div.finding` count check for prose pages, or parameterize which pages use which format.

Rules (both formats):
- Every `data-confidence` maps to a confidence badge: HIGH / MEDIUM / LOW
- Every `data-source` references IDs from `sources_index.md` (card) or cited in attribution (prose)
- No inline styles — use semantic CSS classes only
- No `<script>` tags
- The `<h3>` title must match across EN/ZH versions for structural parity
- **Single attribute**: use `data-confidence` only, not `confidence` (without `data-` prefix). Both attributes on the same element silently breaks parity checks.

## Bilingual Content Strategy

| Element | Approach |
|---|---|
| Page structure | Same HTML template for both languages |
| Navigation | Translated labels, verified consistent across ALL pages |
| Content | Full translation, not summaries |
| Figures | Same for both (language-neutral) |
| CSS | Same system; target language pages use serif fonts |
| Language switch | EN → links to `../zh/`, ZH → links to `../` |
| Image paths | ZH pages use `../images/` prefix; chapter pages use `../../images/` |
| Encoding | UTF-8 without BOM; verify no U+FFFD after generation |

## Pre-Deployment Verification

Before considering the web output complete, run an automated check using the Page Registry:

```python
# check-parity.py — parameterized by Page Registry
import os, re, sys

OUTPUT_DIR = "output"
ZH_DIR = os.path.join(OUTPUT_DIR, "zh")

# === Page Registry (single source of truth) ===
# Pages that use CARD format (<div class="finding">)
CARD_PAGES = [
    "final-report.html",          # chapter sections still use cards... UPDATE if you switch to prose
    "chapters/health/index.html",
    "chapters/uhi/index.html",
    "chapters/economic/index.html",
    "chapters/equity/index.html",
    "chapters/solutions/index.html",
    "chapters/feedbacks/index.html",
    "chapters/data-gaps/index.html",
    "chapters/integrated-analysis/index.html",
]

# Pages that use PROSE format (no <div class="finding">)
PROSE_PAGES = [
    "index.html",                  # landing page — no findings
    "synthesis.html",
    "methodology.html",
    "data.html",
    "solutions.html",
    "knowledge-base.html",         # inline chapter content as prose
]

ALL_PAGES = CARD_PAGES + PROSE_PAGES

EN_NAV_LABELS = ["Home", "Report", "Knowledge Base", "Knowledge Graph", "Synthesis", "Methodology", "Data", "Solutions", "Dashboard"]
ZH_NAV_LABELS = ["首页", "报告", "知识库", "知识图谱", "综合分析", "方法", "数据", "解决方案", "仪表板"]

def check_pair(en_path, zh_path, fname):
    """Check a single EN/ZH page pair for structural parity."""
    issues = []
    en_text = open(en_path, encoding="utf-8").read()
    zh_text = open(zh_path, encoding="utf-8").read()

    # Encoding check (BLOCKING)
    if "\ufffd" in zh_text:
        issues.append(f"CORRUPT: U+FFFD in {zh_path} — must regenerate")

    # lang attribute
    if '<html lang="zh">' not in zh_text:
        issues.append(f"LANG: missing <html lang=\"zh\"> in {fname} (ZH)")

    # Finding count parity — only for card-format pages
    if fname in CARD_PAGES:
        en_findings = en_text.count('<div class="finding"')
        zh_findings = zh_text.count('<div class="finding"')
        if en_findings != zh_findings:
            issues.append(f"PARITY: {fname} finding count EN={en_findings} ZH={zh_findings}")
    else:
        # Prose pages: verify NO finding divs remain (they were converted)
        en_remnants = en_text.count('<div class="finding"')
        zh_remnants = zh_text.count('<div class="finding"')
        if en_remnants > 0 or zh_remnants > 0:
            issues.append(f"PROSE: {fname} is prose-format but has {en_remnants} (EN) / {zh_remnants} (ZH) finding divs")

    # Attribute consistency (catch 'confidence' without 'data-' prefix)
    for attr_variant in ['confidence="', 'data-confidence="']:
        en_c = en_text.count(attr_variant)
        zh_c = zh_text.count(attr_variant)
        if en_c > 0 and en_text.count('data-source=') == 0 and attr_variant == 'confidence="':
            # If no data-source but has confidence, might be prose format — fine
            pass
    # Cross-check: if 'confidence="' count differs from 'data-confidence="' count in the same file
    en_conf = en_text.count('confidence="')
    en_dconf = en_text.count('data-confidence="')
    if en_conf != en_dconf and fname not in PROSE_PAGES:
        issues.append(f"ATTR: {fname} (EN) has confidence={en_conf} but data-confidence={en_dconf} — mismatched attributes")

    # Nav label consistency
    nav = re.search(r'<nav[^>]*>.*?</nav>', zh_text, re.DOTALL)
    if nav:
        zh_labels = re.findall(r'>([^<]+)</a>', nav.group(0))
        # Filter out nav-brand text and separators
        known = set(ZH_NAV_LABELS + ["EN", "ZH"])
        unexpected = [l for l in zh_labels if l.strip() not in known and l.strip() and not l.startswith('&#')]
        for label in unexpected:
            issues.append(f"NAV: {fname} (ZH) unexpected label: '{label.strip()}'")

    # Depth check: verify nav links use correct relative depth for subdirectory pages
    depth = fname.count('/')  # 0 for root, 1 for zh/, 2 for zh/chapters/health/
    if depth >= 1:
        # Check that zh/ pages link to ../knowledge-graph-intro.html (not plain)
        en_has_en_only_links = '../knowledge-graph-intro' in en_text
        zh_has_en_only_links = '../knowledge-graph-intro' in zh_text
        # (This is advisory — the correct depth depends on the page's directory)
        if '../' not in zh_text and depth > 0:
            issues.append(f"DEPTH: {fname} (ZH) may have wrong relative paths — no '../' found in subdirectory page")

    return issues

def main():
    all_issues = []
    for page in ALL_PAGES:
        en_path = os.path.join(OUTPUT_DIR, page)
        zh_path = os.path.join(ZH_DIR, page)
        if not os.path.exists(en_path) or not os.path.exists(zh_path):
            print(f"  SKIP {page}: missing file")
            continue
        issues = check_pair(en_path, zh_path, page)
        if issues:
            print(f"  FAIL {page}: {len(issues)} issue(s)")
            for i in issues:
                print(f"    ! {i}")
            all_issues.extend(issues)
        else:
            print(f"  OK   {page}")
    print(f"\nChecked: {len(ALL_PAGES)} pairs | Issues: {len(all_issues)}")
    return 1 if all_issues else 0

if __name__ == "__main__":
    sys.exit(main())
```

**Customize for your project:**
- Replace `CARD_PAGES` and `PROSE_PAGES` with your actual page lists
- Replace `EN_NAV_LABELS`, `ZH_NAV_LABELS` with your nav labels
- If no chapters exist, remove those variables
- Add project-specific checks (e.g., image path correctness for subdirectory pages)

**Critical customization:** Every time you switch a page from card format to prose format (or vice versa), move it between `CARD_PAGES` and `PROSE_PAGES` in the checker. Otherwise the checker will report false-positive parity issues.

Also verify:
- All EN nav links: every `<a href="..."` in nav groups must resolve to an existing file
- All ZH nav links: same check within `zh/` subdirectory
- Subdirectory pages (e.g., `zh/chapters/health/`): check that nav paths use correct depth (`../../../zh/index.html` not `../zh/index.html`)

## PHASE 6 — PHASE-EXIT GATES

These gates MUST pass before marking Phase 6 complete. If any fail, fix immediately — do not defer.

### Gate 1: Encoding Check (BLOCKING — CJK content)

Before opening any ZH file in a browser, run:

```powershell
$path = "output/zh"
foreach ($f in (Get-ChildItem -LiteralPath $path -Recurse -Filter *.html)) {
    $text = [System.IO.File]::ReadAllText($f.FullName, [System.Text.UTF8Encoding]::new($false))
    if ($text.Contains([char]0xFFFD)) {
        Write-Error "CORRUPTED (U+FFFD): $($f.FullName)"
    }
    # Also check for degraded UTF-8 em dashes shown as '??'
    $degraded = [regex]::Matches($text, '\?\?')
    if ($degraded.Count -gt 0) {
        Write-Warning "DEGRADED UTF-8: $($f.FullName) has $($degraded.Count) '??' occurrences — likely em dashes written through ANSI pipe"
    }
}
```

**This is a blocking gate.** Zero U+FFFD occurrences are required. Any occurrence means the file is permanently corrupted — patch by regenerating the file, not by trying to repair it byte-by-byte.

**Also scan for `??` replacement characters** (degraded UTF-8 em dashes). Unlike U+FFFD, `??` may appear in English text legitimately (e.g., ternary operators), so treat it as a warning, not a blocker. Investigate each occurrence: if it replaces an em dash `—`, the source template or pipeline has an encoding leak. If found across multiple files, it indicates a systemic encoding issue in the generation pipeline, not a one-off corruption.

### Gate 2: Recovery Protocol (for corrupted files)

If Gate 1 fails (U+FFFD found), use this recovery protocol:

1. **Identify scope**: Which files are corrupted? Check `output/zh/` and `output/zh/chapters/*/` separately.
2. **Check EN originals**: Are the EN files intact? If yes, rebuild ZH from EN.
3. **Rebuild strategy** (choose one):
   - **Rebuild from EN template**: For simple pages, copy the EN HTML structure and translate nav labels, headings, and section text into Chinese. Keep SVGs, data tables, and confidence badges as-is.
   - **Rebuild from original source**: If you have the original ZH content cached in conversation history (e.g., from an earlier `Read` tool use), write it back with the Write tool (NOT PowerShell).
   - **Translate fresh**: For complex pages (final-report, knowledge-base), read the EN version and create a new ZH version with full translation. This is the most reliable approach.
4. **Never use `Set-Content` or `Out-File` in PowerShell.** Use the Write tool (which handles UTF-8 natively), or Python's `open(path, "w", encoding="utf-8")`, or .NET's `[System.IO.File]::WriteAllText()`.
5. **Re-verify**: Re-run Gate 1 after recovery. Check also for structural parity (see parity checker below).

### Gate 3: Render Spot-Check (BLOCKING)

Open at least 3 representative pages in a browser and verify visually:

- [ ] Page loads without rendering errors (check browser console)
- [ ] SVG figures display correctly (check at least one figure per page type)
- [ ] All nav links work (click every link in the nav bar)
- [ ] Language switcher works (EN ↔ ZH round-trip)
- [ ] Confidence badge tooltips appear on hover (CSS `::after` pseudo-element)
- [ ] Confidence framework [?] link navigates to the methodology page anchor
- [ ] ZH pages render Chinese characters correctly (not `�` boxes)
- [ ] Responsive layout: narrow the browser to 400px; no overlapping elements

**When pages ship with broken layout, the entire research report loses credibility.** The parity checker (below) verifies structure but cannot see visual rendering. A 2-minute manual spot-check catches layout bugs the checker never can.

### Gate 4: HTML Structure Validation (NEW — Learned from Practice)

After parity and encoding pass, validate DOM structure for every HTML file:

```python
# div_balance_check.py — run against all generated HTML
import glob, re, sys
issues = []
for fp in glob.glob("output/**/*.html", recursive=True):
    with open(fp, encoding="utf-8") as f:
        c = f.read()
    opens = len(re.findall(r'<div\b', c))
    closes = len(re.findall(r'</div>', c))
    if opens != closes:
        issues.append(f"DIV MISMATCH: {fp} ({opens} opens, {closes} closes)")
    # Title tag check
    title_m = re.search(r'<title>(.*?)</title>', c)
    if not title_m or not title_m.group(1).strip():
        issues.append(f"MISSING TITLE: {fp}")
    # Footer date check (advisory)
    if 'compiled' in fp or 'zh' in fp:
        date_m = re.search(r'(?:compiled|last updated|20\d{2}-\d{2}-\d{2})', c, re.IGNORECASE)
        if not date_m:
            issues.append(f"MISSING DATE: {fp}")
if issues:
    for i in issues:
        print(f"  ! {i}")
    sys.exit(1)
else:
    print("All HTML structure checks passed.")
```

**This is a blocking gate.** A single unmatched `<div>` breaks the entire page layout. The parity checker cannot catch this because it counts elements, not nesting.

### Gate 5: Attribute Inconsistency Check

Run this grep for both EN and ZH directories to catch a common typo:

```powershell
$base = "output"
$files = Get-ChildItem $base -Recurse -Filter *.html
foreach ($f in $files) {
    $text = [System.IO.File]::ReadAllText($f.FullName)
    # CATCH: 'confidence="' without 'data-' prefix
    if ($text -match 'confidence="' -and $text -notmatch 'data-confidence=') {
        Write-Warning "Inconsistent attributes in $($f.FullName): 'confidence"' -match 'confidence="'
    }
    # Report 'confidence="' occurrences even when data- also exists
    $conf = [regex]::Matches($text, 'confidence="').Count
    $dconf = [regex]::Matches($text, 'data-confidence="').Count
    if ($conf -ne $dconf) {
        Write-Warning "MIXED attributes in $($f.FullName): confidence=$conf data-confidence=$dconf"
    }
}
```

Both `confidence` and `data-confidence` on the same element means one will be silently ignored by both CSS and the parity checker. Use `data-confidence` consistently.

## Post-Generation: Cross-Artifact Consistency Check

After adding any new finding, data point, or section to one artifact, verify propagation to all others. Use this mapping template:

**Mapping template for additions:**
```
New item: <brief description>
  → Report chapter(s): [list affected chapters]
  → Executive summary / Synthesis: [yes/no — if significant]
  → Knowledge base: [yes/no — if new entity/relation]
  → Dashboard / Interactive features: [yes/no — if new data or visualization]
  → Bilingual pair: [EN file updated → ZH file updated?]
  → Data file: [if new computed data, path to JSON/CSV]
```

**Run this check before marking any task complete.** If any box is "no" but should be "yes," the artifact is stale — update it before proceeding.

**Experience note (global-heatwave):** Adding §9.0 Predictive Timing to the integrated analysis chapter (task 4.3/4.4) produced a `predictive-thresholds.json` data file (4.2) and updated the report chapter, but the dashboard description page remained unchanged until the user flagged it. A 10-second cross-artifact scan would have caught this.

## Encoding Strategy (for CJK Content on Windows)

Windows PowerShell's `>` and `|` operators encode text using the system code page (Windows-1252 for en-US), NOT UTF-8. This corrupts Chinese characters:

**BAD (causes U+FFFD):**
```powershell
$html | Out-File zh/file.html
$html > zh/file.html
Set-Content zh/file.html $html   # <-- PowerShell 5.1 defaults to ANSI!
```

**GOOD:**
```powershell
[System.IO.File]::WriteAllText("zh/file.html", $html, [System.Text.UTF8Encoding]::new($false))
```

Or write via Python from PowerShell:
```powershell
python -c "open('zh/file.html','w',encoding='utf-8').write(open('/dev/stdin').read())"
```

## SVG Map (for geographic topics)

- Bilingual title (English + Chinese)
- Colored regions, city labels, legend
- Responsive viewBox, defs for gradients/shadows
