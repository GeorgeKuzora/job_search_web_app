# Generated by Django 4.2.3 on 2023-10-14 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("skills", "0003_alter_skill_options_skill_skill_description_and_more"),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=20, verbose_name="login name"),
                ),
                ("name", models.CharField(max_length=20, verbose_name="user name")),
                (
                    "lastname",
                    models.CharField(max_length=30, verbose_name="user lastname"),
                ),
                (
                    "parentname",
                    models.CharField(max_length=20, verbose_name="user parent name"),
                ),
                ("birthdate", models.DateField()),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="user email"
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=20, verbose_name="user password"),
                ),
                (
                    "registration_date",
                    models.DateField(
                        default=datetime.datetime(
                            2023,
                            10,
                            14,
                            15,
                            59,
                            46,
                            567938,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=12, verbose_name="company phone"),
                ),
                (
                    "address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="companies.address",
                        verbose_name="address",
                    ),
                ),
                ("skills", models.ManyToManyField(to="skills.skill")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]