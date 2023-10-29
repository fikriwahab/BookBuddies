from django.db import models
from katalog.models import Book
from django.contrib.auth.models import User

class BorrowActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
