# Phase 8: Report — Deliver the Detailed Analysis

**Who drives:** LLM (writes) + Human (reviews/approves)

**Purpose:** Produce the final, detailed report with an Executive Summary and a clear recommendation, built entirely from source-grounded data.

## Required Report Structure

```
# <Company Name> (<Code>.<Exchange>) — Stock Analysis Report
As-of date: YYYY-MM-DD   |   Report currency: HKD   |   Horizon: <selected>

## 1. Executive Summary
   - Rating: BUY / HOLD / SELL  +  Price target (HKD)  +  Upside/downside %
   - Confidence: high/medium/low
   - Thesis in 2–4 sentences
   - Key risks / falsification criterion (1–2 lines)

## 2. Company Overview
   Business, segments, products, moat, management, governance

## 3. Financial & Fundamental Analysis
   Growth, profitability, financial health (tables + commentary)

## 4. Valuation & Price Target
   Methods, assumptions, fair-value range, scenario table, target

## 5. Technical Analysis
   Trend, momentum, support/resistance, volume, data-range note

## 6. Catalysts
   List with timing/materiality

## 7. Risks & Scenario Analysis
   Likelihood × impact; falsification criteria

## 8. Peer Comparison
   Table of key ratios vs peers

## 9. Recommendation
   Clear BUY/HOLD/SELL, target, horizon, confidence, what would change it

## 10. Methodology & Sources
   Sources used (with URLs + local copies), limitations, data coverage/gaps

## 11. Disclaimer
   Research only, not personalized investment advice
```

## Writing Rules
- **Executive Summary first**, supporting detail after.
- Every quantitative claim carries a **source citation** (URL or source ID). No unsourced numbers.
- Use tables for comparative data; keep prose decision-focused.
- **Discovery-first** framing: open sections with claims about the company, not with "we searched X sources."
- Mark every "as of" date; never present historical data as current.
- Keep confidence language consistent with Phase 7.
- Output as markdown file: `report/<Code>-<Company>-analysis.md`.

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Report file written at the defined path with all 11 sections
2. ✅ Executive summary carries the rating, target, confidence, and thesis
3. ✅ Every number has a source citation
4. ✅ Methodology & sources section lists URLs + local copies + limitations
5. ✅ Disclaimer present
6. ✅ Human has reviewed and approved the report
