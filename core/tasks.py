
import json
from core import celery_logger
from celery import shared_task

@shared_task(name="system-hello-celery")
def hello_celery():
    celery_logger.info("HELLO Celery")