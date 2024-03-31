from collections import OrderedDict
from pytils.translit import slugify
from rest_framework import serializers

from sellprice.models import SellPrice, SellDiscount


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


class SellPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellPrice
        fields = ('id', 'product', 'price', 'start_date', 'end_date')


class SellDiscountSerializer(serializers.ModelSerializer):

    def validate_discount(self, value):
        """
        Проверяет диапазон допустимых значений для поля 'discount'
        """
        if value < 0 or value > 50:
            raise serializers.ValidationError('Процент скидки должен быть в диапазоне от 0 до 50')
        return value

    class Meta:
        model = SellDiscount
        fields = ('discount', 'product', 'start_date', 'end_date')
        read_only_fields = ('product',)
