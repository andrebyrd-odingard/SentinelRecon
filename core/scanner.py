import subprocess
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[Scanner] Running advanced Nmap on {target}")
        cmd = ["nmap", "-sV", "-O", "--script", "default,vuln", "-T4", target]
        output = subprocess.check_output(cmd, text=True)
        results["nmap_output"] = output
    except Exception as e:
        log_action(f"[Scanner] Error: {e}")
    return results
