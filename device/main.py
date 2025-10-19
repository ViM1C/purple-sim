# PurpleSim Telemetry – LilyGo T-Dongle (ESP32-S3)
# Prints three ATT&CK-style synthetic events to serial.
import time, json, sys
from secrets import WIFI_SSID, WIFI_PSK, COLLECTOR_URL, SHARED_KEY, DEVICE_ID
from net import connect_wifi, sync_time
from emitter import TelemetryEmitter

def scenario_credential_probe(em):
    em.emit(scenario="Credential Probe (synthetic)",
            event_type="ProcessCreate", tactic="Execution",
            technique_id="T1059", step_id=1,
            fields={
                "process_name": "powershell.exe",
                "command_line": "powershell -NoProfile -EncodedCommand <synthetic>"
            })
    em.emit(scenario="Credential Probe (synthetic)",
            event_type="NetworkConnect", tactic="Command and Control",
            technique_id="T1071", step_id=2,
            fields={
                "domain": "malicious-sim.test",
                "dst_port": 443,
                "dst_ip": "10.0.99.5"
            })
    em.emit(scenario="Credential Probe (synthetic)",
            event_type="FileWrite", tactic="Credential Access",
            technique_id="T1003", step_id=3,
            fields={
                "path": r"C:\\Users\\alice\\AppData\\Local\\Temp\\dump.dat",
                "size_bytes": 20480
            })

def run():
    print("MPY: soft reboot")
    print("----------------------  PurpleSim Telemetry Test  ----------------------")
    print("Scenario: Credential Probe (synthetic)")
    print("-" * 74)

    em = TelemetryEmitter(DEVICE_ID, COLLECTOR_URL, SHARED_KEY)
    scenario_credential_probe(em)

    for idx, evt in enumerate(em.queue, 1):
        print(f"Event {idx}/{len(em.queue)}")
        print(json.dumps(evt, indent=2))
        print("-" * 74)

run()
