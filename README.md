## Purple Team Scenario Simulator (synthetic only)
@'
---

### 🧠 Overview
This project simulates purple-team scenarios by generating **synthetic telemetry**—safe, realistic-looking events that mimic adversary behaviors without performing any actual attacks.  
It’s designed for SOC analysts, students, and engineers who want to test detection rules, SIEM pipelines, and dashboards in a controlled environment.

---

### ⚙️ How It Works
1. Each scenario (`.json`) defines a sequence of steps (e.g., ProcessCreate, NetworkConnect, FileWrite).  
2. The simulator reads the scenario and writes JSONL events (`events_<scenario>.jsonl`).  
3. These files can be ingested into SIEMs, used to trigger alert logic, or replayed through your ThreatLog Automator tool.

---

### 🚀 Usage
```powershell
# Run the simulator
python .\simulator.py .\scenarios\credential_probe.json 0.5

# Summarize the results
python .\summarize.py

📁 Example Output
{
  "event_id": "uuid",
  "ts": "2025-10-19T15:11:56Z",
  "scenario": "Credential Probe (synthetic)",
  "event_type": "ProcessCreate",
  "tactic": "Execution",
  "technique_id": "T1059",
  "host": "WIN-LAB-01",
  "user": "corp\\alice"
}
