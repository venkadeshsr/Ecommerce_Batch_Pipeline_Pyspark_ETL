import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jobs.common import get_spark_session, prepare_silver_dataframe, read_postgres_table, write_postgres_table


def main() -> None:
    spark = get_spark_session("gold_reports_job")

    silver_df = read_postgres_table(spark, "silver_orders")
    silver_df = prepare_silver_dataframe(silver_df)

    reports = {
        "gold_sales_by_date": silver_df.groupBy("order_date").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_sales_by_product": silver_df.groupBy("product_name").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_sales_by_category": silver_df.groupBy("category").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_sales_by_region": silver_df.groupBy("region").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_monthly_sales": silver_df.groupBy("year", "month").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity")
         .orderBy("year", "month"),
        "gold_product_region": silver_df.groupBy("product_name", "region").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_category_region": silver_df.groupBy("category", "region").agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
        "gold_kpi_summary": silver_df.agg(
            {"sales": "sum", "profit": "sum", "quantity": "sum"}
        ).withColumnRenamed("sum(sales)", "total_sales")
         .withColumnRenamed("sum(profit)", "total_profit")
         .withColumnRenamed("sum(quantity)", "total_quantity"),
    }

    for table_name, report_df in reports.items():
        write_postgres_table(report_df, table_name)

    print("Gold reports job completed successfully")
    spark.stop()


if __name__ == "__main__":
    main()
