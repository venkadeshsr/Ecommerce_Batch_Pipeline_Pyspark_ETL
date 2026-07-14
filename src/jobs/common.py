import os
from typing import Dict

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col


def get_spark_session(app_name: str) -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.jars", "/opt/spark/jars/postgresql-42.7.4.jar")
        .getOrCreate()
    )


def get_jdbc_config() -> Dict[str, str]:
    return {
        "url": "jdbc:postgresql://"
        + os.getenv("POSTGRES_HOST", "postgres")
        + ":5432/sales_db",
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "change_me"),
        "driver": "org.postgresql.Driver",
    }


def read_raw_csv(spark: SparkSession, input_path: str) -> DataFrame:
    if not os.path.exists(input_path):
        return spark.createDataFrame(
            [],
            schema="order_date string, product_name string, category string, region string, quantity int, sales double, profit double",
        )

    return (
        spark.read.format("csv")
        .option("header", "true")
        .option("inferSchema", "true")
        .load(input_path)
    )


def read_postgres_table(spark: SparkSession, table_name: str) -> DataFrame:
    return (
        spark.read.format("jdbc")
        .options(**get_jdbc_config())
        .option("dbtable", table_name)
        .load()
    )


def write_postgres_table(df: DataFrame, table_name: str, mode: str = "overwrite") -> None:
    if df.rdd.isEmpty():
        print(f"Skipping load for {table_name}: data frame is empty.")
        return

    (
        df.write.format("jdbc")
        .mode(mode)
        .options(**get_jdbc_config())
        .option("dbtable", table_name)
        .save()
    )
    print(f"Loaded data into PostgreSQL table: {table_name}")


def prepare_bronze_dataframe(df: DataFrame) -> DataFrame:
    return (
        df.withColumnRenamed("Order Date", "order_date")
        .withColumnRenamed("Product Name", "product_name")
        .withColumnRenamed("Category", "category")
        .withColumnRenamed("Region", "region")
        .withColumnRenamed("Quantity", "quantity")
        .withColumnRenamed("Sales", "sales")
        .withColumnRenamed("Profit", "profit")
        .withColumn("order_date", col("order_date").cast("date"))
        .withColumn("quantity", col("quantity").cast("int"))
        .withColumn("sales", col("sales").cast("decimal(12,2)"))
        .withColumn("profit", col("profit").cast("decimal(12,2)"))
    )


def prepare_silver_dataframe(df: DataFrame) -> DataFrame:
    from pyspark.sql.functions import month, quarter, when, year, round

    return (
        df.dropDuplicates()
        .na.drop()
        .withColumn("order_date", col("order_date").cast("date"))
        .withColumn("year", year("order_date"))
        .withColumn("month", month("order_date"))
        .withColumn("quarter", quarter("order_date"))
        .withColumn(
            "profit_margin",
            when(col("sales") != 0, round(col("profit") / col("sales"), 2)).otherwise(0.0),
        )
    )
