#!/usr/bin/env python3
# simulator.py — reads a scenario JSON and writes synthetic JSONL events (one per step)
# Beginner friendly: no external network activity, purely synthetic telemetry.

import json
import sys
import time
from datetime import datetime, timezone
import uuid

# Defaults (you can change these later)
DEFAULT_HOST = "WIN-LAB-01"
DEFAULT_USER = "corp\\alice"
OUTPUT_FILE = "events.jsonl"

def ts_now():
    return datetime.now(timezone.utc).isoformat()

def load_scenario(path):
    # NOTE: use utf-8-sig to handle BOM that PowerShell adds with Out-File -Encoding utf8
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)

def emit_event(out_f, scenario_name, step):
    event = {
        "event_id": str(uuid.uuid4()),
        "ts": ts_now(),
        "scenario": scenario_name,
        "step_id": step.get("id"),
        "event_type": step.get("type"),
        "tactic": step.get("tactic"),
        "technique_id": step.get("technique_id"),
        "host": DEFAULT_HOST,
        "user": DEFAULT_USER,
        "fields": step.get("fields", {})
    }
    out_f.write(json.dumps(event) + "\n")
    out_f.flush()
    print("emitted:", event["event_type"], "step", event["step_id"])

def main():
    if len(sys.argv) < 2:
        print("Usage: python simulator.py <scenario.json> [delay_seconds]")
        sys.exit(1)

    scenario_path = sys.argv[1]
    delay = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

    scenario = load_scenario(scenario_path)
    scenario_name = scenario.get("name", "unnamed-scenario")
    steps = scenario.get("steps", [])

    with open(OUTPUT_FILE, "w", encoding="utf8") as out_f:
        for step in steps:
            emit_event(out_f, scenario_name, step)
            time.sleep(delay)

    print("Done. Events written to", OUTPUT_FILE)

if __name__ == "__main__":
    main()
