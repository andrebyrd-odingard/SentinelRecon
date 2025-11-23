import asyncio
from core import recon, scanner, vuln_scan, web_scan, brute_force, privilege, report
from utils.logger import log_action
import argparse

async def run_all_modules(target):
    log_action(f"Starting Pentest on {target}")
    results = await asyncio.gather(
        recon.run(target),
        scanner.run(target),
        vuln_scan.run(target),
        web_scan.run(target),
        brute_force.run(target),
        privilege.run(target)
    )
    report.generate_report(target, *results)
    log_action("Pentest complete.")

def main():
    parser = argparse.ArgumentParser(description="SentinelRecon - Autonomous Pentest")
    parser.add_argument("target", help="Target IP or domain")
    args = parser.parse_args()
    asyncio.run(run_all_modules(args.target))

if __name__ == "__main__":
    main()
    