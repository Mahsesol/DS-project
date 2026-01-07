
from datetime import datetime

LOG_FILE = "system.log"
_logs = []  # logs in memory


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    _logs.append(entry)

    # write to file immediately
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")


def show_logs():
    if not _logs:
        print("No logs recorded.")
        return

    print("\n===== SYSTEM LOGS =====")
    for entry in _logs:
        print(entry)


def clear_logs():
    global _logs
    _logs = []