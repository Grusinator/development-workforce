# Generated by Django 5.0.7 on 2024-07-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0005_alter_project_id_alter_repository_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="agentrepoconnection",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
