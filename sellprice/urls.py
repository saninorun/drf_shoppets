from django.contrib import admin
from django.urls import path, include

from sellprice import views

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'sellprice', views.SellPriceListView, basename='sellprice')


app_name = 'sellprice'
urlpatterns = [
    # path('', include(router.urls), name='sellprice'),
    path('sellprice/', views.SellPriceView.as_view({'get': 'list', 'post': 'create'}), name='list-add-sellprice'),
    path('sellprice/<int:pk>/',
         views.SellPriceView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='get_update_product'),
    path('discountprice/', views.SellDiscountView.as_view({'get': 'list', 'post': 'create'}),
         name='list-add-discountprice'),
    path('discountprice/<int:pk>/',
         views.SellDiscountView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='get_update_discountprice'),
]
