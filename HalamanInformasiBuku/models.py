from django.db import models
from django.contrib.auth.models import User
from katalog.models import Book

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    address = models.TextField() 