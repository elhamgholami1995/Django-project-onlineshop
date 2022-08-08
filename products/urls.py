from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductsDetailView, CommentCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='comment_create')
]
