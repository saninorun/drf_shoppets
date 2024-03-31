from collections import OrderedDict
from pytils.translit import slugify
from rest_framework import serializers

from products.models import Product, Category


class ProductListSerializer(serializers.ListSerializer):
    def create(self, validated_data: list[OrderedDict]):
        """
        Создание поля 'slug' в случае его отсутствия перед сохранением списка товаров в базу данных.
        """
        for product in validated_data:
            if not product.get("slug", False):
                product.update(slug=slugify(product["title"]))
        products = [Product(**item) for item in validated_data]
        return Product.objects.bulk_create(objs=products)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("title", "description", "image", "slug")


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(source="price_item", read_only=True)
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
            "price",
        )
        read_only_fields = ("slug",)
        # depth = 1
        list_serializer_class = ProductListSerializer
