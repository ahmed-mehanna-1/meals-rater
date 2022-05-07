from rest_framework import serializers
from .models import Meal, Rating


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'unique_id', 'title', 'description']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'unique_id', 'stars', 'user', 'meal']