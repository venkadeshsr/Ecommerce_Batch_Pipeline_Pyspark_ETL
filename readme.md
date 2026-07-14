# Ecommerce Batch Pipeline with PySpark and Airflow

This project demonstrates a production-style batch ETL pipeline for ecommerce sales data. It generates raw sales files, processes them with Apache Spark, stores curated data in PostgreSQL, and orchestrates the workflow with Apache Airflow.

## What the project does

- Generates synthetic ecommerce sales data
- Ingests raw CSV files into a Spark-based pipeline
- Builds bronze, silver, and gold layers
- Loads reporting tables into PostgreSQL
- Archives raw files and generated reports
- Schedules daily execution with Airflow

## Architecture overview

Raw CSV -> Bronze -> Silver -> Gold -> PostgreSQL

## Tech stack

- Python
- Apache Spark
- PostgreSQL
- Apache Airflow
- Docker
- pgAdmin

## Project structure

- src/: Spark ETL entrypoints and job modules
- dags/: Airflow DAG definitions
- data/: raw, processed, and archived data
- docs/: detailed documentation for each tool
- postgress/: PostgreSQL initialization scripts

## Quick start

1. Start the containers
   ```bash
   docker compose up -d --build
   ```
2. Run the ETL workflow
   ```bash
   docker exec -i ETL_Spark python /opt/spark/work/src/main.py
   ```
3. Open Airflow at http://localhost:8080

## Documentation

- [docs/project_setup.md](docs/project_setup.md)
- [docs/spark.md](docs/spark.md)
- [docs/airflow.md](docs/airflow.md)
- [docs/postgresql.md](docs/postgresql.md)
- [docs/docker.md](docs/docker.md)
- [docs/pgadmin.md](docs/pgadmin.md)

## Notes

- Raw files are archived by day only in the data/archive folder
- The Airflow DAG is scheduled to run daily at 9:00 AM
- The Spark pipeline now loads PostgreSQL tables for each reporting dataset instead of relying only on CSV outputs

## Repository hygiene

- Python bytecode caches such as __pycache__ and pytest artifacts are generated locally and should not be committed
- The repository uses .gitignore to prevent these files from being tracked
- Tests are optional and live under the tests folder; they are not required for the ETL runtime