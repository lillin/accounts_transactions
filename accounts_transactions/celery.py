from __future__ import absolute_import
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accounts_transactions.settings')

celery_website = Celery('website')
celery_website.config_from_object('django.conf:settings', namespace='CELERY')

celery_website.conf.task_routes = (
    [
        ('website.tasks.create_transaction', {'queue': 'create_transaction'}),
     ],
)

celery_website.autodiscover_tasks()
