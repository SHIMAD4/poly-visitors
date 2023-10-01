# Generated by Django 4.2.2 on 2023-06-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_students"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commandants",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=40, verbose_name="Фамилия")),
            ],
            options={
                "verbose_name": "Комендант",
                "verbose_name_plural": "Коменданты",
            },
        ),
    ]
