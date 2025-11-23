import subprocess
import requests
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[Recon] WHOIS for {target}")
        results["whois"] = subprocess.check_output(["whois", target], text=True)

        log_action(f"[Recon] DIG for {target}")
        results["dig"] = subprocess.check_output(["dig", target], text=True)

        log_action(f"[Recon] crt.sh cert scrape for {target}")
        r = requests.get(f"https://crt.sh/?q={target}&output=json", timeout=10)
        results["crtsh"] = r.text if r.ok else "No results or error"

    except Exception as e:
        log_action(f"[Recon] Error: {e}")
    return results
