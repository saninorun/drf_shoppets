# Generated by Django 5.0.3 on 2024-04-09 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("sellprice", "0003_alter_selldiscount_options_alter_sellprice_options"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="selldiscount",
            name="unique_discount",
        ),
        migrations.AlterField(
            model_name="sellprice",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sell_price",
                to="products.product",
                verbose_name="Товар",
            ),
        ),
        migrations.AddConstraint(
            model_name="selldiscount",
            constraint=models.UniqueConstraint(
                fields=("product_id", "start_date"), name="unique_discount"
            ),
        ),
    ]