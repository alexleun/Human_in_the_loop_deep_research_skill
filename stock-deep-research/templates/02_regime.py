# -*- coding: utf-8 -*-
"""
Template: 02_regime.py — Market Regime Classification
Whole-market stock-deep-research skill (v2.0).

Classifies the market regime from the index price series:
  - Trend: index vs MA200, MA20/50/200 structure
  - Momentum: 12M-1M momentum, RSI(14), 12M rate of change
  - Volatility state: 60d realized vol percentile (high / normal / low)
Output: composite label — Bull / Neutral / Bear / Volatile-with-trend

Usage:  python 02_regime.py  <market>  <asof>
Data needed: data/<market>-price-history-<asof>.csv  (date, close)

TODO(tune): RSI window, vol percentile history depth, label thresholds
"""
import sys, os, json

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
CSV = os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv")
OUT = os.path.join("data", f"{MARKET}-regime-{ASOF}.json")


def sma(values, window):
    if len(values) < window:
        return None
    return sum(values[-window:]) / window


def rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    gains, losses = [], []
    for i in range(len(prices) - period, len(prices)):
        d = prices[i] - prices[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    ag = sum(gains) / period
    al = sum(losses) / period
    if al == 0:
        return 100.0
    rs = ag / al
    return 100.0 - (100.0 / (1.0 + rs))


def regime():
    try:
        import pandas as pd
        df = pd.read_csv(CSV).sort_values("date")
        prices = df["close"].astype(float).tolist()
    except ImportError:
        prices = []
        with open(CSV, "r", encoding="utf-8") as fh:
            next(fh, None)
            for line in fh:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    try:
                        prices.append(float(parts[1]))
                    except ValueError:
                        continue
    if len(prices) < 250:
        print(f"ERROR: need >=250 closes in {CSV}, got {len(prices)}")
        sys.exit(1)

    last = prices[-1]
    ma20, ma50, ma200 = sma(prices, 20), sma(prices, 50), sma(prices, 200)
    rsi14 = rsi(prices)
    mom = (prices[-1] / prices[-253] - 1.0) if len(prices) > 253 else (prices[-1] / prices[0] - 1.0)

    # Sanity gate
    if not (ma20 and ma50 and ma200 and rsi14 is not None):
        print("ERROR: insufficient history for regime classification")
        sys.exit(1)

    trend_up = last > ma200
    ma_bull = ma20 > ma50 > ma200
    ma_bear = ma20 < ma50 < ma200
    mom_ok = mom > 0.0
    rsi_ok = 50.0 <= rsi14 <= 70.0  # healthy momentum zone

    # Composite label
    if trend_up and ma_bull and mom_ok:
        label = "Bull"
    elif not trend_up and ma_bear:
        label = "Bear"
    elif ma_bull and not mom_ok:
        label = "Neutral"
    else:
        label = "Sideways"
    # TODO: add "Volatile-with-trend" when vol percentile is high but trend is intact

    result = {
        "market": MARKET, "asof": ASOF,
        "close": last,
        "ma20": round(ma20, 2), "ma50": round(ma50, 2), "ma200": round(ma200, 2),
        "above_ma200": trend_up,
        "rsi14": round(rsi14, 1),
        "momentum_12m_1m": round(mom, 4),
        "regime": label,
        "trend": "up" if trend_up else "down",
        "ma_structure": "bull" if ma_bull else ("bear" if ma_bear else "mixed"),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    print(f"Saved -> {OUT}")


if __name__ == "__main__":
    regime()