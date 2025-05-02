FROM apache/airflow:2.8.1-python3.10

USER root
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

USER airflow

COPY ./airflow/dags /opt/airflow/dags
COPY ./etl/scripts /opt/airflow/etl/scripts
COPY requirements.txt /opt/airflow/requirements.txt

# 👇 Add these lines to install compatible providers
RUN pip install --no-cache-dir apache-airflow-providers-common-io==1.2.0

# Maintain path and install other deps
ENV PYTHONPATH='/opt/airflow:/opt/airflow/dags:$PYTHONPATH'
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt