from rest_framework import serializers
from .models import Rating, Product, Comment, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "created_at", "edited_at", "reply_to_comment"]


class RatingSerializer(serializers.ModelSerializer):
    author = ProfileSerializer()

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ["author", "created_at", "edited_at"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
