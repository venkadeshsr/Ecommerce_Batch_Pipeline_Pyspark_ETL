FROM python:3.10-slim

LABEL maintainer="data-engineer" \
      description="Standardized Spark runtime for the ecommerce batch ETL pipeline"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jre-headless \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/spark/jars \
    && curl -L https://jdbc.postgresql.org/download/postgresql-42.7.4.jar -o /opt/spark/jars/postgresql-42.7.4.jar

WORKDIR /opt/spark/work

RUN pip install --no-cache-dir \
    pyspark==3.5.0 \
    faker \
    pandas