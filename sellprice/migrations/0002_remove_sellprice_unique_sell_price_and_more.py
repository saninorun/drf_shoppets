# Generated by Django 5.0.3 on 2024-04-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("sellprice", "0001_initial"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="sellprice",
            name="unique_sell_price",
        ),
        migrations.AddConstraint(
            model_name="sellprice",
            constraint=models.UniqueConstraint(
                fields=("product_id", "start_date"), name="unique_sell_price"
            ),
        ),
    ]
