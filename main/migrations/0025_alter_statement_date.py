# Generated by Django 4.2.2 on 2023-06-28 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0024_alter_statement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 6, 28, 16, 59, 4, 905723, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата отправки",
            ),
        ),
    ]
