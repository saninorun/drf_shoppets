from datetime import datetime

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from sellprice.models import SellPrice
from sellprice.serializers import SellPriceSerializer


class SellPriceListView(viewsets.ModelViewSet):
    queryset = SellPrice.objects.filter(start_date__gte=datetime.now())
    serializer_class = SellPriceSerializer

