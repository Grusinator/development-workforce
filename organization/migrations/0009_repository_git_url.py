# Generated by Django 5.0.7 on 2024-07-22 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0008_agent_agent_user_name_agent_organization_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="repository",
            name="git_url",
            field=models.URLField(
                default="https://GrusinatorsAiCorp@dev.azure.com/GrusinatorsAiCorp/TestProject1/_git/test_repo"
            ),
            preserve_default=False,
        ),
    ]