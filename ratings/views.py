from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.pagination import PageNumberPagination
from .models import Rating
from .serializers import RatingSerializer


class CreateRating(CreateAPIView):
    model = Rating
    queryset = Rating.objects
    serializer_class = RatingSerializer


class ListRating(ListAPIView):
    model = Rating
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination
    lookup_url_kwarg = "product_id"

    def get_queryset(self):
        product_id = self.kwargs.get(self.lookup_url_kwarg)
        return Rating.objects.filter(product=product_id)


class RatingViews(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects
    serializer_class = RatingSerializer
    http_method_names = ["get", "delete", "patch"]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
