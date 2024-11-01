from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="product-images/")
    calories = models.PositiveIntegerField()
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    history = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    harms = models.TextField(blank=True)
    tags = TaggableManager()
