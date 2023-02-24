from __future__ import absolute_import
from core.celery import app as celery_app, logger as celery_logger

__all__ = ('celery_app', 'celery_logger',)