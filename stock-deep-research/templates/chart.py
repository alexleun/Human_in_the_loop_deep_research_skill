# -*- coding: utf-8 -*-
"""
Template: chart.py — Standard Index Price + MA + Volume Chart
Whole-market stock-deep-research skill (v2.0).

Produces the standard index chart: price + MA20/MA50/MA200 + volume,
persisted to report/charts/<market>-price-<asof>.png.
On Windows, verify CJK fonts before rendering if CJK labels are used.

Usage:  python chart.py  <market>  <asof>
Data needed: data/<market>-price-history-<asof>.csv  (date, open, high, low, close, volume)

TODO(tune): chart style, volume axis, annotations (drawdown, regime bands)
"""
import sys, os

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
CSV = os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv")
OUTDIR = os.path.join("report", "charts")
PNG = os.path.join(OUTDIR, f"{MARKET}-price-{ASOF}.png")


def check_cjk_fonts():
    """Verify CJK font availability before rendering (deep-research pattern)."""
    try:
        import matplotlib.font_manager as fm
        cjk = [f.name for f in fm.fontManager.ttflist
               if any(k in f.name.lower() for k in
                      ["microsoft", "noto", "simsun", "simhei", "yahei", "jhenghei", "ming", "cjk", "kai", "fang"])]
        if not cjk:
            print("WARNING: No CJK fonts found — text may render as boxes.")
        else:
            import matplotlib.pyplot as plt
            plt.rcParams["font.family"] = [cjk[0], "sans-serif"]
        return cjk[:5]
    except ImportError:
        return None


def chart():
    try:
        import pandas as pd
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError as ex:
        print(f"ERROR: charting needs pandas + matplotlib: {ex}")
        print("Phase 1 env probe result should have decided this fallback already.")
        sys.exit(1)

    if not os.path.exists(CSV):
        print(f"ERROR: {CSV} not found.")
        sys.exit(1)

    check_cjk_fonts()
    df = pd.read_csv(CSV).sort_values("date")
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma50"] = df["close"].rolling(50).mean()
    df["ma200"] = df["close"].rolling(200).mean()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True,
                                   gridspec_kw={"height_ratios": [3, 1]})
    ax1.plot(df["date"], df["close"], label=f"{MARKET.upper()} close", color="#0b5394", lw=1.6)
    ax1.plot(df["date"], df["ma20"], label="MA20", color="#e69138", lw=1.0, alpha=0.9)
    ax1.plot(df["date"], df["ma50"], label="MA50", color="#6aa84f", lw=1.0, alpha=0.9)
    ax1.plot(df["date"], df["ma200"], label="MA200", color="#990000", lw=1.1, alpha=0.9)
    ax1.set_ylabel("Index level")
    ax1.set_title(f"{MARKET.upper()} — price + MA20/50/200 (as-of {ASOF})")
    ax1.legend(loc="best")
    ax1.grid(alpha=0.3)

    ax2.bar(df["date"], df.get("volume", 0), color="#b7b7b7", width=1.0)
    ax2.set_ylabel("Volume")
    ax2.grid(alpha=0.3)

    os.makedirs(OUTDIR, exist_ok=True)
    fig.tight_layout()
    fig.savefig(PNG, dpi=150)
    plt.close(fig)
    print(f"Saved chart -> {PNG}")

    # Sanity: confirm the file exists and is non-empty
    if os.path.getsize(PNG) == 0:
        print("ERROR: chart file is empty.")
        sys.exit(1)


if __name__ == "__main__":
    chart()