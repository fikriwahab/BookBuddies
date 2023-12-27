from django.db import models
from django.contrib.auth.models import User
from katalog.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewBook(models.Model):
    book = models.OneToOneField(Book, on_delete = models.CASCADE)
    total_rating = models.FloatField(default=0.0)
    total_review = models.IntegerField(default=0)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField()
