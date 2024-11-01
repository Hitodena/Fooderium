from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    nickname = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to="profile-images/", blank=True)
    # favorite_recipes = models.ManyToManyField(Recipe, blank=True, related_name="favorited_by")
    # comments = models.ManyToManyField(Comment, blank=True, related_name="user_comments")
