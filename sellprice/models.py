from datetime import datetime, timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

from products.models import Product


class SellPrice(models.Model):
    product = models.ForeignKey(to=Product,
                                on_delete=models.PROTECT,
                                related_name='sell_price',
                                verbose_name='Товар'
                                )
    price = models.PositiveIntegerField(verbose_name='Цена')
    start_date = models.DateField(default=datetime.now, verbose_name='Дата начала действия цены')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания действия цены')

    class Meta:
        ordering = ('product', 'start_date')
        verbose_name = 'Цена номенклатуры'
        verbose_name_plural = 'Цены номенклатуры'

    def __str__(self):
        return str(self.price)


class SellDiscount(models.Model):
    product = models.ForeignKey(to=Product,
                                on_delete=models.PROTECT,
                                related_name='sell_discount',
                                verbose_name='Товар'
                                )
    discount = models.IntegerField(verbose_name='Скидка в процентах',
                                   validators=[MinValueValidator(0), MaxValueValidator(50)]
                                   )
    start_date = models.DateField(default=datetime.now, verbose_name='Действует с ')
    end_date = models.DateField(verbose_name='Окончание')

    class Meta:
        ordering = ('product', 'discount')
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return ''.join(('в ', str(self.discount), '%', ' для ', str(self.product.title)))
