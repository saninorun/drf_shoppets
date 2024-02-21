from decimal import Decimal

from django.contrib import admin

from orders.models import SellOrder, SellOrderItem


@admin.register(SellOrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    model = SellOrderItem
    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",
        "discount_price",
        "total_price",
    )
    list_display_links = ("product",)
    list_editable = ("quantity",)

    @admin.display(description="Итого")
    def total_price(self, obj: SellOrderItem) -> Decimal:
        """
        Подсчитывает вычисляемое поле суммарной стоимости
        для каждого товара в заказе и отображает в админпанели
        """
        total_price_obj = (
            obj.discount_price if obj.discount_price else obj.price
        ) * obj.quantity
        return total_price_obj


@admin.register(SellOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "time_created",
        "time_updated",
        "is_completed",
        "is_paid",
    )
    # inlines = [
    #     OrderItemAdmin,
    # ]
