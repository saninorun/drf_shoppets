from django.http import HttpRequest
from django.shortcuts import render, get_list_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView, ListCreateAPIView, get_object_or_404
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, BrowsableAPIRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly, ])
def list_add_products(request: HttpRequest | Request) -> Response:
    if request.method == 'GET':
        products = Product.objects.all().select_related('categories')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly, ])
def get_update_product(request: HttpRequest | Request, slug: str = None) -> Response:
    if request.method == 'GET':
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
