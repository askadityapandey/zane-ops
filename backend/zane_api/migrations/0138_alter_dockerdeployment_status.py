# Generated by Django 5.0.4 on 2024-07-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zane_api", "0137_alter_gitdeployment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dockerdeployment",
            name="status",
            field=models.CharField(
                choices=[
                    ("QUEUED", "Queued"),
                    ("CANCELLED", "Cancelled"),
                    ("FAILED", "Failed"),
                    ("PREPARING", "Preparing"),
                    ("STARTING", "Starting"),
                    ("RESTARTING", "Restarting"),
                    ("HEALTHY", "Healthy"),
                    ("UNHEALTHY", "Unhealthy"),
                    ("REMOVED", "Removed"),
                    ("SLEEPING", "Sleeping"),
                ],
                default="QUEUED",
                max_length=10,
            ),
        ),
    ]