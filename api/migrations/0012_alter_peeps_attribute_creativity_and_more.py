# Generated by Django 4.2.5 on 2023-10-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0011_alter_peeps_attribute_creativity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="peeps",
            name="attribute_creativity",
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="peeps",
            name="attribute_romance",
            field=models.SmallIntegerField(blank=True),
        ),
    ]