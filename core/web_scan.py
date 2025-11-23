from utils.logger import log_action

async def run(target):
    results = {}
    try:
        log_action(f"[WebScan] Performing dummy web scan on {target}")
        results["headers"] = {"Server": "Apache/2.4.1"}
        results["issues"] = ["Directory listing enabled"]
    except Exception as e:
        log_action(f"[WebScan] Error: {e}")
    return results
