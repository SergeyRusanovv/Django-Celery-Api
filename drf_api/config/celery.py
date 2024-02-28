import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("my_api")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "delete-expired-tasks-every-day": {
        "task": "my_api.tasks.delete_expired_tasks",
        "schedule": crontab(hour="*/24"),
    },
}
