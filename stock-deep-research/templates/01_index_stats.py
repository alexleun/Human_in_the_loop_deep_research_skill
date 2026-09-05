# -*- coding: utf-8 -*-
"""
Template: 01_index_stats.py — Index Statistics
Whole-market stock-deep-research skill (v2.0).

Computes core index statistics from the daily price series:
  - period returns (1M / 3M / 12M / YTD)
  - drawdown profile (current, max, longest, avg)
  - rolling 20d and 60d realized volatility (annualized)
  - rolling 60d Sharpe (vs 0% risk-free proxy; adjust RFR per market)

Usage:  python 01_index_stats.py  <market>  <asof>
  e.g.   python 01_index_stats.py  hsi  2026-09-04

Data needed: data/<market>-price-history-<asof>.csv  with columns:
  date, close  (and optionally open, high, low, volume)

TODO(tune): market code, RFR, lookbacks, output path (data/<market>-index-stats-<asof>.json)
"""
import sys, os, json

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
RFR = 0.00  # TODO(tune): 1-year govt yield as risk-free proxy for the market
TRADING_DAYS = 252
CSV = os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv")
OUT = os.path.join("data", f"{MARKET}-index-stats-{ASOF}.json")


def load_series():
    try:
        import pandas as pd
    except ImportError:
        # Pure-python fallback when pandas is unavailable (env probe, Phase 1)
        print("WARN: pandas not found; using pure-python path.")
        closes = []
        with open(CSV, "r", encoding="utf-8") as fh:
            next(fh, None)
            for line in fh:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    try:
                        closes.append(float(parts[1]))
                    except ValueError:
                        continue
        return closes, None
    df = pd.read_csv(CSV)
    df = df.sort_values("date")
    return df["close"].astype(float).tolist(), df


def annualized_vol(prices, window):
    n = len(prices)
    if n <= window + 1:
        return None
    rets = [prices[i] / prices[i - 1] - 1.0 for i in range(1, n)]
    vols = []
    for i in range(len(rets) - window + 1):
        chunk = rets[i:i + window]
        mean = sum(chunk) / len(chunk)
        var = sum((r - mean) ** 2 for r in chunk) / max(len(chunk) - 1, 1)
        vols.append((var ** 0.5) * (TRADING_DAYS ** 0.5))
    return vols


def stats():
    prices, _ = load_series()
    if len(prices) < 30:
        print(f"ERROR: insufficient data in {CSV}")
        sys.exit(1)

    last = prices[-1]
    latest = dict(close=last, asof=ASOF)

    def ret(n):
        return last / prices[-1 - n] - 1.0 if len(prices) > n and prices[-1 - n] > 0 else None

    latest["ret_1m"] = ret(21)
    latest["ret_3m"] = ret(63)
    latest["ret_12m"] = ret(252)
    latest["ret_ytd"] = None  # TODO: compute from Jan-1 anchor if series spans the year

    # Drawdown profile
    peak = prices[0]
    max_dd, cur_dd = 0.0, 0.0
    dd_len, max_dd_len = 0, 0
    for p in prices:
        peak = max(peak, p)
        dd = p / peak - 1.0
        max_dd = min(max_dd, dd)
        if dd < 0:
            dd_len += 1
            max_dd_len = max(max_dd_len, dd_len)
        else:
            dd_len = 0
    cur_dd = last / max(prices) - 1.0 if prices else 0.0
    latest["drawdown_current"] = round(cur_dd, 4)
    latest["drawdown_max"] = round(max_dd, 4)
    latest["drawdown_max_depth_days"] = max_dd_len

    v20 = annualized_vol(prices, 20)
    v60 = annualized_vol(prices, 60)
    latest["vol_20d"] = round(v20[-1], 4) if v20 else None
    latest["vol_60d"] = round(v60[-1], 4) if v60 else None
    latest["vol_60d_percentile"] = None  # TODO: percentile of current vs historical vol

    # Rolling 60d Sharpe
    if v60 and len(v60) > 60:
        rets = [prices[i] / prices[i - 1] - 1.0 for i in range(1, len(prices))]
        w = 60
        sharpe_step = []
        for end in range(w, len(rets) + 1):
            chunk = rets[end - w:end]
            mu = sum(chunk) / len(chunk)
            sig = (sum((r - mu) ** 2 for r in chunk) / (len(chunk) - 1)) ** 0.5
            sharpe_step.append((mu - RFR / TRADING_DAYS) / sig if sig > 0 else 0.0)
        latest["sharpe_60d"] = round(sharpe_step[-1] * (TRADING_DAYS ** 0.5), 3)

    # Sanity gate
    for k, v in latest.items():
        if isinstance(v, float) and (v < -2 or v > 5) and k.startswith("ret_") is False:
            pass
    for k in ("ret_1m", "ret_3m", "ret_12m"):
        if latest[k] is not None and (latest[k] < -0.9 or latest[k] > 2.0):
            print(f"WARN: sanity gate — {k} outside plausible range: {latest[k]}")

    print(json.dumps({"market": MARKET, "asof": ASOF, **latest}, indent=2, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"market": MARKET, "asof": ASOF, **latest}, fh, indent=2, ensure_ascii=False)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    stats()