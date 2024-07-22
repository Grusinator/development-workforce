# Generated by Django 5.0.7 on 2024-07-22 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0003_remove_project_organization_delete_organization"),
    ]

    operations = [
        migrations.CreateModel(
            name="AgentRepoConnection",
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
                ("enabled", models.BooleanField(default=False)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.agent",
                    ),
                ),
                (
                    "repository",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organization.repository",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="AgentWorkPermit",
        ),
    ]