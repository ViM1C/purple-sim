# Minimal emitter for PurpleSim on MicroPython.
# Keeps a small in-memory queue and builds event dicts.

class TelemetryEmitter:
    def __init__(self, device_id="tdongle-s3-01", collector_url="", shared_key=b"", max_queue=100):
        self.device_id = device_id
        self.collector_url = collector_url or ""
        self.shared_key = shared_key or b""
        self.max_queue = max_queue
        self.queue = []
        self.schema_version = "1.0.0"

    def _enqueue(self, evt: dict):
        if len(self.queue) >= self.max_queue:
            self.queue.pop(0)
        self.queue.append(evt)

    def emit(self, *, scenario, event_type, tactic=None, technique_id=None, step_id=None,
             severity="info", fields=None, ts=None):
        evt = {
            "schema": self.schema_version,
            "device_id": self.device_id,
            "ts": ts or "1970-01-01T00:00:00",  # device may not have NTP; not needed for demo
            "scenario": scenario,
            "event_type": event_type,
            "tactic": tactic,
            "technique_id": technique_id,
            "step_id": step_id,
            "severity": severity,
            "fields": fields or {},
        }
        self._enqueue(evt)
