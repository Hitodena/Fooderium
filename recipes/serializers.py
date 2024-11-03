from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from products.models import Product
from recipes.models import Rating, Recipe, RecipeProduct, RecipeStep
from users.models import UserProfile


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name", "image"]


class RecipeProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField(required=True, min_value=1)

    class Meta:
        model = RecipeProduct
        fields = ["product", "quantity"]


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
        fields = ["id", "title", "image", "is_favorited"]

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
    is_favorited = serializers.SerializerMethodField()
    steps = RecipeStepSerializer(many=True, required=True)
    recipe_products = RecipeProductSerializer(many=True, required=True)
    average_rating = serializers.FloatField(source="get_average_rating", read_only=True)
    favorited_by_count = serializers.IntegerField(source="favorited_by.count", read_only=True)
    tags = TagListSerializerField()
    is_favorited = serializers.SerializerMethodField()
    servings = serializers.IntegerField(required=True, min_value=1)
    target_servings = serializers.IntegerField(write_only=True, required=False, min_value=1)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "published_date",
            "author",
            "image",
            "description",
            "calories",
            "proteins",
            "fats",
            "carbs",
            "spiciness",
            "difficulty",
            "hours",
            "minutes",
            "favorites_count",
            "tags",
            "recipe_products",
            "steps",
            "average_rating",
            "favorited_by_count",
            "is_favorited",
            "servings",
            "target_servings",
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request and request.query_params.get("target_servings"):
            try:
                target_servings = int(request.query_params.get("target_servings"))
                if target_servings > 0:
                    multiplier = target_servings / instance.servings
                    adjusted_products = []

                    # Перерасчёт количества для каждого продукта
                    for recipe_product in instance.recipe_products.all():
                        adjusted_quantity = int(recipe_product.quantity * multiplier)
                        adjusted_products.append(
                            {
                                "product": recipe_product.product.id,
                                "quantity": adjusted_quantity,
                                "name": recipe_product.product.name,
                                "image": (
                                    recipe_product.product.image.url
                                    if recipe_product.product.image
                                    else None
                                ),
                            }
                        )

                    data["recipe_products"] = adjusted_products
                    data["adjusted_servings"] = target_servings
            except (ValueError, ZeroDivisionError):
                pass
        return data

    def create(self, validated_data):
        steps_data = validated_data.pop("steps", [])
        recipe_products_data = validated_data.pop("products", [])
        recipe = Recipe.objects.create(**validated_data)

        for step_data in steps_data:
            RecipeStep.objects.create(recipe=recipe, **step_data)

        for recipe_product_data in recipe_products_data:
            product = recipe_product_data["product"]
            quantity = recipe_product_data["quantity"]
            RecipeProduct.objects.create(recipe=recipe, product=product, quantity=quantity)

        return recipe
