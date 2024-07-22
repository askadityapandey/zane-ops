# Generated by Django 5.0.4 on 2024-07-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zane_api", "0141_alter_httplog_request_id"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="httplog",
            index=models.Index(
                fields=["request_method"], name="zane_api_ht_request_5fa6b3_idx"
            ),
        ),
    ]
