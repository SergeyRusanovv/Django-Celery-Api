from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Task


@receiver(post_delete, sender=Task)
def increment_executor_tasks_count(sender, instance, **kwargs):
    instance.executor.remote_tasks_count += 1
    instance.executor.save()
