docker exec -it pipeline_test bash

re-attach to dokcer container

---

For line the containser direlcyt into my local project : docker run -it --name dynamic_pipeline -v "${PWD}:/opt/spark/work" my_custom_spark:latest bash