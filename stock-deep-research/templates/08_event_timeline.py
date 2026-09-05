# -*- coding: utf-8 -*-
"""
Template: 08_event_timeline.py — Event Timeline from Findings-Index
Whole-market stock-deep-research skill (v2.0).

Builds documents/event-timeline.md from documents/findings-index.json
(dated events: policy-rate days, earnings season, index recons, press
triggers) and enforces the as-of window: only events dated <= decision
date (ASOF) are admissible justification. Post-cutoff events are listed
but marked ^post-cutoff and excluded from the view (P9).

Usage:  python 08_event_timeline.py  <market>  <asof>
  e.g.   python 08_event_timeline.py  hsi  2026-09-04

Data needed: documents/findings-index.json entries carrying an event-date
field (or documents/events-<asof>.csv with: date, title, type, source_doc).

TODO(tune): date field name in your findings-index; event types
"""
import sys, os, json

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MARKET = sys.argv[1] if len(sys.argv) > 1 else "hsi"
ASOF = sys.argv[2] if len(sys.argv) > 2 else "2026-09-04"
INDEX = os.path.join("documents", "findings-index.json")
CSV = os.path.join("data", f"{MARKET}-events-{ASOF}.csv")
OUT = os.path.join("documents", "event-timeline.md")

EVENT_TYPES = ("policy", "earnings", "index-recon", "press", "market", "other")


def iso(d):
    return str(d)[:10]


def build():
    events = []
    if os.path.exists(INDEX):
        try:
            with open(INDEX, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            if isinstance(data, dict):
                data = data.get("events", [])
            for e in data:
                if e.get("event_date"):
                    events.append({
                        "date": iso(e["event_date"]),
                        "title": e.get("title") or e.get("quote", "")[:80],
                        "type": e.get("event_type", "other"),
                        "source_doc": e.get("source_doc", ""),
                    })
        except Exception as ex:
            print(f"WARN: could not read {INDEX}: {ex}")
    if os.path.exists(CSV):
        import csv
        with open(CSV, "r", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                events.append({
                    "date": iso(row.get("date", "")),
                    "title": row.get("title", ""),
                    "type": row.get("type", "other"),
                    "source_doc": row.get("source_doc", ""),
                })

    events.sort(key=lambda e: (e["date"], e["title"]))
    in_window = [e for e in events if not e["date"] or e["date"] <= ASOF]
    post_cutoff = [e for e in events if e["date"] and e["date"] > ASOF]

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(f"# Event Timeline — {MARKET} (as-of {ASOF})\n\n")
        fh.write(f"In-window events (admissible justification): {len(in_window)}  |  "
                 f"post-cutoff (excluded, marked): {len(post_cutoff)}\n\n")
        fh.write("| date | type | title | source_doc |\n|---|---|---|---|\n")
        for e in in_window:
            fh.write(f"| {e['date']} | {e['type']} | {e['title']} | {e['source_doc']} |\n")
        fh.write("\n## Post-cutoff events (excluded — never justify the view, P9)\n\n")
        for e in post_cutoff:
            fh.write(f"- {e['date']} ^post-cutoff — {e['title']} ({e['type']}, {e['source_doc']})\n")
        fh.write("\n> Rule: only in-window events (<= as-of) are admissible. "
                 "Post-cutoff events are listed for transparency only.\n")

    print(f"Wrote {OUT}: {len(in_window)} in-window, {len(post_cutoff)} post-cutoff events.")


if __name__ == "__main__":
    build()