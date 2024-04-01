from datetime import datetime, timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q, Max, F
from rest_framework.exceptions import ValidationError

from products.models import Product


class SellPrice(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name="sell_price",
        verbose_name="Товар",
    )
    price = models.PositiveIntegerField(verbose_name="Цена")
    start_date = models.DateField(
        default=datetime.now, verbose_name="Дата начала действия цены"
    )
    end_date = models.DateField(
        null=True, blank=True, verbose_name="Дата окончания действия цены"
    )

    class Meta:
        ordering = ("product", "start_date")
        verbose_name = "Цена номенклатуры"
        verbose_name_plural = "Цены номенклатуры"
        constraints = [
            models.UniqueConstraint(
                fields=["product", "start_date"], name="unique_sell_price"
            )
        ]

    def __str__(self):
        return str(self.price)


class SellDiscount(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.PROTECT,
        related_name="sell_discount",
        verbose_name="Товар",
    )
    discount_procent = models.IntegerField(
        verbose_name="Скидка в процентах",
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        blank=True,
    )
    # discount = models.IntegerField(
    #     verbose_name="Скидка в валюте продажи",
    #     blank=True,
    # )
    start_date = models.DateField(default=datetime.now, verbose_name="Действует с ")
    end_date = models.DateField(verbose_name="Окончание")

    class Meta:
        ordering = ("product", "discount_procent")
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
        constraints = [
            models.CheckConstraint(
                check=Q(start_date__lte=F("end_date")) & Q(discount_procent__lte=100),
                name="unique_sell_discount",
            )
        ]

    def __str__(self):
        return "".join(
            ("в ", str(self.discount_procent), "%", " для ", str(self.product.title))
        )
