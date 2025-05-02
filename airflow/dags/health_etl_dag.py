import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.scripts.fetch_data import fetch_data
from etl.scripts.transform_data import transform_data
from etl.scripts.load_to_postgres import load_to_postgres

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='health_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for public health data',
    schedule_interval='@daily',
    catchup=False,
    tags=['health', 'etl'],
) as dag:

    fetch = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data,
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_to_postgres,
    )

    fetch >> transform >> load
