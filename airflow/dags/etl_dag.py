# import python libraries
import os
from datetime import datetime, timedelta
from airflow import DAG
#from etl import run_etl
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# setup Airflow default arguments
default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 10,
}

# define the Dag
dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='API DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

# # creating tasks
# api_call_ingest = PythonOperator(
#         task_id="request",
#         python_callable=run_etl,
#         execution_timeout=datetime.timedelta(minutes=45),
#         dag=dag
#     )

ingest = BashOperator(
    task_id = "testing",
    bash_command = 'echo "Yello World!"'
)
    # setting up dependencies 
ingest

