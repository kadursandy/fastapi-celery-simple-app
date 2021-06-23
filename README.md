### FastAPI Simple Celery App
##### Demonstrate the use of celery for adding 2 numbers

### View the urls
App url: http://localhost:8081/
Flower url: http://localhost:5555/

```shell
pip install fastapi
pip install celery
pip install uvicorn
pip install flower
pip install redis
pip freeze > requirements.txt
docker build -t kadursandy/fastapi-celery-simple-app:latest .
docker login
docker push kadursandy/fastapi-celery-simple-app:latest
docker-compose up -d
```