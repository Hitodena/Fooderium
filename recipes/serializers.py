from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from products.models import Product
from recipes.models import Rating, Recipe, RecipeStep
from users.models import UserProfile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image", "calories", "proteins", "fats", "carbs"]


class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ["step_number", "instruction", "image"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["user", "score"]


class RecipeListSerializer(serializers.ModelSerializer):
    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ["id", "title", "photo", "is_favorited"]

    def get_is_favorited(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            try:
                user_profile = request.user.profile
                return user_profile.favorite_recipes.filter(id=obj.id).exists()
            except UserProfile.DoesNotExist:
                return False
        return False


class RecipeSerializer(TaggitSerializer, serializers.ModelSerializer):
    steps = RecipeStepSerializer(many=True, required=True)
    products = ProductSerializer(many=True, required=True)
    average_rating = serializers.FloatField(source="get_average_rating", read_only=True)
    favorited_by_count = serializers.IntegerField(source="favorited_by.count", read_only=True)
    tags = TagListSerializerField()
    is_favorited = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "published_date",
            "author",
            "photo",
            "description",
            "calories",
            "proteins",
            "fats",
            "carbs",
            "spiciness",
            "difficulty",
            "hours",
            "minutes",
            "rating",
            "favorites_count",
            "tags",
            "products",
            "steps",
            "average_rating",
            "favorited_by_count",
            "is_favorited",
        ]

    def get_is_favorited(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            try:
                user_profile = request.user.profile
                return user_profile.favorite_recipes.filter(id=obj.id).exists()
            except UserProfile.DoesNotExist:
                return False
        return False

    def create(self, validated_data):
        steps_data = validated_data.pop("steps", [])
        products_data = validated_data.pop("products", [])
        recipe = Recipe.objects.create(**validated_data)

        for step_data in steps_data:
            RecipeStep.objects.create(recipe=recipe, **step_data)

        for product_data in products_data:
            Product.objects.get_or_create(**product_data)

        return recipe
