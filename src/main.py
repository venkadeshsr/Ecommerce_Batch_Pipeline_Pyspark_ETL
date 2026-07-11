# Create Spark Session

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Read CSV (Bronze)

spark = SparkSession.builder \
    .appName("Sales Reporting Pipeline") \
    .getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("./data/raw/ecommerce_sales_data.csv")

df.show()
df.printSchema()

# Save Bronze Data

df.write.mode("overwrite").parquet("data/bronze/orders")

# Read Bronze

bronze_df = spark.read.parquet("bronze/orders")

# Silver Layer (Cleaning)

# remove duplicates

silver_df = bronze_df.dropDuplicates()

# remove null's

silver_df = silver_df.na.drop()

# Convert date format

silver_df = silver_df.withColumn(
    "Order Date",
    to_date(col("Order Date"), "yyyy-MM-dd")
)

# Add derived columns

silver_df = silver_df.withColumn(
    "Year",
    year("Order Date")
)

silver_df = silver_df.withColumn(
    "Month",
    month("Order Date")
)

silver_df = silver_df.withColumn(
    "Quarter",
    quarter("Order Date")
)

# profit margin

silver_df = silver_df.withColumn(
    "Profit Margin",
    round(col("Profit") / col("Sales"), 2)
)

# save silver layer

silver_df = silver_df.withColumn(
    "Profit Margin",
    round(col("Profit") / col("Sales"), 2)
)

# Stop Spark Session

spark.stop()