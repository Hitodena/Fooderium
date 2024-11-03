from email.mime import image
from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "image_url",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class ProductDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "image_url",
            "calories",
            "proteins",
            "fats",
            "carbs",
            "history",
            "benefits",
            "harms",
            "tags",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
