# Generated by Django 5.0.6 on 2024-06-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
