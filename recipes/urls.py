from django.urls import path

from recipes.views import RecipeDetail, RecipesList

urlpatterns = [
    path("api/recipes/", RecipesList.as_view(), name="recipe-list"),
    path("api/recipes/<int:pk>/", RecipeDetail.as_view(), name="recipe-detail"),
]
