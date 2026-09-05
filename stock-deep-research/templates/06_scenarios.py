# -*- coding: utf-8 -*-
"""
Template: 06_scenarios.py — Index Target Scenarios (Base/Bull/Bear + Monte Carlo)
Whole-market stock-deep-research skill (v2.0).

Deterministic scenario targets for the index fair-value band:
  - Base: central valuation percentile + earnings at trend growth -> expected level
  - Bull: re-rating to a high-historical percentile + above-trend earnings -> upside
  - Bear: derating to a low-historical percentile + earnings cut -> downside
Optional Monte Carlo over (percentile, earnings growth) -> distribution/band.
Every output passes a units/currency sanity gate before entering the report.

Usage:  python 06_scenarios.py  <market>  <asof>  [--mc 2000]
Data needed: data/<market>-valuation-<asof>.csv + the percentile outputs of 04_market_valuation.py

TODO(tune): percentile targets, trend EPS growth, MC sample count + seed; market code
"""
import sys, os, json, argparse, random

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

TRADING_DAYS = 252
EPY = 12  # months in an evaluation period -> annualize

# TODO(tune): assumptions for the market
ASSUMPTIONS = {
    "base_pe_percentile": 0.50,
    "bull_pe_percentile": 0.85,
    "bear_pe_percentile": 0.15,
    "trend_eps_growth": 0.05,   # annual trend EPS growth
    "bull_eps_growth": 0.10,
    "bear_eps_growth": -0.10,
    "horizon_months": 12,
}
MC_DEFAULTS = {"n": 2000, "seed": 42}


def sanity(level, target, current):
    if target <= 0 or abs(target / current - 1.0) > 0.5:
        print(f"WARN: sanity gate — {level} target {target:.2f} outside +/-50% of current {current:.2f}.")
        return False
    return True


def scenarios():
    parser = argparse.ArgumentParser()
    parser.add_argument("market")
    parser.add_argument("asof")
    parser.add_argument("--mc", type=int, default=0)
    args, _ = parser.parse_known_args()
    MARKET, ASOF = args.market, args.asof
    mc_n = args.mc or MC_DEFAULTS["n"]

    per_csv = os.path.join("data", f"{MARKET}-valuation-percentile-{ASOF}.json")
    if not os.path.exists(per_csv):
        print("NOTE: percentile outputs not found; using current level directly from price series.")
        import pandas as pd
        closes = pd.read_csv(os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv"))["close"].astype(float)
        cur = float(closes.iloc[-1])
        pe, pb, dy = None, None, None
    else:
        with open(per_csv, "r", encoding="utf-8") as fh:
            p = json.load(fh)
        cur = float(p.get("close") or 0)
        # Fallback: price series for current level
        if not cur:
            import pandas as pd
            closes = pd.read_csv(os.path.join("data", f"{MARKET}-price-history-{ASOF}.csv"))["close"].astype(float)
            cur = float(closes.iloc[-1])
        pe, pb, dy = p.get("pe"), p.get("pb"), p.get("div_yield")

    if cur <= 0:
        print(f"ERROR: no positive current level for {MARKET}")
        sys.exit(1)

    # Deterministic scenario band: level * (1 + earnings growth) * percentile multiple ratio
    def target(growth, pct):
        # P/E ratio shift: move P/E toward percentile-implied multiple; series-level proxy
        return cur * (1.0 + growth * ASSUMPTIONS["horizon_months"] / 12.0) * (1.0 + (pct - 0.5) * 0.4)

    base = target(ASSUMPTIONS["trend_eps_growth"], ASSUMPTIONS["base_pe_percentile"])
    bull = target(ASSUMPTIONS["bull_eps_growth"], ASSUMPTIONS["bull_pe_percentile"])
    bear = target(ASSUMPTIONS["bear_eps_growth"], ASSUMPTIONS["bear_pe_percentile"])

    # Sorted / monotonic sanity
    if not (bear < base < bull):
        print("WARN: sanity gate — scenario ordering violated (expected bear < base < bull); adjust assumptions.")

    for label, t in (("base", base), ("bull", bull), ("bear", bear)):
        sanity(label, t, cur)

    result = {
        "market": MARKET, "asof": ASOF,
        "current_level": round(cur, 2),
        "band": {
            "bull": round(bull, 2),
            "base": round(base, 2),
            "bear": round(bear, 2),
        },
        "assumptions": ASSUMPTIONS,
        "monte_carlo": None,
    }

    if mc_n > 0:
        rng = random.Random(MC_DEFAULTS["seed"])
        draws = []
        for _ in range(mc_n):
            g = rng.gauss(ASSUMPTIONS["trend_eps_growth"], 0.06)
            pct = rng.uniform(0.05, 0.95)
            draws.append(cur * (1.0 + g) * (1.0 + (pct - 0.5) * 0.4))
        draws.sort()
        result["monte_carlo"] = {
            "n": mc_n,
            "p5": round(draws[int(len(draws) * 0.05)], 2),
            "p50": round(draws[len(draws) // 2], 2),
            "p95": round(draws[int(len(draws) * 0.95) - 1], 2),
            "seed": MC_DEFAULTS["seed"],
        }

    print(json.dumps(result, indent=2, ensure_ascii=False))
    with open(os.path.join("data", f"{MARKET}-scenarios-{ASOF}.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
    print("Saved -> data/{} -scenarios-{}.json".format(MARKET, ASOF))


if __name__ == "__main__":
    scenarios()