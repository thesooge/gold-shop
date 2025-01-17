
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<int:pk>/comment', views.CommentsView.as_view(), name='product-comment'),
    path('<int:pk>/delete', views.delete_own_comment, name='comment_delete'),
    path('products/category/<int:category_id>/', views.ProductList.as_view(), name='product-list-by-category'),

    
    
]
