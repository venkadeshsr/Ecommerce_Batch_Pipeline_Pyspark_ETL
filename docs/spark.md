# Apache Spark Guide

## What it does
Apache Spark handles the ETL transformation logic for this project.

## How to run
From the project root, run:

```bash
docker exec -i ETL_Spark python /opt/spark/work/src/main.py
```

## Main jobs
- job_bronze_to_silver.py: reads raw data and prepares the silver layer
- job_gold_reports.py: builds gold reporting datasets and loads them to PostgreSQL
