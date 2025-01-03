from django.urls import path
from products.views import ProductList, ProductDetail

urlpatterns = [
    path("api/products/", ProductList.as_view(), name="product-list"),
    path("api/products/<int:pk>", ProductDetail.as_view(), name="product-detail"),
]
