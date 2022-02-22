from datetime import timedelta, datetime
import json
import requests
import re
import gcsfs
import os
import zlib
# import time

from google.cloud import secretmanager_v1
import google.auth

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.gcs_delete_operator import GoogleCloudStorageDeleteOperator
from airflow.contrib.operators.bigquery_table_delete_operator import BigQueryTableDeleteOperator
from airflow.hooks.base_hook import BaseHook
from airflow.utils.trigger_rule import TriggerRule
from dataplatform.mux_integration.helper import custom_func
from airflow import configuration

# ================================================================================
# environment setting
# ================================================================================
sparrow_env = Variable.get("env")
if sparrow_env == "unittest_env":
    prefix_dir = "/workspace/"
    env = "staging_env"
else:
    prefix_dir = configuration.get('core', 'dags_folder')
    env = sparrow_env

# ================================================================================
# custom functions
# ================================================================================

def func():
    pass


# ================================================================================
# airflow arguments
# ================================================================================
args = {
    'owner': 'tdg_dp',
    'depends_on_past': False,
    'email': ['myemail@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(hours=2),
    'start_date': datetime(2021, 6, 20),
}

if env == "production_env":
    sched = "0 12 * * *" 
else:
    sched = "0 12 * * *" 

dag_name = "sample_dag"
job_start_date = datetime.now()
dag = DAG(dag_name, schedule_interval=sched, catchup = False, default_args = args)

# ================================================================================
# main function
# ================================================================================
def main():
    pass

main()