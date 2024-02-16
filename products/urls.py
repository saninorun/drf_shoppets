from django.contrib import admin
from django.urls import path, include

from products import views

from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register(prefix=r'products', viewset=views.ProductViewSet, basename='products')
router.register(prefix=r'category', viewset=views.CategoryViewSet, basename='category')


app_name = 'products'
urlpatterns = [
    path('', include(router.urls)),
    # path('products/', views.list_add_products, name='list-add-products'),
    # path('products/<slug:slug>/', views.get_update_product, name='get_update_product'),
    # path('categories/', views.CategoryList.as_view(), name='list-add-category'),
    # path('categories/<slug:slug>/', views.CategoryView.as_view(), name='get_update_category'),
]
