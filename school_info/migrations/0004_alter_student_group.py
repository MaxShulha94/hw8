# Generated by Django 4.2.5 on 2023-10-12 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school_info", "0003_alter_teacher_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="group",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to="school_info.group",
            ),
        ),
    ]
