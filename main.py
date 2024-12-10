from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def job_start():
    print("Iniciando job")

with DAG(dag_id="Iniciando_job_dag",
         start_date=datetime(2024,3,24),
         schedule_interval="* * * * *",
         catchup=False) as dag:

     task1 = PythonOperator(
            task_id="Job_01",
            python_callable=job_start)        
        
