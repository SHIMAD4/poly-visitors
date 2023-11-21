# Generated by Django 4.2 on 2023-11-21 17:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0027_visithistory_day_of_visit_alter_statement_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="statement",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 11, 21, 17, 54, 34, 261460, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата отправки",
            ),
        ),
        migrations.AlterField(
            model_name="visithistory",
            name="statement",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="main.statement",
            ),
        ),
        migrations.CreateModel(
            name="HistoricalVisitHistory",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("day_of_visit", models.DateField(verbose_name="Дата посещения")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "statement",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="main.statement",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical История посещения",
                "verbose_name_plural": "historical История посещений",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalStatement",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=30, verbose_name="Название")),
                (
                    "payment",
                    models.BooleanField(default=False, verbose_name="Оплата общежития"),
                ),
                (
                    "status",
                    models.CharField(
                        default="Отправлено", max_length=30, verbose_name="Статус"
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=datetime.datetime(
                            2023,
                            11,
                            21,
                            17,
                            54,
                            34,
                            261460,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="Дата отправки",
                    ),
                ),
                (
                    "file",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Файл заявления",
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Заявление",
                "verbose_name_plural": "historical Заявления",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDormitory",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=30, verbose_name="Номер")),
                ("street", models.CharField(max_length=250, verbose_name="Адрес")),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Общежитие",
                "verbose_name_plural": "historical Общежития",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
