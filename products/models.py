from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product-images/", blank=True)
    calories = models.DecimalField(decimal_places=2, max_digits=5)
    proteins = models.DecimalField(decimal_places=2, max_digits=5)
    fats = models.DecimalField(decimal_places=2, max_digits=5)
    carbs = models.DecimalField(decimal_places=2, max_digits=5)
    history = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    harms = models.TextField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.name
