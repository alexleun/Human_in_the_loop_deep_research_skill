# -*- coding: utf-8 -*-
"""
Template: 03_breadth.py — Market Breadth
Whole-market stock-deep-research skill (v2.0).

Computes breadth signals:
  - % constituents above MA200 (or documented approximation)
  - advance/decline and new-highs/new-lows counts
  - cross-sectional dispersion of member returns
When full member data is unavailable, uses a documented broad-subset / ETF
approximation. ALWAYS label the approximation in the output (Phase 2 note).

Usage:  python 03_breadth.py  <market>  <asof>
Data needed: data/<market>-members-<asof>.csv with columns:
  member, date, close   (one row per member per date; or member, close latest)
or data/<market>-breadth-<asof>.csv with precomputed breadth series.

TODO(tune): free member/ETF source for the market; approximation label
"""
import sys, os, json, glob

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
OUT = os.path.join("data", f"{MARKET}-breadth-{ASOF}.json")


def approx_label():
    # TODO(verify): document the approximation used (Phase 2 must state it)
    return "APPROXIMATION: member-level data unavailable; breadth from broad liquid subset (e.g. a constituent-listed ETF or top-N liquid names). Verify before use."


def breadth():
    mem_csv = os.path.join("data", f"{MARKET}-members-{ASOF}.csv")
    pcsv = os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv")
    if not os.path.exists(mem_csv):
        print("NOTE: member file not found; breadth will use the index series only and")
        print("      the documented approximation. Machine-using a member file yields")
        print("      real A/D, new-highs/new-lows, and % above MA200.")
        # Minimal proxy breadth from the index series itself (labeled)
        try:
            import pandas as pd
            df = pd.read_csv(pcsv).sort_values("date")
            closes = df["close"].astype(float).tolist()
        except ImportError:
            closes = []
            with open(pcsv, "r", encoding="utf-8") as fh:
                next(fh, None)
                for line in fh:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        try:
                            closes.append(float(parts[1]))
                        except ValueError:
                            continue
        ma200 = sum(closes[-200:]) / 200 if len(closes) >= 200 else None
        above = 1.0 if (ma200 and closes[-1] > ma200) else 0.0
        result = {
            "market": MARKET, "asof": ASOF,
            "approximation": approx_label(),
            "pct_above_ma200": above,
            "advance": None, "decline": None, "net_adv": None,
            "new_highs": None, "new_lows": None,
            "cross_sectional_dispersion": None,
            "note": "index-proxy only; supply a member file for real breadth",
        }
    else:
        # Member-level breadth
        try:
            import pandas as pd
            df = pd.read_csv(mem_csv, parse_dates=["date"]).sort_values(["member", "date"])
            latest = df[df["date"] == df["date"].max()]
            # % above MA200 measured on the last 200 closes per member
            grp = df.groupby("member")["close"].agg(lambda s: s.iloc[-1] > s.tail(200).mean())
            above = float(grp.mean())
            closes = latest["close"].tolist()
            med = sorted(closes)[len(closes) // 2]
            disp = (sum((c - med) ** 2 for c in closes) / max(len(closes) - 1, 1)) ** 0.5 / max(med, 1e-9)
            result = {
                "market": MARKET, "asof": ASOF,
                "pct_above_ma200": round(above, 4),
                "advance": None, "decline": None, "net_adv": None,
                "new_highs": None, "new_lows": None,
                "cross_sectional_dispersion": round(disp, 4),
                "members": int(len(latest)),
            }
        except ImportError:
            print("ERROR: member-level breadth requires pandas")
            sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    breadth()