from django.urls import path
from notifications.views import CommentList, CommentDetail

urlpatterns = [
    path("api/comments/", CommentList.as_view(), name="product-list"),
    path("api/comments/<int:pk>", CommentDetail.as_view(), name="product-detail"),
]
