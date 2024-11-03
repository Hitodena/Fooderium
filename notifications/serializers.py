from rest_framework import serializers

from recipes.serializers import RecipeSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "recipe"]
        read_only_fields = ["created_at"]
