import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Meal(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)

    def avg_rating(self):
        ratings = Rating.objects.filter(meal=self)
        size = len(ratings)
        if size == 0:
            return 0

        ratings_sum = 0
        for rating in ratings:
            ratings_sum += int(rating.stars)
        return ratings_sum / size

    def __str__(self):
        return self.title


class Rating(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    # def __str__(self):
    #     return self.meal

    class Meta:
        unique_together = (('user', 'meal'))
        index_together = (('user', 'meal'))
