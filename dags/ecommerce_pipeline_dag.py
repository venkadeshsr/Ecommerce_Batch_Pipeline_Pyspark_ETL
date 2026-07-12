from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments for the workflow
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2026, 7, 1), # Sets start date in the past so it triggers immediately
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# DAG Definition
with DAG(
    'ecommerce_batch_etl',
    default_args=default_args,
    description='Testing our PySpark ETL pipeline every 2 minutes',
    schedule_interval='*/20 * * * *', # Cron expression for "Every 0 minutes"
    catchup=False,                  # Prevents running historical missed jobs
) as dag:

    generate_sales_data = BashOperator(
        task_id='generate_sales_data',
        bash_command='docker exec -i ETL_Spark python /opt/spark/work/src/generate_sales_data.py',
    )

    run_pyspark_etl = BashOperator(
        task_id='run_pyspark_etl',
        bash_command='docker exec -i ETL_Spark python /opt/spark/work/src/main.py',
    )

    archive_pipeline_outputs = BashOperator(
        task_id='archive_pipeline_outputs',
        bash_command='docker exec -i ETL_Spark python /opt/spark/work/src/archive_pipeline_outputs.py',
    )

    generate_sales_data >> run_pyspark_etl >> archive_pipeline_outputs