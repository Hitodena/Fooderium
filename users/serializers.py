from rest_framework import serializers

from recipes.serializers import RecipeSerializer
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    favorite_recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ["id", "user", "nickname", "name", "profile_image", "favorite_recipes"]
