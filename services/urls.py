from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('edit-order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('orders/', views.orders, name='orders'),
]

