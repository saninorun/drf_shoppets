from django.http import HttpRequest
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product, Category
from products.serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductListSerializer,
)


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
        summary="Добавление нового товара в справочник",
        description="Добавить в справочник новый товар",
    ),
    retrieve=extend_schema(summary="Получение конкретного товара"),
    destroy=extend_schema(summary="Удаление конкретного товара"),
    list_create=extend_schema(summary="Массовое загрузка товара"),
)
# endregion
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.catalog_manager.actual_price()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    renderer_classes = (TemplateHTMLRenderer, JSONRenderer)
    # parser_classes = (JSONParser,)
    lookup_field = "slug"
    template_name = "products/product_detail.html"

    @action(detail=False, methods=["post"], name="Many create products name")
    def list_create(self, request: HttpRequest | Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


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
        summary="Добавление новой категории",
    ),
    retrieve=extend_schema(summary="Получение конкретной категории"),
    destroy=extend_schema(summary="Удаление категории"),
)
# endregion
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


# region testing
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
# endregion
