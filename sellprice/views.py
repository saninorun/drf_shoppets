from datetime import datetime

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from sellprice.models import SellPrice, SellDiscount
from sellprice.serializers import SellPriceSerializer, SellDiscountSerializer


class SellPriceView(viewsets.ModelViewSet):
    queryset = SellPrice.objects.all()
    serializer_class = SellPriceSerializer


class SellDiscountView(viewsets.ModelViewSet):
    queryset = SellDiscount.objects.all()
    serializer_class = SellDiscountSerializer
