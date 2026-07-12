FROM python:3.9-slim

# Install system dependencies (Java 21 is required for PySpark 4.0.3)
RUN apt-get update && apt-get install -y \
    openjdk-21-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /opt/spark/work

# Install the required Python data engineering packages cleanly
RUN pip install --no-cache-dir \
    pyspark==4.0.3 \
    faker \
    pandas