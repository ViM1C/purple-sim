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

4. ---

## 🔧 Device Mode (ESP32-S3 — LilyGo T-Dongle)

PurpleSim now runs on hardware too.  
The MicroPython-based **device mode** turns a LilyGo T-Dongle (ESP32-S3) into a tiny standalone telemetry generator that mirrors the desktop simulator’s output.

- **Firmware:** MicroPython  
- **Files:** [`device/`](device/)  
- **Output:** Serial console (JSON events, same schema as the desktop simulator)  
- **Purpose:** Demonstrate lightweight, on-device purple-team simulation for IoT or field demos  

### Example Run

<p align="center">
  <img src="https://github.com/user-attachments/assets/3178367a-f524-47eb-9173-a077723204b8" 
       alt="LilyGo T-Dongle boot" width="300"/>
</p>

Example telemetry output from serial console:

<p align="center">
  <img src="https://github.com/user-attachments/assets/3cb7dcf2-094c-4c81-8342-18582265966d" 
       alt="PurpleSim Telemetry Output" width="550"/>
</p>

> The device mode uses the same ATT&CK-style event format (`ProcessCreate`, `NetworkConnect`, `FileWrite`) as the desktop version.  
> It’s a self-contained demo—no network connection or collector required.


---


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

## Device Mode (ESP32-S3 — LilyGo T-Dongle)

PurpleSim can also run on a tiny microcontroller to emit ATT&CK-style telemetry over **serial**.

**Folder:** `device/`  
**Board:** LilyGo T-Dongle (ESP32-S3)  
**Firmware:** MicroPython  
**Output:** Pretty-printed JSON events in the serial console (no network required)

### Quick Start (device)
1. Copy the files in `device/` to the board (e.g., with Thonny).
2. Rename `device/secrets.py.example` → `secrets.py` **on the device only** (do not commit `secrets.py`).
3. Soft-reboot the board. You’ll see a banner and three events:
   - `ProcessCreate` (T1059)
   - `NetworkConnect` (T1071)
   - `FileWrite` (T1003)

> The desktop simulator (`simulator.py`) is unchanged. Use it for JSONL outputs.  
> Device mode is a minimal, serial-only demo suitable for screenshots and demos.


