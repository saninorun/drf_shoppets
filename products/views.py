from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, viewsets, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
    renderer_classes,
)
from rest_framework.generics import CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework import generics
from rest_framework.renderers import (
    JSONRenderer,
    TemplateHTMLRenderer,
    BrowsableAPIRenderer,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


# region api_documentation
@extend_schema(tags=["Товары"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список Товаров",
        description="Получить список всех товаров в справочнике",
    ),
    update=extend_schema(
        summary="Изменение существующего товара",
    ),
    create=extend_schema(
        summary="Добавленеи нового товара в справочник",
        description="Добавить в справочник новый товар",
    ),
    retrieve=extend_schema(summary="Получение конкретного товара"),
    destroy=extend_schema(summary="Удаление конкретного товара"),
)
# endregion
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("categories").all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


# region api_documentation
@extend_schema(tags=["Категории"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список всех категорий",
    ),
    update=extend_schema(
        summary="Изменение существующей категории",
    ),
    create=extend_schema(
        summary="Добавленеи новой категории",
    ),
    retrieve=extend_schema(summary="Получение конкретной категории"),
    destroy=extend_schema(summary="Удаление категории"),
)
# endregion
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


# @api_view(['GET', 'POST'])
# # @authentication_classes([JWTAuthentication, SessionAuthentication, BasicAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated, ])
# # @renderer_classes([TemplateHTMLRenderer])
# def list_add_products(request: HttpRequest | Request) -> Response:
#     if request.method == 'GET':
#         products = Product.objects.all().select_related('categories')
#         serializer = ProductSerializer(products, many=True)
#         return Response(data=serializer.data,
#                         # template_name='product/product_list.html',
#                         status=status.HTTP_200_OK)
#
#     if request.method == 'POST':
#         serializer = ProductSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#

# @api_view(['GET', 'PUT'])
# # @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly, ])
# def get_update_product(request: HttpRequest | Request, slug: str = None) -> Response:
#     if request.method == 'GET':
#         product = get_object_or_404(Product, slug=slug)
#         serializer = ProductSerializer(product)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         product = get_object_or_404(Product, slug=slug)
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsAuthenticated,)
#     # renderer_classes = [JSONRenderer]
#
#
# class CategoryView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsAuthenticated,)
#     lookup_field = 'slug'
