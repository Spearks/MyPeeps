# Generated by Django 4.2.5 on 2023-10-08 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Peeps",
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
                ("name", models.CharField(max_length=16, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("seed", models.IntegerField(blank=True, editable=False, unique=True)),
                ("age", models.SmallIntegerField(default=0, editable=False)),
                ("attribute_hp", models.SmallIntegerField(default=100, editable=False)),
                ("attribute_creativity", models.FloatField(default=0)),
                ("attribute_romance", models.FloatField(default=0)),
                ("attribute_happiness", models.FloatField(default=0)),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="users", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PeepsMetric",
            fields=[
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("action", models.CharField(max_length=255)),
                ("attribute_hp", models.IntegerField()),
                ("attribute_creativity", models.FloatField()),
                ("attribute_romance", models.FloatField()),
                (
                    "peep",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.peeps"
                    ),
                ),
            ],
        ),
    ]
