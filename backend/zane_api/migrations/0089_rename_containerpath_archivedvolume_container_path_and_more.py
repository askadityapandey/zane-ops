# Generated by Django 5.0.4 on 2024-05-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zane_api", "0088_volume_zane_api_vo_host_pa_25c9d1_idx"),
    ]

    operations = [
        migrations.RenameField(
            model_name="archivedvolume",
            old_name="containerPath",
            new_name="container_path",
        ),
        migrations.AddField(
            model_name="archivedvolume",
            name="host_path",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
