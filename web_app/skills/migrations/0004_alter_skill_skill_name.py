# Generated by Django 4.2.3 on 2023-10-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0003_alter_skill_options_skill_skill_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="skill_name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="skill title"
            ),
        ),
    ]