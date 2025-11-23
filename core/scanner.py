import subprocess
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[Scanner] Running Nmap on {target}")
        results["nmap"] = subprocess.check_output(["nmap", "-sV", "-T4", target], text=True)
    except Exception as e:
        log_action(f"[Scanner] Error: {e}")
    return results
