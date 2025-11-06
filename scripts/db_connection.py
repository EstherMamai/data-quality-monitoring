# scripts/db_connection.py

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///../data/sales_data.db")
df = pd.read_excel("../data/sales_data.xlsx")
df.to_sql("sales", engine, if_exists="replace", index=False)

# Example query
check_nulls = pd.read_sql("SELECT COUNT(*) AS null_emails FROM sales WHERE Email IS NULL", engine)
print(check_nulls)