# Generated by Django 4.2.3 on 2023-10-14 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0005_alter_job_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="pub_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 10, 14, 16, 5, 34, 475481, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
