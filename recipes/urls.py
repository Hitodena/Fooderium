from django.urls import path

urlpatterns = [
    path("api/recipes/", ..., name="recipe-list"),
    path("api/recipes/<int:pk>", ..., name="recipe-detail"),
]
