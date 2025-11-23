import subprocess
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[Recon] WHOIS for {target}")
        results["whois"] = subprocess.check_output(["whois", target], text=True)

        log_action(f"[Recon] DIG for {target}")
        results["dig"] = subprocess.check_output(["dig", target], text=True)

    except Exception as e:
        log_action(f"[Recon] Error: {e}")
    return results
