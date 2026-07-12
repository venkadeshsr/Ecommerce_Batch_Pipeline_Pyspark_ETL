docker exec -it pipeline_test bash

re-attach to dokcer container

---

Docker Rebuild Comments : docker compose -f docker-compose.yaml up --build -d

Docker Image deletion : docker system prune -a --volumes -f

COmmand to go inside the docker : docker exec -it ETL_Spark /bin/bash

Execution Command : docker exec -it ETL_Spark python /opt/spark/work/etl_script.py
---

Docker image switch

# 1. Force remove the old container that is blocking the name
docker rm -f dynamic_pipeline

# 2. Run your command again to create the fresh container and jump inside
docker run -it --name dynamic_pipeline -v "${PWD}:/opt/spark/work" my_custom_spark:latest bash

---

docker compose down to stop the container

---

Deleting the unused image

docker system prune -a --volumes -f