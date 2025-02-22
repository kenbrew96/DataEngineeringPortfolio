from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def extract():
    df = pd.read_json("student_enrollment_data.json")
    return df

def transform(df):
    df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])
    return df

def load(df):
    conn = psycopg2.connect("dbname=school user=admin password=secret")
    df.to_sql("students", conn, if_exists='replace', index=False)
    conn.close()

def etl():
    df = extract()
    df = transform(df)
    load(df)
