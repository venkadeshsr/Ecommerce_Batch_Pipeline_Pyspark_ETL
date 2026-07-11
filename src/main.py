# Create Spark Session

from pyspark.sql import SparkSession

# Read CSV (Bronze)

spark = SparkSession.builder \
    .appName("Sales Reporting Pipeline") \
    .getOrCreate()

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("D:/Data_Engineer/Github_Repository/Ecommerce_Batch_Pipeline_Pyspark_ETL/data/raw/ecommerce_sales_data.csv")

df.show()
df.printSchema()

spark.stop()