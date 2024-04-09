from collections import OrderedDict
from pytils.translit import slugify
from rest_framework import serializers

from .models import SellOrder, SellOrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOrderItem
        fields = ("product", "quantity", "price", "discount_price")


class OrderSerializer(serializers.ModelSerializer):
    sellorderitems = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = SellOrder
        fields = (
            "user",
            "time_created",
            "time_updated",
            "is_paid",
            "is_completed",
            "sellorderitems",
        )
        read_only_fields = (
            "time_created",
            "time_updated",
            "is_paid",
            "is_completed",
        )
        depth = 1
