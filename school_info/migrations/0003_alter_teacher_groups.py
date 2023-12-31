# Generated by Django 4.2.5 on 2023-10-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school_info", "0002_alter_student_group_alter_teacher_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="groups",
            field=models.ManyToManyField(
                related_name="teacher", to="school_info.group"
            ),
        ),
    ]
