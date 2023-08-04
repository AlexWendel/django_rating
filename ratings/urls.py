from django.urls import path
from .views import RatingViews, CreateRating

urlpatterns = [
    path("create/", CreateRating.as_view(), name="create-rating"),
    path("<int:pk>/", RatingViews.as_view(), name="rating-details"),
]
