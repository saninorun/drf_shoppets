# from collections import OrderedDict
# from pytils.translit import slugify
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from products.models import Product


class CatalogSerializer(serializers.ModelSerializer):
    price_item = serializers.IntegerField(label="Цена товара")
    discount_item = serializers.IntegerField(label="Скидка", allow_null=True, default=0)

    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "accounting_unit",
            "manufacturer",
            "categories",
            "slug",
            "article_number",
            "price_item",
            "discount_item",
        )
        read_only_fields = ("slug",)
