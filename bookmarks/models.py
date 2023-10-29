from django.db import models
from django.contrib.auth.models import User
from katalog.models import Book

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s bookmark for {self.book.title}"
