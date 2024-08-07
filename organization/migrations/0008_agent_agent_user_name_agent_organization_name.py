# Generated by Django 5.0.7 on 2024-07-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0007_agent_ado_task_id_agent_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="agent_user_name",
            field=models.CharField(default="William Sandvej Hansen", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="agent",
            name="organization_name",
            field=models.CharField(default="GrusinatorsAiCorp", max_length=128),
            preserve_default=False,
        ),
    ]
