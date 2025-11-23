from jinja2 import Template
from weasyprint import HTML
from utils.logger import log_action
import datetime
import os

def generate_report(target, recon, ports, vulns, web, brute, privilege):
    log_action("[Report] Generating PDF Report")
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
    timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    html_path = f"output/reports/report-{timestamp}.html"
    pdf_path = f"output/reports/report-{timestamp}.pdf"

    with open(html_path, "w") as f:
        f.write(html)

    HTML(string=html).write_pdf(pdf_path)
    log_action(f"[Report] Saved HTML to {html_path}")
    log_action(f"[Report] Saved PDF to {pdf_path}")
