from django.db import models
from django.db.models import F, Sum
from django.db.models.functions import Coalesce


# class OrderManager(models.Manager):
#     def total_price_order(self):
#         return self.annotate(
#             total_price_order=Sum(
#                 Coalesce(F("sellorderitems__discount_price"), F("sellorderitems__price"))
#                 * F("sellorderitems__quantity")
#             )
#         )
