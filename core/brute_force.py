import subprocess
from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[BruteForce] Running Hydra against FTP on {target}")
        cmd = ["hydra", "-L", "data/wordlists/users.txt", "-P", "data/wordlists/passwords.txt", "ftp://" + target]
        output = subprocess.check_output(cmd, text=True)
        results["hydra"] = output
    except Exception as e:
        log_action(f"[BruteForce] Error: {e}")
    return results
