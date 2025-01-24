
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_create, name='order-create'),
    path('list/', views.OrderList.as_view(), name='order-list'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='order-delete'),
    path('<int:pk>/', views.OrderUpdate.as_view(), name="order-update"),
    
]