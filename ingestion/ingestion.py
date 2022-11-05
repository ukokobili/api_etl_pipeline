import os
from datetime import datetime
from airflow import DAG
from etl import run_etl
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


local_workflow = DAG(
    "IngestionDag"
)

with local_workflow:

    api_request = PythonOperator(
        task_id="request",
        python_callable=
    )

    ingest_csv = PythonOperator(
        task_id="ingest",
        python_callable=
    )

    api_request >> ingest_csv 

