# Generated by Django 5.0.7 on 2024-08-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0020_agenttask_agent"),
    ]

    operations = [
        migrations.AddField(
            model_name="workitem",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="workitem",
            name="title",
            field=models.CharField(default="test title", max_length=255),
            preserve_default=False,
        ),
    ]
