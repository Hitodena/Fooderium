from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from products.models import Product
from products.serializers import ProductListSerializer, ProductDetailSerializer


class ProductList(APIView):
    """ """

    pagination_class = PageNumberPagination

    def get(self, request):
        products = Product.objects.all()
        paginator = self.pagination_class()
        paginated_recipes = paginator.paginate_queryset(products, request)
        serializer = ProductListSerializer(paginated_recipes, many=True)
        return paginator.get_paginated_response(serializer.data)  # Good

    def post(self, request):
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Create and Return
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Not all headers


class ProductDetail(APIView):
    """"""

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = ProductDetailSerializer(recipe, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = ProductDetailSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
