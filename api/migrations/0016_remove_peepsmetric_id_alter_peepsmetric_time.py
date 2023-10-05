# Generated by Django 4.2.5 on 2023-10-05 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0015_peepsmetric"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="peepsmetric",
            name="id",
        ),
        migrations.AlterField(
            model_name="peepsmetric",
            name="time",
            field=models.DateTimeField(
                auto_now_add=True, db_index=True, primary_key=True, serialize=False
            ),
        ),
    ]
