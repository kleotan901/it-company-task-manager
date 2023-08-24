# Generated by Django 4.2.1 on 2023-05-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0004_task_is_completed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.ManyToManyField(
                        default=None,
                        null=True,
                        related_name="tags",
                        to="task_manager.task",
                    ),
                ),
            ],
        ),
    ]
