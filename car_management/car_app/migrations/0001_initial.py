# Generated by Django 4.2.2 on 2023-06-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("model", models.CharField(max_length=100)),
                ("brand", models.CharField(max_length=100)),
                ("main_color", models.CharField(max_length=100)),
                ("value", models.IntegerField()),
                ("production_costs", models.IntegerField()),
                ("transportation_costs", models.IntegerField()),
            ],
        ),
    ]
