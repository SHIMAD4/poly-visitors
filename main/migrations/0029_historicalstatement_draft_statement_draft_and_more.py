# Generated by Django 4.2 on 2024-06-11 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0028_alter_statement_date_alter_visithistory_statement_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalstatement",
            name="draft",
            field=models.BooleanField(default=False, verbose_name="Черновик"),
        ),
        migrations.AddField(
            model_name="statement",
            name="draft",
            field=models.BooleanField(default=False, verbose_name="Черновик"),
        ),
        migrations.AlterField(
            model_name="historicalstatement",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Дата отправки"
            ),
        ),
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Дата отправки"
            ),
        ),
    ]