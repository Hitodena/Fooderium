from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product-images/", blank=True)
    calories = models.PositiveIntegerField()
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    history = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    harms = models.TextField(blank=True, null=True)
    tags = TaggableManager()
