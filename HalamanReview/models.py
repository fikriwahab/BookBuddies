from django.db import models

class Review(models.Model):
    user_id = models.CharField(max_length=150)
    book_id = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
