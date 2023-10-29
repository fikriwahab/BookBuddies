from django.db import models
from django.contrib.auth.models import User
from katalog.models import Book

class MemberLoanActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now=True)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
