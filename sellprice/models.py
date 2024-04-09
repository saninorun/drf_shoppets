from datetime import datetime, timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Q, Max, F

from products.models import Product
from sellprice.managers import DiscountManager


class SellPrice(models.Model):
    product = models.OneToOneField(
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
        ordering = ("product_id", "start_date")
        verbose_name = "Цена номенклатуры"
        verbose_name_plural = "Цены номенклатуры"
        constraints = [
            models.CheckConstraint(
                check=Q(price__gte=0),
                name="price_greater_than_zero",
            ),
            models.UniqueConstraint(
                fields=["product_id", "start_date"], name="unique_sell_price"
            ),
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
    discount_percent = models.IntegerField(
        verbose_name="Скидка в процентах",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True,
    )
    start_date = models.DateField(default=datetime.now, verbose_name="Действует с ")
    end_date = models.DateField(verbose_name="Окончание")

    objects = models.Manager()
    catalog_manager = DiscountManager()

    class Meta:
        ordering = ("product_id", "discount_percent")
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"
        constraints = [
            models.CheckConstraint(
                check=Q(start_date__lte=F("end_date")) & Q(discount_percent__lte=100),
                name="unique_sell_discount",
            ),
            models.UniqueConstraint(
                fields=["product_id", "start_date"],
                name="unique_discount",
            ),
        ]

    def __str__(self):
        return "".join(
            ("в ", str(self.discount_percent), "%", " для ", str(self.product.title))
        )
