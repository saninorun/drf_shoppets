from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

from orders import abstractmodels

from products.models import Product


class SellOrder(abstractmodels.Order):

    class Meta(abstractmodels.Order.Meta):
        verbose_name = "Заказ на продажу"
        verbose_name_plural = "Заказы на продажу"

    def __str__(self):
        return f"Продажа № {self.id}"


class SellOrderItem(abstractmodels.OrderItem):
    order = models.ForeignKey(
        to=SellOrder,
        on_delete=models.CASCADE,
        related_name="sellorderitems",
        verbose_name="Номер заказа",
    )

    class Meta(abstractmodels.OrderItem.Meta):
        constraints = [
            models.CheckConstraint(
                check=(Q(quantity__gte=0) & Q(discount_price__gte=0) & Q(price__gte=0)),
                name="check_item",
            ),
        ]

    def __str__(self):
        return f"{self.product.title}"


class BuyOrder(abstractmodels.Order):

    supplier = models.CharField(max_length=250, verbose_name="Поставщик", unique=True)

    class Meta(abstractmodels.Order.Meta):
        ordering = ("supplier", "time_created")
        verbose_name = "Заказ на поставку"
        verbose_name_plural = "Заказы на поставку"

    def __str__(self):
        return f"Поставка № {self.id}"


class BuyOrderItem(abstractmodels.OrderItem):
    order = models.ForeignKey(
        to=BuyOrder,
        on_delete=models.CASCADE,
        related_name="buyorderitem",
        verbose_name="Номер заказа",
    )

    class Meta(SellOrderItem.Meta):
        pass
