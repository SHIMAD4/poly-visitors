# Generated by Django 4.2.2 on 2023-06-21 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 6, 21, 12, 17, 8, 762012, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата отправки",
            ),
        ),
    ]
