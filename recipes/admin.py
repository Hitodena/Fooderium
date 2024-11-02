from django.contrib import admin

from recipes.models import Rating, Recipe, RecipeProduct, RecipeStep

admin.site.register(Recipe)
admin.site.register(RecipeStep)
admin.site.register(Rating)
admin.site.register(RecipeProduct)
