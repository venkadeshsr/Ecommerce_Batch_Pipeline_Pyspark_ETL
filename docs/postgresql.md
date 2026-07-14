# PostgreSQL Guide

## What it does
PostgreSQL stores the curated reporting tables produced by Spark.

## Access
Use the following connection details:
- Host: localhost
- Port: 55432
- Database: sales_db
- User: postgres
- Password: mysecretpassword

## Verify tables
```bash
docker exec -i ETL_Postgres psql -U postgres -d sales_db -c "\dt"
```