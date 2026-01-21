
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'mly0100_pipeline',
    default_args=default_args,
    description='MLY0100 Brazilian E-commerce ML pipeline (CRISP-DM)',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

business_understanding = BashOperator(
    task_id='business_understanding',
    bash_command='python src/crispdm/business_understanding.py',
    dag=dag,
)

data_understanding = BashOperator(
    task_id='data_understanding',
    bash_command='python src/crispdm/data_understanding.py',
    dag=dag,
)

data_preparation = BashOperator(
    task_id='data_preparation',
    bash_command='python src/crispdm/data_preparation.py',
    dag=dag,
)

modeling_classification = BashOperator(
    task_id='modeling_classification',
    bash_command='python src/crispdm/modeling_classification.py',
    dag=dag,
)

modeling_regression = BashOperator(
    task_id='modeling_regression',
    bash_command='python src/crispdm/modeling_regression.py',
    dag=dag,
)

evaluation = BashOperator(
    task_id='evaluation',
    bash_command='python src/crispdm/evaluation.py',
    dag=dag,
)

deployment = BashOperator(
    task_id='deployment',
    bash_command='python src/crispdm/deployment.py',
    dag=dag,
)

# Dependencias: modelado en paralelo
business_understanding >> data_understanding >> data_preparation >> [modeling_classification, modeling_regression] >> evaluation >> deployment
