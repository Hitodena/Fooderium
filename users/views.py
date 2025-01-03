from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile
from users.serializers import UserProfileDetailSerializer, UserProfileListSerializer


class UserList(APIView):
    """ """

    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  # Good

    def post(self, request):
        serializer = UserProfileListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Create and Return
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Not all headers


class UserDetail(APIView):
    """"""

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = UserProfileDetailSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = UserProfileDetailSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
