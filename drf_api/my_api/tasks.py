from datetime import datetime, timedelta
from django.db import transaction
from config.celery import app
from .models import Task


@app.task
def delete_expired_tasks():
    expired_tasks = Task.objects.filter(deadline__lt=datetime.now() - timedelta(days=1))
    with transaction.atomic():
        for task in expired_tasks:
            task.executor.remote_tasks_count += 1
            task.executor.save()
            task.delete()
