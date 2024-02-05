from django.contrib import admin
from django.urls import path, include

from products import views

# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'item', views.ProductViewSet, basename='items')


app_name = 'product'
urlpatterns = [
    path('', views.list_add_products, name='list-add-products'),
    path('<slug:slug>/', views.get_update_product, name='get_update_product'),
]
