# Project Setup

## Prerequisites
- Docker Desktop
- Python 3.10+
- Internet access for pulling images

## Start the stack
```bash
docker compose up -d --build
```

## Run the ETL pipeline
```bash
docker exec -i ETL_Spark python /opt/spark/work/src/main.py
```
