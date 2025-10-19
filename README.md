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
