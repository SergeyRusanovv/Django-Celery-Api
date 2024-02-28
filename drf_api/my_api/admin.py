from django.contrib import admin
from .models import Executor, Project, Task


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = "name", "remote_tasks_count"
    list_display_links = "name", "remote_tasks_count"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "name",
    list_display_links = "name",


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "created_date", "deadline", "executor",
        "priority", "title", "comment"
    )
    list_display_links = (
        "created_date", "deadline", "executor",
        "priority", "title", "comment"
    )
