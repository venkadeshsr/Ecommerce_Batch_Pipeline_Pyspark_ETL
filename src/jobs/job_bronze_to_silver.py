import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from jobs.common import get_spark_session, prepare_bronze_dataframe, prepare_silver_dataframe, read_raw_csv, write_postgres_table


def main() -> None:
    spark = get_spark_session("bronze_to_silver_job")

    project_root = Path(__file__).resolve().parents[2]
    raw_path = str(project_root / "data" / "raw")
    bronze_df = prepare_bronze_dataframe(read_raw_csv(spark, raw_path))
    bronze_df.createOrReplaceTempView("bronze_orders")

    silver_df = prepare_silver_dataframe(bronze_df)

    write_postgres_table(silver_df, "silver_orders")

    print("Bronze to Silver job completed successfully")
    spark.stop()


if __name__ == "__main__":
    main()
