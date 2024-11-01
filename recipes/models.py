from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

from notifications.models import Comment
from products.models import Product


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="recipes/", blank=True)
    description = models.TextField()
    calories = models.PositiveIntegerField()
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    spiciness = models.IntegerField(blank=True, null=True)
    difficulty = models.CharField(max_length=50, blank=True)
    total_time = models.DurationField()
    kitchen_time = models.DurationField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    favorites_count = models.PositiveIntegerField(default=0, blank=True)
    tags = TaggableManager()
    # Many-to-many fields
    products = models.ManyToManyField(Product, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    instruction = models.TextField()
    image = models.ImageField(upload_to="recipe-steps-images/", blank=True)

    class Meta:
        ordering = ["step_number"]
