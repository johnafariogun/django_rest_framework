# Generated by Django 4.1.1 on 2023-03-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=10, max_digits=8),
        ),
    ]
