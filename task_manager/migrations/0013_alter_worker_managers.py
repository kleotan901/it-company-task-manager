# Generated by Django 4.2.1 on 2023-05-30 22:32

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0012_alter_worker_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="worker",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
