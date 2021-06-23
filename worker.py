from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672',
                    backend="redis://app-redis:6379/0")
logger = get_task_logger(__name__)


@celery_app.task
def add(a, b):
    result = a + b
    logger.info(f"Adding {a} + {b} = {result}")
    return {"result": result}
