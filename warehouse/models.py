from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


class WarehouseOrder(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, related_name='WarehouseOrder')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

    def __str__(self):
        return f'Поставка №{self.id}'


class WarehouseOrderItem(models.Model):
    warehouseorder = models.ForeignKey(to=WarehouseOrder, on_delete=models.CASCADE,
                                       related_name='warehouseorderitems',
                                       verbose_name='Поставка номер')
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT, related_name='warehouseorderitem',
                                verbose_name='Товар')
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена покупки')
    quantity = models.IntegerField(default=1, verbose_name='Количество')

    class Meta:
        ordering = ('product',)
        verbose_name = 'Поставленный продукт'
        verbose_name_plural = 'Поставленные продукты'

    def __str__(self):
        return f'{self.product.title}'
