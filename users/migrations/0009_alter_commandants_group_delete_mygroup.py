# Generated by Django 4.2.2 on 2023-06-28 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0008_alter_commandants_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commandants",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="auth.group",
            ),
        ),
        migrations.DeleteModel(
            name="MyGroup",
        ),
    ]
