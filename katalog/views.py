from django.shortcuts import render
from .models import Book
from authentication.models import UserProfile
from django.shortcuts import render, redirect


def book_list(request):
    books = Book.objects.all()
    user_profile = None
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        
    return render(request, 'book_list.html', {'book_list': books, 'user_profile': user_profile})
