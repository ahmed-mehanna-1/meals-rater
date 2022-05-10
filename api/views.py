from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http.request import QueryDict

from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=["POST"], detail=True)
    def rate_meal(self, request, pk):
        if 'stars' not in request.data:
            json = {
                "message": "Stars not provided"
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)
        meal = Meal.objects.get(id=pk)
        stars = request.data['stars']
        username = request.data['username']
        user = User.objects.get(username=username)
        try:
            rate = Rating.objects.get(user=user.id, meal=meal.id)
            # data = {
            #     "user": rate.user,
            #     "meal": rate.meal,
            #     "stars": rate.stars
            # }
            # serializer = RatingSerializer(rate, many=False)
            # print(serializer)
            # if serializer.is_valid():
            #     serializer.save()
            #     json = {
            #         "message": "Meal Rate Updated",
            #         "result": serializer.data
            #     }
            #     return Response(data=json, status=status.HTTP_200_OK)

            rate.stars = stars
            rate.save()
            serializer = RatingSerializer(rate, many=False)
            json = {
                "message": "Meal Rate Updated",
                "result": serializer.data
            }
            return Response(data=json, status=status.HTTP_200_OK)
        except Exception:
            # data = {
            #     "user": user,
            #     "meal": meal,
            #     "stars": int(stars)
            # }
            # serializer = RatingSerializer(data=data)
            # if serializer.is_valid():
            #     serializer.save()
            #     json = {
            #         "message": "Meal Rate Created",
            #         "result": serializer.data
            #     }
            #     return Response(data=json, status=status.HTTP_201_CREATED)

            rate = Rating.objects.create(stars=stars, meal=meal, user=user)
            rate.save()
            serializer = RatingSerializer(data=rate, many=False)
            if serializer.is_valid():
                json = {
                    "message": "Meal Rate Created",
                    "result": serializer.data
                }
                return Response(data=json, status=status.HTTP_201_CREATED)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer