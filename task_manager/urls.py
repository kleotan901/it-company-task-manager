from django.contrib import admin
from django.urls import path

from task_manager.views import index, TaskListView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
]

app_name = "task_manager"
