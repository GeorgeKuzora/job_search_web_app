# Generated by Django 4.2.3 on 2023-10-14 11:25

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0001_initial"),
        ("jobs", "0003_job_skills_delete_jobskills"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="companies.address",
                verbose_name="address",
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="companies.company",
                verbose_name="company",
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="is_archived",
            field=models.BooleanField(default=False, verbose_name="is archived"),
        ),
        migrations.AddField(
            model_name="job",
            name="max_salary",
            field=models.IntegerField(null=True, verbose_name="maximum salary"),
        ),
        migrations.AddField(
            model_name="job",
            name="min_salary",
            field=models.IntegerField(
                null=True,
                validators=[django.core.validators.MinValueValidator(limit_value=0)],
                verbose_name="minimum salary",
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="pub_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 10, 14, 11, 25, 14, 57702, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="job",
            name="required_experience",
            field=models.CharField(
                blank=True,
                choices=[
                    ("WITHOUT", "Without"),
                    ("1-3YEARS", "Upto3Years"),
                    ("3-6YEARS", "Upto6Years"),
                    ("6-9YEARS", "Upto9Years"),
                    ("9-12YEARS", "Upto12Years"),
                ],
                max_length=11,
                verbose_name="required experience",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_description",
            field=models.TextField(verbose_name="job description"),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_name",
            field=models.CharField(max_length=100, verbose_name="job title"),
        ),
    ]
