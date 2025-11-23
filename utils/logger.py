from datetime import datetime

def log_action(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    with open("logs/activity.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
