from django.contrib import admin

from recipes.models import Recipe, RecipeStep

admin.site.register(Recipe)
admin.site.register(RecipeStep)
