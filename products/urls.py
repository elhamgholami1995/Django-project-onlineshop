from django.contrib import admin
from django.urls import path
from .views import ProductListView,ProductsDetailView


urlpatterns = [
    path('', ProductListView.as_view(),name='product_list'),
    path('<int:pk>/',ProductsDetailView.as_view(),name='product_detail'),
]
