# Phase 3: Fundamentals — Quality, Growth, Profitability, Balance Sheet

**Who drives:** LLM (computation on collected data)

**Purpose:** Assess the company's **quality and growth** — the core of "what is this business worth, and how risky is it?"

**Code-first discipline:** For any computation (growth rates, margins, ratios), **write and run Python** from the collected figures — do not compute from memory. Use `sys.stdout.reconfigure(encoding='utf-8')` on Windows for safety.

## Dimensions

### 1. Business Quality & Moat
- Business model: how does it make money? Per segment.
- Competitive advantage / moat: brand, scale, network effects, switching costs, IP, cost advantage, regulatory barriers.
- Management & governance: reputation, track record, alignment (insider ownership, buybacks), related-party risk.
- Earnings **quality**: is profit backed by cash flow? Any aggressive accounting, one-off gains/losses, capex intensity?

### 2. Growth
- Revenue growth (YoY, trend over ≥3 years).
- Profit / EPS growth (YoY, trend).
- Growth **sustainability**: organic vs one-off; market expansion, new products, TAM.
- Segment growth breakdown if available.
- Compute CAGR for revenue and EPS.

### 3. Profitability
- Gross margin, operating margin, net margin (trend over ≥3 years).
- ROE, ROIC/ROCE (trend).
- Compare margins/returns to peers.

### 4. Balance Sheet & Financial Health
- Net cash / net debt; gearing (D/E).
- Liquidity: current ratio, quick ratio.
- Operating cash flow vs net income (quality check).
- Free cash flow + FCF yield.
- Dividend policy & payout ratio (coverability).
- Capex intensity and any signs of balance-sheet stress.

## Output

Produce a **fundamentals summary table** with the source ID for each number, plus a short prose assessment: is this a quality, growing, financially sound business? What are the top 2–3 fundamental risks?

## End Conditions

This phase is **complete** when ALL of the following are true:

1. ✅ Growth, profitability, and financial-health metrics computed by script (not memory)
2. ✅ Every number has a source ID and as-of date
3. ✅ Quality & moat assessed against a defined competition set
4. ✅ A one-paragraph fundamental verdict (bull/bear/neutral) is written
5. ✅ Top fundamental risks are listed
