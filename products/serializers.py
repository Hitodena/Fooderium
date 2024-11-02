from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from products.models import Product


class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "image",
            "calories",
            "proteins",
            "fats",
            "carbs",
            "history",
            "benefits",
            "harms",
            "tags",
        ]
