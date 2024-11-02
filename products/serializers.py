from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
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
