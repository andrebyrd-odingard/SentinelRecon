import subprocess
from utils.logger import log_action

async def run(target):
    results = {"nuclei_results": ""}
    try:
        log_action(f"[VulnScan] Running Nuclei scan on {target}")
        cmd = ["nuclei", "-u", target]
        output = subprocess.check_output(cmd, text=True)
        results["nuclei_results"] = output
    except Exception as e:
        log_action(f"[VulnScan] Error: {e}")
    return results
