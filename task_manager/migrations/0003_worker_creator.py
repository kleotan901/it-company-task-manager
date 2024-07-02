# Generated by Django 4.2.2 on 2024-07-02 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0002_tag_task_is_completed_task_slug_worker_slug_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="worker",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_workers",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
