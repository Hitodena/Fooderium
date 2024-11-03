from rest_framework import serializers

from notifications.serializers import CommentSerializer
from recipes.serializers import RecipeListSerializer
from users.models import UserProfile


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "email",
            "nickname",
        ]
        read_only_fields = ["nickname"]


class UserProfileDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="user_comments")
    created_recipes = RecipeListSerializer(many=True, read_only=True, source="created_by")

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "email",
            "profile_image",
            "nickname",
            "favorite_recipes",
            "comments",
            "created_recipes",
        ]
        read_only_fields = ["nickname"]
