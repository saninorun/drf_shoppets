from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

from products.models import Product

User = get_user_model()


class Order(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        verbose_name="Пользователь",
    )
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    time_updated = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_completed = models.BooleanField(default=False, verbose_name="Статус исполнения")
    is_paid = models.BooleanField(default=False, verbose_name="Статус оплаты")

    class Meta:
        abstract = True
        ordering = ("user",)

    def __str__(self):
        return f"№ {self.id}"


class OrderItem(models.Model):

    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name="%(class)s",
        verbose_name="Товар",
    )
    price = models.DecimalField(
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
        abstract = True
        ordering = ("product",)
        verbose_name = "Составляющие заказа"
        verbose_name_plural = "Составляющие заказа"

    def __str__(self):
        return f"{self.product.title}"
