# Project Overview

This repository contains an end-to-end batch ETL pipeline for ecommerce sales data. The workflow generates raw sales files, processes them with Apache Spark, loads curated data into PostgreSQL, and archives the output for auditability.

## Architecture

- Raw layer: CSV files generated in data/raw
- Bronze layer: ingested and normalized records
- Silver layer: cleaned and enriched datasets
- Gold layer: reporting datasets loaded into PostgreSQL
- Orchestration: Apache Airflow for scheduled execution

## Main Tools

- Python
- Apache Spark
- PostgreSQL
- Apache Airflow
- Docker
- pgAdmin

## Project Structure

- src: Spark ETL jobs and helpers
- dags: Airflow DAG definitions
- data: input, processed, and archived datasets
- postgress: PostgreSQL initialization scripts
- docs: tool-specific documentation
