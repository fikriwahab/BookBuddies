from django.db import models

class Review(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
