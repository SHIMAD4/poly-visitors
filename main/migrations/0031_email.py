# Generated by Django 3.2.25 on 2024-06-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_historicalstatement_draft_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('recipient', models.EmailField(max_length=254)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]