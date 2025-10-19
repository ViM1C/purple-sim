#!/usr/bin/env python3
# summarize.py — simple summary of events.jsonl
# Prints counts per event_type and the first/last timestamp seen.

import json
from collections import Counter
from datetime import datetime

F = "events.jsonl"

def load_events(path):
    with open(path, "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)

def main():
    types = Counter()
    first_ts = None
    last_ts = None
    total = 0
    for ev in load_events(F):
        total += 1
        et = ev.get("event_type","<unknown>")
        types[et] += 1
        ts = ev.get("ts")
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z","+00:00"))
                if first_ts is None or dt < first_ts:
                    first_ts = dt
                if last_ts is None or dt > last_ts:
                    last_ts = dt
            except Exception:
                pass

    print(f"Total events: {total}")
    print("Events by type:")
    for k,v in types.most_common():
        print(f"  {k}: {v}")
    if first_ts and last_ts:
        print("Time range:", first_ts.isoformat(), "→", last_ts.isoformat())

if __name__ == '__main__':
    main()
