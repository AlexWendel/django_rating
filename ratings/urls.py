from django.urls import path
from .views import RatingViews, CreateRating, ListRating

urlpatterns = [
    path("create/", CreateRating.as_view(), name="create-rating"),
    path("list/<int:product_id>", ListRating.as_view(), name="list-ratings"),
    path("<int:pk>/", RatingViews.as_view(), name="rating-details"),
]
