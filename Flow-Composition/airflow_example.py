from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, world!")

def build_airflow_example():
    dag = DAG('airflow_example', description='Simple Airflow Example',
              schedule_interval='@daily', start_date=datetime(2022, 1, 1), catchup=False)

    hello_task = PythonOperator(task_id='hello', python_callable=hello_world, dag=dag)
    hello_task

if __name__ == '__main__':
    build_airflow_example()

