from django.db import models
from BookBuddies import settings
from katalog.models import Book
from django.contrib.auth.models import User

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Update referensi ke CustomUser
    name = models.CharField(max_length=255)
    due_date = models.DateField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.book.title}"