import subprocess
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[WebScan] Running Nikto on {target}")
        nikto_out = subprocess.check_output(["nikto", "-h", target], text=True)
        results["nikto"] = nikto_out

        log_action(f"[WebScan] Running Dirb on {target}")
        dirb_out = subprocess.check_output(["dirb", f"http://{target}"], text=True)
        results["dirb"] = dirb_out

    except Exception as e:
        log_action(f"[WebScan] Error: {e}")
    return results
