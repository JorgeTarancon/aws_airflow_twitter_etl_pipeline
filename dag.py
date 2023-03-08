###### LIBRARIES ######
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from twitter_processor_without_classes import run_twitter_etl
###### LIBRARIES ######

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,2,14),
    'email': ['si.jorgetarancon@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='A simple DAG to extract tweets from Twitter'#,
    #schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='twitter_etl_pipeline',
    python_callable=run_twitter_etl,
    dag=dag,
)

run_etl