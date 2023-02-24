import logging
import os
from kombu import Exchange, Queue

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# 建立一個 Celery 實例，名稱為 core
app = Celery('core')

# 設置 broker 和 backend
app.conf.broker_url = "redis://140.114.30.101:11855/1"
app.conf.result_backend = "redis://140.114.30.101:11855/0"

# 設置時區和序列化方式
app.conf.timezone = "UTC"
app.conf.accept_content = ['application/json']
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'
app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

# 設置要被 celery worker 載入的任務模組
app.conf.imports = ["core.tasks"]

# 設置定時任務
app.conf.beat_schedule = {
    "system-task": {
        "task": "system-hello-celery",
        "schedule": 2.0 # 每兩秒執行一次
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

logger = logging.getLogger('django.celery')

# development
# celery -A core.celery worker -l info -B
# online
# celery -A core.celery worker --loglevel=info
# celery -A core.celery beat -l info