from django.db import models

from recipes.models import Recipe
from users.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on {self.recipe.title, self.id}"
