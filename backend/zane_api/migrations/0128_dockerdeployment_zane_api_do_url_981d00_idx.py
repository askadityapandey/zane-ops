# Generated by Django 5.0.4 on 2024-06-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ("django_celery_beat", "0018_improve_crontab_helptext"),
        ("zane_api", "0127_alter_dockerdeployment_options"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="dockerdeployment",
            index=models.Index(fields=["url"], name="zane_api_do_url_981d00_idx"),
        ),
    ]
