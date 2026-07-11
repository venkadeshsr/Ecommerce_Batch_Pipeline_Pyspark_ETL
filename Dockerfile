FROM python:3.9-slim
RUN apt-get update && apt-get install -y openjdk-21-jre-headless && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/spark/work
RUN pip install --no-cache-dir pyspark
CMD ["bash"]
