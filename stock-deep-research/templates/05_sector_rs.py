# -*- coding: utf-8 -*-
"""
Template: 05_sector_rs.py — Sector Relative Strength & Concentration
Whole-market stock-deep-research skill (v2.0).

Computes for the market's sectors:
  - 3M/12M relative strength (sector index return minus market return)
  - valuation dispersion across sectors (P/E spread)
  - top-10 constituent concentration (optional, from members file)
Feeds the sector tilts (Phase 8) and the crowding check in the fragility audit.

Usage:  python 05_sector_rs.py  <market>  <asof>
Data needed: data/<market>-sectors-<asof>.csv  with columns:
  sector, date, close    (one row per sector per date)
or:  sector, close_latest, pe, pb  (single-row snapshot per sector)

TODO(tune): sector universe/source for the market; top-10 source
"""
import sys, os, json

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
CSV = os.path.join("data", f"{MARKET}-sectors-{ASOF}.csv")
OUT = os.path.join("data", f"{MARKET}-sector-rs-{ASOF}.json")


def sector_rs():
    import pandas as pd
    if not os.path.exists(CSV):
        print(f"ERROR: {CSV} not found. Provide sector index series or a snapshot (Phase 2).")
        sys.exit(1)
    df = pd.read_csv(CSV)
    if "date" in df.columns:
        df = df.sort_values(["sector", "date"])
        rows = []
        for sec, g in df.groupby("sector"):
            closes = g["close"].astype(float).tolist()
            if len(closes) > 63:
                ago3 = closes[-1] / closes[-64] - 1.0
            else:
                ago3 = None
            if len(closes) > 252:
                ago12 = closes[-1] / closes[-253] - 1.0
            else:
                ago12 = None
            rows.append({"sector": sec, "ret_3m": ago3, "ret_12m": ago12,
                         "pe": None, "pb": None})
        table = pd.DataFrame(rows)
    else:
        table = df.copy()

    mkt_ret = None
    mkt_csv = os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv")
    if os.path.exists(mkt_csv):
        try:
            closes = pd.read_csv(mkt_csv)["close"].astype(float).tolist()
            mkt_ret = closes[-1] / closes[-64] - 1.0 if len(closes) > 63 else None
        except Exception:
            pass

    rel = []
    for _, r in table.iterrows():
        rel.append({
            "sector": r["sector"],
            "ret_3m": round(float(r["ret_3m"]), 4) if pd.notna(r.get("ret_3m")) else None,
        })
    pcts = [r["pe"] for r in rel if r.get("pe") is not None]
    dispersion = round(max(pcts) - min(pcts), 2) if len(pcts) >= 2 else None

    result = {
        "market": MARKET, "asof": ASOF,
        "market_ret_3m": round(mkt_ret, 4) if mkt_ret is not None else None,
        "sectors": rel,
        "pe_dispersion": dispersion,
        "top10_concentration": None,  # TODO: % of index market cap in top-10 (from members/weights file)
        "note": "relative strength = sector return vs market return at 3M/12M (compute in Phase 8 tilts)",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    sector_rs()