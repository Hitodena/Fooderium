from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from recipes.models import Recipe
from recipes.serializers import RecipeListSerializer, RecipeSerializer


class RecipesList(APIView):
    """ """

    pagination_class = PageNumberPagination

    def get(self, request):
        recipes = Recipe.objects.all()
        paginator = self.pagination_class()
        paginated_recipes = paginator.paginate_queryset(recipes, request)
        serializer = RecipeListSerializer(paginated_recipes, many=True)
        return paginator.get_paginated_response(serializer.data)  # Good

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Create and Return
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Not all headers


class RecipeDetail(APIView):
    """"""

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
