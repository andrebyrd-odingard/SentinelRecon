from jinja2 import Template
from utils.logger import log_action
import datetime
import os

def generate_report(target, recon, ports, vulns, web, brute, privilege):
    log_action("[Report] Generating report")
    with open("templates/report_template.html") as f:
        template = Template(f.read())
    html = template.render(
        target=target,
        date=str(datetime.datetime.now()),
        recon=recon,
        ports=ports,
        vulns=vulns,
        web=web,
        brute=brute,
        privilege=privilege
    )
    os.makedirs("output/reports", exist_ok=True)
    filename = f"output/reports/report-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}.html"
    with open(filename, "w") as f:
        f.write(html)
    log_action(f"[Report] Saved to {filename}")
