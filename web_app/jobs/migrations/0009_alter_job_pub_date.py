# Generated by Django 4.2.3 on 2023-10-22 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0008_alter_job_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="pub_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 10, 22, 17, 46, 21, 719533, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
