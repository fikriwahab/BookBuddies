from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from katalog.models import Book
from .forms import BookForm

# Create your views here.

@login_required
def index(request):
    book_count = Book.objects.count()

    context = {
        'page_title': 'Dashboard',
        'book_count': book_count,
    }

    return render(request, 'index.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user, 'page_title': 'Profile'})

@login_required
def bookmarks(request):
    return render(request, 'bookmarks.html', {'page_title': 'Bookmarks'})

@login_required
def recommended(request):
    return render(request, 'recommended.html', {'page_title': 'Recommended'})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/')

