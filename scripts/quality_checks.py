# scripts/quality_checks.py

import pandas as pd
import re
from pathlib import Path

# --- Load data ---
data_path = Path("data/sales_data.xlsx")
df = pd.read_excel(data_path)

# --- Quality checks ---

# Missing values
missing_values = df.isnull().sum()

# Duplicates
duplicate_count = df.duplicated().sum()

# Email format validation
def check_email_format(email):
    if pd.isnull(email):
        return False
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(pattern, str(email)))

df["ValidEmail"] = df["Email"].apply(check_email_format)
invalid_emails = df[~df["ValidEmail"]]

# Date format validation
def check_date_format(date):
    try:
        pd.to_datetime(date, errors='raise')
        return True
    except:
        return False

df["ValidDate"] = df["PurchaseDate"].apply(check_date_format)
invalid_dates = df[~df["ValidDate"]]

# --- Summary ---
summary = {
    "Missing Values": missing_values.to_dict(),
    "Duplicate Rows": int(duplicate_count),
    "Invalid Emails": len(invalid_emails),
    "Invalid Dates": len(invalid_dates)
}

print("=== DATA QUALITY SUMMARY ===")
for k, v in summary.items():
    print(f"{k}: {v}")

# --- Export issues to Excel ---
output_path = Path("reports/data_quality_report.xlsx")
with pd.ExcelWriter(output_path) as writer:
    pd.DataFrame(missing_values).to_excel(writer, sheet_name="Missing Values")
    invalid_emails.to_excel(writer, sheet_name="Invalid Emails", index=False)
    invalid_dates.to_excel(writer, sheet_name="Invalid Dates", index=False)

print(f"\nReport generated at: {output_path.resolve()}")

from report_generator import create_report

create_report(
    missing_values=missing_values,
    invalid_emails=invalid_emails,
    invalid_dates=invalid_dates
)