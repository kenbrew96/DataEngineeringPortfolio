from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

def build_data_pipeline():
    dag = DAG('data_pipeline', description='Simple Data Pipeline',
              schedule_interval='@daily', start_date=datetime(2022, 1, 1), catchup=False)

    start_task = DummyOperator(task_id='start', dag=dag)
    end_task = DummyOperator(task_id='end', dag=dag)

    start_task >> end_task

if __name__ == '__main__':
    build_data_pipeline()

