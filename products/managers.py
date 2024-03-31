from datetime import datetime

from django.db import models
from django.db.models import F, Sum, Max
from django.db.models.functions import Coalesce


class CatalogManager(models.Manager):
    def actual_date_price(self):
        """
        Возвращает список/[] (list) дат для действующей актуальной цены на товар в разрезе текущего времени,
        прописанной в справочнике цен (модель SellPrice).
        """
        return (
            self.filter(sell_price__start_date__lte=datetime.now())
            .annotate(start_date=Max("sell_price__start_date"))
            .values_list("start_date", flat=True)
        )

    def actual_price(self):
        """
        Возвращает QuerySet с добавленным аннотированным полем "price_item",
        в котором содержится значение актуальной цены на товар для текущего времени.
        """
        actual_date_price = self.actual_date_price()

        return self.filter(sell_price__start_date__in=actual_date_price).annotate(
            price_item=F("sell_price__price")
        )
