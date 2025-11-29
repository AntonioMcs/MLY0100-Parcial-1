"""
Airflow DAG to orchestrate Kedro pipelines for the diabetes project.

How to use:
1. Copy this file into your Airflow `dags/` folder (or mount the repo).
2. Set the environment variable KEDRO_PROJECT_PATH to the folder that contains `pyproject.toml`.
   By default it points to `/opt/airflow/dags/mly0100parcial-kedro`.
3. Make sure the Airflow environment has Kedro + project dependencies installed
   (you can copy the Dockerfile instructions or install via `pip install -r requirements.txt`).
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

# Path where the Kedro project lives inside the Airflow worker/container.
KEDRO_PROJECT_PATH = os.environ.get(
    "KEDRO_PROJECT_PATH",
    "/opt/airflow/dags/mly0100parcial-kedro",
)

BASE_CMD = f"cd {KEDRO_PROJECT_PATH} && "

default_args = {
    "owner": "kedro",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    dag_id="kedro_diabetes_pipeline",
    description="Run Kedro diabetes + reporting pipelines",
    default_args=default_args,
    schedule_interval="0 3 * * *",  # every day at 03:00
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["kedro", "diabetes"],
) as dag:
    run_diabetes = BashOperator(
        task_id="run_diabetes_pipeline",
        bash_command=BASE_CMD + "kedro run --pipeline diabetes",
    )

    run_unsupervised = BashOperator(
        task_id="run_unsupervised_pipeline",
        bash_command=BASE_CMD + "kedro run --pipeline unsupervised_learning",
    )

    run_reporting = BashOperator(
        task_id="run_reporting_pipeline",
        bash_command=BASE_CMD + "kedro run --pipeline reporting",
    )

    run_diabetes >> [run_unsupervised, run_reporting]

