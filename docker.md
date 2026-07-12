docker exec -it pipeline_test bash

re-attach to dokcer container

---

For line the containser direlcyt into my local project : docker run -it --name dynamic_pipeline -v "${PWD}:/opt/spark/work" my_custom_spark:latest bash

Docker Rebuild Comments : docker build -t my_custom_spark:latest .

---

Docker image switch

# 1. Force remove the old container that is blocking the name
docker rm -f dynamic_pipeline

# 2. Run your command again to create the fresh container and jump inside
docker run -it --name dynamic_pipeline -v "${PWD}:/opt/spark/work" my_custom_spark:latest bash