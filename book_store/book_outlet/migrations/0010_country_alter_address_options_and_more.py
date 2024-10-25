# Generated by Django 5.0.3 on 2024-03-30 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book_outlet", "0009_address_author_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=64)),
                ("code", models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name_plural": "Addresses"},
        ),
        migrations.AddField(
            model_name="book",
            name="published_countries",
            field=models.ManyToManyField(to="book_outlet.country"),
        ),
    ]
