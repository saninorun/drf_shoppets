from collections import OrderedDict
from pytils.translit import slugify
from rest_framework import serializers

from .models import Order, OrderItem


#
#
# class ProductListSerializer(serializers.ListSerializer):
#     def create(self, validated_data: list[OrderedDict]):
#         """
#         Создание поля 'slug' в случае его отсутсвия перед сохранением списка товаров в базу данных.
#         """
#         for product in validated_data:
#             if not product.get('slug', False):
#                 product.update(slug=slugify(product['title']))
#         products = [Product(**item) for item in validated_data]
#         return Product.objects.bulk_create(objs=products)
#
#


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'sell_price', 'discount_price')


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('user', 'time_created', 'time_updated', 'is_paid', 'is_completed', 'orderitems')
        read_only_fields = ('time_created', 'time_updated', 'is_paid', 'is_completed',)
