# Apache Airflow Guide

## What it does
Airflow schedules and orchestrates the ETL workflow.

## Access
Open the Airflow UI at:

- http://localhost:8080

## Schedule
The DAG runs daily at 9:00 AM.

## Useful commands
```bash
docker exec -it Airflow airflow dags reserialize
```