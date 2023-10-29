from django.db import models
from django.contrib.auth.models import User
from katalog.models import Book
from django.urls import reverse
from audioop import reverse

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    due_date = models.DateField(auto_now_add = False, auto_now = False, blank = True, null = True)
    address = models.TextField() 