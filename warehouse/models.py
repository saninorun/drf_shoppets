from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class Warehouse(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name="warehouse",
        verbose_name="Товар",
    )
    in_stock = models.IntegerField(default=0, verbose_name="Количество на складе")
    quantity_shipment = models.PositiveIntegerField(
        verbose_name="Всего поставленно на склад"
    )
    quantity_selling = models.PositiveIntegerField(
        verbose_name="Всего оплаченных продаж"
    )

    def __str__(self):
        return f"{self.product}"
