Installation Guide

Python is mandatory

after python installing install pyspar

python -m pip install pyspark on your terminal

-----

Architecture layer

Raw CSV
   │
   ▼
Read CSV (PySpark)
   │
   ▼
Bronze Layer
   │
   ▼
Data Cleaning
   │
   ├── Remove duplicates
   ├── Handle nulls
   ├── Data type conversion
   ├── Data validation
   └── Add Year/Month/Quarter
   │
   ▼
Silver Layer (sales_clean)
   │
   ├── Sales by Date
   ├── Sales by Product
   ├── Sales by Category
   ├── Sales by Region
   ├── Product × Region
   ├── Category × Region
   ├── Monthly Sales
   ├── Monthly Category Sales
   ├── Monthly Product Sales
   └── KPI Summary
   │
   ▼
Gold Layer (Parquet/Delta)

//////

In a real PySpark project

A common pipeline is:

1 Bronze table (raw data)
1 Silver table (cleaned and enriched data)
8–10 Gold tables (aggregated reporting datasets)

This is a standard ETL design used in data engineering projects, where the Silver layer acts as the source for multiple reporting-ready Gold datasets.

///

End to End flow : (As per Code)

orders.csv
      │
      ▼
Read CSV
      │
      ▼
Bronze
      │
      ▼
Clean Data
      │
      ▼
Silver
      │
      ├─────────────► Sales by Date
      │
      ├─────────────► Sales by Product
      │
      ├─────────────► Sales by Category
      │
      └─────────────► Sales by Region
                     │
                     ▼
                  Gold Layer

----

Implement Airflow and move on to real time projects

Start
   │
   ▼
Check File Exists
   │
   ▼
Archive Previous Raw File
   │
   ▼
Bronze
   │
   ▼
Data Quality Check
   │
   ▼
Silver
   │
   ▼
Gold
   │
   ▼
Generate Report
   │
   ▼
Send Email Notification
   │
   ▼
End

---

Dokcer installtion command

docker run -it --name pipeline_test -v "${PWD}:/opt/spark/work" -w /opt/spark/work apache/spark:3.5.0 bash

Docker verification commands

# Start the Postgres and Spark containers
docker compose up -d --build postgres spark

# Run the ETL job inside the Spark container
docker exec -i ETL_Spark python /opt/spark/work/src/main.py

# Check that the Postgres table exists
docker exec -i ETL_Postgres psql -U postgres -d sales_db -c "\dt"

# Query the uploaded data from Spark
docker exec -i ETL_Postgres psql -U postgres -d sales_db -c "SELECT * FROM gold_sales_by_date LIMIT 10;"

# Confirm the row count
docker exec -i ETL_Postgres psql -U postgres -d sales_db -c "SELECT COUNT(*) AS rows_from_spark FROM gold_sales_by_date;"

# If pgAdmin is connecting from your machine, use host localhost and port 55432 instead of 5432."