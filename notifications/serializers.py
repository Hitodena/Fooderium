from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "recipe", "content", "created_at"]
        read_only_fields = ["created_at"]
