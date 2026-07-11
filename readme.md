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