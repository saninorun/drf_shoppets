from django.contrib import admin

from sellprice.models import SellPrice, SellDiscount


@admin.register(SellPrice)
class SellPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price',)


@admin.register(SellDiscount)
class SellDiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_percent', 'product', 'start_date', 'end_date')
