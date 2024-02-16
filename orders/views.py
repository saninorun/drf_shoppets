from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Order
from .serializers import OrderSerializer


# region api_documentation
@extend_schema(tags=["Заказы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список заказов",
    ),
    update=extend_schema(
        summary="Изменение существующего заказа",
    ),
    create=extend_schema(
        summary="Создание нового заказа",
    ),
    retrieve=extend_schema(summary="Получение конкретного заказа"),
    destroy=extend_schema(summary="Удаление конкретного заказа"),
)
# endregion
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'orders/product_list.html'
    permission_classes = (IsAuthenticated,)
