# Generated by Django 5.0.1 on 2024-01-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeStatus",
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
                ("on", models.BooleanField()),
                ("sent_at", models.DateTimeField()),
                ("recieved_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Home Statuses",
            },
        ),
    ]
