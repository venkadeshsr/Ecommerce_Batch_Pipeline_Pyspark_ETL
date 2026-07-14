import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# --------------------------------------------
# Create Spark Session
# --------------------------------------------

spark = SparkSession.builder \
    .appName("Sales Reporting Pipeline") \
    .config("spark.jars", "/opt/spark/jars/postgresql-42.7.4.jar") \
    .getOrCreate()

# --------------------------------------------
# Read Raw CSV
# --------------------------------------------

raw_data_path = "data/raw/"

df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(raw_data_path)

print("Raw Data")
df.show(5)
df.printSchema()

# This calculates the count and explicitly prints it out
row_count = df.count()
print(f"Total row count: {row_count}")

# --------------------------------------------
# Bronze Layer
# --------------------------------------------

df.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/bronze/orders")

bronze_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("./data/bronze/orders")

# --------------------------------------------
# Silver Layer - Cleaning
# --------------------------------------------

silver_df = bronze_df.dropDuplicates()

silver_df = silver_df.na.drop()

silver_df = silver_df.withColumn(
    "Order Date",
    to_date(col("Order Date"), "yyyy-MM-dd")
)

silver_df = silver_df.withColumn("Year", year("Order Date")) \
                     .withColumn("Month", month("Order Date")) \
                     .withColumn("Quarter", quarter("Order Date"))

silver_df = silver_df.withColumn(
    "Profit Margin",
    round(col("Profit") / col("Sales"), 2)
)

silver_df.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/silver/orders")

silver_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("./data/silver/orders")

# --------------------------------------------
# Gold Report 1 - Sales by Date
# --------------------------------------------

sales_by_date = silver_df.groupBy("Order Date") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

sales_by_date.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/sales_by_date")

jdbc_url = "jdbc:postgresql://" + os.getenv("POSTGRES_HOST", "postgres") + ":5432/sales_db"
jdbc_properties = {
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "mysecretpassword"),
    "driver": "org.postgresql.Driver"
}

sales_by_date_db = sales_by_date.select(
    col("Order Date").alias("order_date"),
    col("Total Sales").alias("total_sales"),
    col("Total Profit").alias("total_profit"),
    col("Total Quantity").alias("total_quantity")
)

sales_by_date_db.write \
    .format("jdbc") \
    .mode("overwrite") \
    .option("url", jdbc_url) \
    .options(**jdbc_properties) \
    .option("dbtable", "gold_sales_by_date") \
    .save()

print("Loaded sales_by_date into Postgres table gold_sales_by_date")

# --------------------------------------------
# Gold Report 2 - Sales by Product
# --------------------------------------------

sales_by_product = silver_df.groupBy("Product Name") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

sales_by_product.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/sales_by_product")

# --------------------------------------------
# Gold Report 3 - Sales by Category
# --------------------------------------------

sales_by_category = silver_df.groupBy("Category") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

sales_by_category.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/sales_by_category")

# --------------------------------------------
# Gold Report 4 - Sales by Region
# --------------------------------------------

sales_by_region = silver_df.groupBy("Region") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

sales_by_region.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/sales_by_region")

# --------------------------------------------
# Gold Report 5 - Monthly Sales
# --------------------------------------------

monthly_sales = silver_df.groupBy("Year", "Month") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    ) \
    .orderBy("Year", "Month")

monthly_sales.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/monthly_sales")

# --------------------------------------------
# Gold Report 6 - Product by Region
# --------------------------------------------

product_region = silver_df.groupBy("Product Name", "Region") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

product_region.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/product_region")

# --------------------------------------------
# Gold Report 7 - Category by Region
# --------------------------------------------

category_region = silver_df.groupBy("Category", "Region") \
    .agg(
        sum("Sales").alias("Total Sales"),
        sum("Profit").alias("Total Profit"),
        sum("Quantity").alias("Total Quantity")
    )

category_region.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/category_region")

# --------------------------------------------
# Gold Report 8 - KPI Summary
# --------------------------------------------

kpi_summary = silver_df.agg(
    sum("Sales").alias("Total Sales"),
    sum("Profit").alias("Total Profit"),
    sum("Quantity").alias("Total Quantity"),
    round(avg("Sales"), 2).alias("Average Sales"),
    round(avg("Profit"), 2).alias("Average Profit")
)

kpi_summary.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("./data/gold/kpi_summary")

# --------------------------------------------
# Display Reports
# --------------------------------------------

print("\nSales by Date")
sales_by_date.show()

print("\nSales by Product")
sales_by_product.show()

print("\nSales by Category")
sales_by_category.show()

print("\nSales by Region")
sales_by_region.show()

print("\nMonthly Sales")
monthly_sales.show()

print("\nProduct by Region")
product_region.show()

print("\nCategory by Region")
category_region.show()

print("\nKPI Summary")
kpi_summary.show()

print("\nPipeline completed successfully!")

spark.stop()