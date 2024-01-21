# Generated by Django 4.1.13 on 2024-01-21 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="store",
        ),
        migrations.CreateModel(
            name="Price",
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
                ("date", models.DateField()),
                ("value", models.FloatField()),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.store"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.price"
            ),
        ),
    ]
