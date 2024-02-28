from django.db import models


class Executor(models.Model):
    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    name = models.CharField(max_length=50, verbose_name="Имя исполнителя")
    remote_tasks_count = models.IntegerField(default=0, verbose_name="Количество удаленных задач")


class Project(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    name = models.CharField(max_length=50, verbose_name="Название проекта")


class Priority(models.IntegerChoices):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Task(models.Model):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    deadline = models.DateTimeField(verbose_name="Дата окончания задачи")
    executor = models.ForeignKey(
        to=Executor,
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name="Исполнитель"
    )
    priority = models.IntegerField(choices=Priority.choices)
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    comment = models.TextField()
    projects = models.ManyToManyField(to=Project, related_name="tasks")
