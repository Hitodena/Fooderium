from django.db import models
from django.db.models import Avg
from taggit.managers import TaggableManager

from products.models import Product


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "users.UserProfile", on_delete=models.CASCADE, related_name="created_by"
    )
    image = models.ImageField(upload_to="recipes-images/", blank=True)
    description = models.TextField()
    calories = models.DecimalField(decimal_places=2, max_digits=5)
    proteins = models.DecimalField(decimal_places=2, max_digits=5)
    fats = models.DecimalField(decimal_places=2, max_digits=5)
    carbs = models.DecimalField(decimal_places=2, max_digits=5)
    spiciness = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True
    )
    difficulty = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], blank=True, null=True
    )
    hours = models.PositiveIntegerField(blank=True, null=True, default=0)
    minutes = models.PositiveIntegerField(blank=True, null=True, default=0)
    favorites_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    servings = models.PositiveSmallIntegerField(default=1)
    tags = TaggableManager()
    # Many-to-many fields
    products = models.ManyToManyField(Product, blank=True)

    def get_average_rating(self):
        average_rating = self.ratings.aggregate(Avg("score"))["score__avg"]  # Access by rel.name
        return average_rating if average_rating is not None else 0  # Return 0 if rating is empty

    def __str__(self) -> str:
        return self.title


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ("recipe", "user")

    def __str__(self) -> str:
        return f"Rating by {self.user.nickname} for {self.recipe.title} with id {self.recipe.id} is {self.score}"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    instruction = models.TextField()
    image = models.ImageField(upload_to="recipe-steps-images/", blank=True)

    class Meta:
        ordering = ["step_number"]

    def __str__(self) -> str:
        return f"Step {self.step_number} of {self.recipe.title} with recipe id {self.recipe.id}"


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="recipe_products", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.product.name} for {self.recipe.title} with id {self.recipe.id}"
