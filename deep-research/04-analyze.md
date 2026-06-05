# Phase 4: Apply — Data Analysis

**Purpose:** Analyze collected data to produce evidence for findings.

## Core Principle: Code-First

**Do not state results in text.** Output Python code that computes them. The human runs the code locally; the actual output is the result.

- Good: "Here is a Pandas script to compute the mean and standard deviation from `data.csv`."
- Bad: "The mean is 42.3 and the standard deviation is 5.1."

## Binary Choice for Output

Each analysis step produces exactly **one** of:
- **Python code block** (for statistical computation, data processing, figure generation)
- **JSON data block** (for extracted metrics, structured findings)

Never mix both in the same block.

## Requirements for Every Artifact

1. **Self-contained and reproducible**: load from `analysis/data/`, full pipeline documented, dependencies in `requirements.txt`
2. **Preserved**: notebooks → `analysis/notebooks/`, scripts → `analysis/scripts/`, figures → `analysis/figures/`, data → `analysis/data/`
3. **Parameter choices justified** in comments
4. **Robustness checks** included (sensitivity analysis, alternative specifications)

## Consistency

- Shared config in `analysis/config.yaml`
- Consistent naming, date formats, color palettes
- Utility functions centralized in `analysis/scripts/`

## Validation Run

After generating any script, notebook, or application code, **execute it and confirm zero errors** before marking the analysis complete. If the code produces runtime errors, fix them in the same phase — do not defer to a later phase.

- For Python scripts: run with `python script.py` and check exit code
- For notebooks: execute all cells and confirm no exceptions
- For dashboards/apps: start the server and verify the landing page loads

## Review Manifest

```yaml
# STEP_REVIEW_MANIFEST
summary: "Computed [metric] from [dataset]"
code_output: "script_name.py"
key_figures: ["figure_1.png", "figure_2.png"]
data_gaps:
  - "Any limitations in the data discovered during analysis"
next_action: "Interpret results or run next analysis"
validation: "Script ran without errors"  # or list issues found
```

---

## File Truncation Safeguard (NEW in v2.0)

Notebook outputs and data files may exceed 50KB. After reading any analysis output, check for truncation and read offset segments. Do not draw conclusions from truncated data.

---

## End Conditions (NEW in v2.0)

This phase is **complete** when ALL of the following are true:

1. ✅ All analysis scripts produce zero runtime errors when executed
2. ✅ Scripts are preserved at `analysis/scripts/` or notebooks at `analysis/notebooks/`
3. ✅ Figures saved to `analysis/figures/` with descriptive filenames
4. ✅ Data files saved to `analysis/data/` with provenance notes
5. ✅ Parameter choices and robustness checks documented in comments
6. ✅ Review manifest appended: summary, key figures, data gaps, validation results
7. ✅ task_state.json updated if spanning multiple sessions
