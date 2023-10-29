
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import UserProfile, Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': books})

#handling login semua user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = request.POST.get('role', 'G')  # default ke Guest
            UserProfile.objects.create(user=user, role=role)
            login(request, user)
            return redirect('katalog:book_list')
        else:
            messages.error(request, "Invalid registration credentials. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('katalog:book_list')
        else:
            messages.error(request, "Invalid login credentials. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def get_book_list(request):
    books = Book.objects.all()
    return books


def user_logout(request):
    logout(request)
    messages.success(request, "Berhasil logout.")
    return redirect('katalog:book_list')
