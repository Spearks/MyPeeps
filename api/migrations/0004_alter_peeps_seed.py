# Generated by Django 4.2.5 on 2023-10-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_peeps_seed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="peeps",
            name="seed",
            field=models.IntegerField(blank=True, editable=False, unique=True),
        ),
    ]
