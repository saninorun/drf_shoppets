from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    TYPE_ORDER_CHOICES = {
        "SELL_ORDER": "SELL_ORDER",
        "BUY_ORDER": "BUY_ORDER",
    }
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="order",
        verbose_name="Пользователь",
    )
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_completed = models.BooleanField(default=False, verbose_name="Статус исполнения")
    is_paid = models.BooleanField(default=False, verbose_name="Статус оплаты")
    type_order = models.CharField(
        max_length=10, verbose_name="Тип заказа", choices=TYPE_ORDER_CHOICES
    )

    class Meta:
        ordering = ("user",)
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"№ {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name="orderitems",
        verbose_name="Номер заказа",
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name="orderitems",
        verbose_name="Товар",
    )
    sell_price = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Цена за штуку"
    )
    discount_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name="Цена с учетом скидки",
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(default=1, verbose_name="Количество")

    class Meta:
        ordering = ("product",)
        verbose_name = "Составляющие заказа"
        verbose_name_plural = "Составляющие заказа"

    def __str__(self):
        return f"{self.product.title}"
