from decimal import Decimal

from django.contrib import admin

from orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'time_created', 'time_updated', 'is_completed', 'is_paid')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'sell_price', 'discount_price', 'total_price')
    list_display_links = ('product',)
    list_editable = ('quantity',)

    def total_price(self, obj: OrderItem) -> Decimal:
        """
            Подсчитывает вычисляемое поле суммарной стоимости
            для каждого товара в заказе и отображает в админпанели
        """
        total_price_obj = (obj.discount_price if obj.discount_price else obj.sell_price) * obj.quantity
        return total_price_obj
