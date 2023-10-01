# Generated by Django 4.2.2 on 2023-06-28 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_dormitory_commandant_alter_statement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 6, 28, 15, 0, 23, 861929, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата отправки",
            ),
        ),
    ]
