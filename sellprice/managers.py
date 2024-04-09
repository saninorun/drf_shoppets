from datetime import datetime

from django.db import models
from django.db.models import F, Sum, Max, Q
from django.db.models.functions import Coalesce


class DiscountManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
        )
