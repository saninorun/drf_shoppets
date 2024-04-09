from django.urls import path, include

from . import views


app_name = 'orders'
urlpatterns = [
    path('orders/', views.OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='list-add-order'),
    path('orders/<int:pk>/', views.OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='get_update_order'),
]
