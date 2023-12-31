# Generated by Django 4.2.2 on 2023-06-28 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_rename_name_commandants_first_name_and_more"),
        ("main", "0016_dormitory_student_alter_statement_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="dormitory",
            name="commandant",
            field=models.ManyToManyField(to="users.commandants"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 6, 28, 13, 15, 30, 68955, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата отправки",
            ),
        ),
    ]
