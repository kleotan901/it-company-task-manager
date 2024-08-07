from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, default=None, null=True
    )
    slug = models.SlugField(max_length=50, blank=True, allow_unicode=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.position})"

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"slug": self.slug})


class TaskType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, default=None)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent and important", "Urgent and important"),
        ("High priority", "High priority"),
        ("Medium priority", "Medium priority"),
        ("Low priority", "Low priority"),
    ]
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_tasks",
    )
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")
    tags = models.ManyToManyField(Tag, related_name="tasks", default=None, blank=True)
    slug = models.SlugField(max_length=50, blank=True, allow_unicode=True)

    def __str__(self):
        return f"{self.name} {self.deadline}"

    def get_absolute_url(self):
        return reverse("task_manager:task-detail", kwargs={"slug": self.slug})
