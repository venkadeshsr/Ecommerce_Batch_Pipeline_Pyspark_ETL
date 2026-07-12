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
    schedule_interval='*/1 * * * *', # Cron expression for "Every 2 minutes"
    catchup=False,                  # Prevents running historical missed jobs
) as dag:

    # The task that reaches into the Spark container to run your script
    run_pipeline = BashOperator(
        task_id='execute_pyspark_etl',
        # NOTE: Replace 'your_script_name.py' with the actual name of your execution file
        bash_command='docker exec -i dynamic_pipeline python /opt/spark/work/src/generate_sales_data.py',
    )

    run_pipeline