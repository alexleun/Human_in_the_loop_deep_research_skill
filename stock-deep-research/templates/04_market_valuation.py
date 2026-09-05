# -*- coding: utf-8 -*-
"""
Template: 04_market_valuation.py — Index Valuation Percentiles
Whole-market stock-deep-research skill (v2.0).

Computes the market's valuation POSITION (percentiles, not levels):
  - Index P/E and P/B percentile rank vs the market's own history
  - Dividend-yield support band (yield quintile historically at market bottoms)
  - Earnings-yield minus bond-yield spread (ERP proxy) + percentile
Purely computational: it never transcribes an aggregator's "current P/E" —
it recomputes from the collected P/E, P/B, yield series.

Usage:  python 04_market_valuation.py  <market>  <asof>
Data needed: data/<market>-valuation-<asof>.csv  with columns:
  date, pe, pb, div_yield, earnings_yield, bond_yield  (bond_yield optional)

TODO(tune): lookback window, source of the historical series, bond-yield source
"""
import sys, os, json

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
CSV = os.path.join("data", f"{MARKET}-valuation-{ASOF}.csv")
OUT = os.path.join("data", f"{MARKET}-valuation-percentile-{ASOF}.json")
LOOKBACK = 10 * 252  # TODO(tune): ~10 years of daily/trading observations


def pct_rank(target, series):
    filtered = [v for v in series if v is not None and v == v]
    if not filtered:
        return None
    below = sum(1 for v in filtered if v <= target)
    return round(below / len(filtered) * 100.0, 1)


def valuation():
    import pandas as pd
    if not os.path.exists(CSV):
        print(f"ERROR: {CSV} not found. Reconstruct the historical P/E, P/B, yield series")
        print("      from free aggregators/HKEX EOD data (Phase 2) with the same date axis.")
        sys.exit(1)
    df = pd.read_csv(CSV).sort_values("date")
    df = df.tail(LOOKBACK)
    last = df.iloc[-1]
    hist_pe = df["pe"].astype(float).tolist()
    hist_pb = df["pb"].astype(float).tolist()
    hist_dy = df["div_yield"].astype(float).tolist()

    pe, pb, dy = float(last["pe"]), float(last["pb"]), float(last["div_yield"])

    # Sanity gates (units/currency)
    if not (5 <= pe <= 100):
        print(f"WARN: sanity gate — P/E {pe} outside plausible index band [5, 100]; fix source series.")
    if not (0.3 <= pb <= 20):
        print(f"WARN: sanity gate — P/B {pb} outside plausible index band [0.3, 20]; fix source series.")
    if not (0 <= dy <= 0.15):
        print(f"WARN: sanity gate — dividend yield {dy} outside plausible band [0, 0.15]; fix source series.")

    result = {
        "market": MARKET, "asof": ASOF,
        "pe": pe, "pe_percentile_10y": pct_rank(pe, hist_pe),
        "pb": pb, "pb_percentile_10y": pct_rank(pb, hist_pb),
        "div_yield": dy,
        "dy_support_band": {
            "p90_yield_quintile": None,  # TODO: yield level at 90th percentile (historically 'market bottom' zone)
            "p95_yield_quintile": None,
            "note": "yield support band = yield quintiles from the historical series"
        },
        "erp_spread": None,  # TODO: earnings_yield - bond_yield from valuation CSV
        "erp_percentile": None,
    }
    if "earnings_yield" in df.columns and "bond_yield" in df.columns:
        ey = float(last["earnings_yield"])
        by = float(last["bond_yield"])
        result["erp_spread"] = round(ey - by, 4)
        result["erp_percentile"] = pct_rank(ey - by, (df["earnings_yield"] - df["bond_yield"]).astype(float).tolist())

    print(json.dumps(result, indent=2, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    valuation()