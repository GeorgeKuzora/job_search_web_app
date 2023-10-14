# Generated by Django 4.2.3 on 2023-10-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0002_remove_skill_id_alter_skill_skill_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="skill",
            options={
                "ordering": ["skill_name"],
                "verbose_name": "skill",
                "verbose_name_plural": "skills",
            },
        ),
        migrations.AddField(
            model_name="skill",
            name="skill_description",
            field=models.TextField(
                blank=True, null=True, verbose_name="skill description"
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skill_name",
            field=models.CharField(
                max_length=50,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="skill title",
            ),
        ),
    ]
