## 🧮 Data Quality Monitoring System

### 📘 Overview

The **Data Quality Monitoring System** is a Python-based tool that automatically scans Excel datasets to identify and summarize data quality issues.
It ensures data integrity by detecting **missing values**, **duplicate records**, and **invalid entries**, and generates a detailed Excel report for review.

---

### 🚀 Key Features

* **Excel File Support:** Processes `.xlsx` files for quality checks.
* **Missing Value Detection:** Highlights columns with incomplete data.
* **Duplicate Record Identification:** Flags repeated rows.
* **Data Validation Rules:** Checks for invalid emails and incorrect date formats.
* **Automated Reporting:** Saves a summary report in Excel format for review.

---

### 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * `pandas` – data manipulation and analysis
  * `openpyxl` – Excel file handling
  * `re` – regular expressions for email validation

---

### 📂 Project Structure

```
data-quality-monitoring/
│
├── data/
│   └── sales_data.xlsx            # Input Excel dataset
│
├── reports/
│   └── data_quality_report.xlsx   # Generated output report
│
├── scripts/
│   └── quality_checks.py          # Main data validation script
│
├── venv1/                         # Virtual environment
│
└── README.md
```

---

### ⚙️ How It Works

1. **Load Dataset:** Reads Excel data using pandas.
2. **Run Quality Checks:** Performs:

   * Missing value detection
   * Duplicate row identification
   * Invalid email format detection
   * Invalid date validation
3. **Generate Report:** Exports summary results to `reports/data_quality_report.xlsx`.

---

### ▶️ Running the Script

#### 1️⃣ Activate the virtual environment:

```bash
venv1\Scripts\activate
```

#### 2️⃣ Run the quality check script:

```bash
python scripts/quality_checks.py
```

#### 3️⃣ View the results:

Open the file in `reports/data_quality_report.xlsx` to review the summary.

---

### 🧠 Example Output

```
=== DATA QUALITY SUMMARY ===
Missing Values: {'CustomerID': 0, 'Email': 1, 'PurchaseDate': 0, 'Amount': 1}
Duplicate Rows: 0
Invalid Emails: 2
Invalid Dates: 1
```

---

### 🔧 Planned Enhancements

* [ ] Add CSV file support
* [ ] Automate data validation rules for any dataset structure
* [ ] Integrate dashboard visualization (Power BI / Streamlit)
* [ ] Schedule automated runs (e.g., daily/weekly data checks)
