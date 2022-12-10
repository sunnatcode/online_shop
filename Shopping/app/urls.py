from django.urls import path
from .views import (SearchProductView, ProductDeleteView,
ProductView, CategoryView, OrderView, CartView, 
ProductUpdateView)

urlpatterns = [
    path('search/', SearchProductView.as_view()),
    path('prodcut/', ProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('order/', OrderView.as_view()),
    path('cart/', CartView.as_view()),

    path('product_delete/<int:pk>/', ProductDeleteView.as_view()),
    path('product_update/<int:pk>/', ProductUpdateView.as_view()),
]