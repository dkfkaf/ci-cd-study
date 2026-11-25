from pathlib import Path

from orderlab.csv_report import revenue_from_csv


revenue= revenue_from_csv("data/sample_orders.csv")

site = Path("site")
site.mkdir(exist_ok=True)

(site/"index.html").write_text(
    f"<h1>orderlab report</h1> <p>revenuee: {revenue:,} KRW</p>",
    encoding="utf-8",

)