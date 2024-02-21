from django.db import models
from django.db.models import F, Sum


class OrderManager(models.Manager):
    def total_price_order(self):
        return self.annotate(
            total_price_orderitem=(F("price") * F("quantity"))
        ).aggregate(total_price_order=Sum("total_price_orderitem"))
