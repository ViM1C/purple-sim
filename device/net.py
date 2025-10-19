# Minimal stubs so device/main.py can import these without needing Wi-Fi/NTP.
# You can replace with real MicroPython networking later.

def connect_wifi(ssid: str, psk: str, timeout_s: int = 20):
    """
    Stub: return a tuple shaped like network.WLAN().ifconfig()
    (ip, subnet, gateway, dns). No real connection is attempted.
    """
    return ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0")

def sync_time(retries: int = 5):
    """Stub: pretend NTP failed/unused and return False."""
    return False
