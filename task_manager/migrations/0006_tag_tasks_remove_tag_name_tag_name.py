# Generated by Django 4.2.1 on 2023-05-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0005_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="tasks",
            field=models.ManyToManyField(
                default=None, null=True, related_name="tags", to="task_manager.task"
            ),
        ),
        migrations.RemoveField(
            model_name="tag",
            name="name",
        ),
        migrations.AddField(
            model_name="tag",
            name="name",
            field=models.CharField(default=None, max_length=64, unique=True),
        ),
    ]
