http://localhost:8080 - Local host used for airflow

Aifrlow setup 

# 1. Force remove the old container blocking the name
docker rm -f dynamic_pipeline

# 2. Start your Docker Compose setup again
docker compose up -d

----

Airflow password seeing

docker exec -it airflow_scheduler cat /opt/airflow/standalone_admin_password.txt

---

DAG Sync immediately

docker exec -it Airflow airflow dags reserialize