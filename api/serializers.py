from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Meal, Rating
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "required": True
            }
        }


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'unique_id', 'title', 'description', 'no_of_ratings', 'avg_rating']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'unique_id', 'stars', 'user', 'meal']