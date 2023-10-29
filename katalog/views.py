
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import UserProfile, Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def book_list(request):
    book_objects = Book.objects.all()
    
    # Menentukan jumlah buku per halaman
    books_per_page = 35
    paginator = Paginator(book_objects, books_per_page)
    
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        # Jika `page` bukan integer, tampilkan halaman pertama.
        book_list = paginator.page(1)
    except EmptyPage:
        # Jika `page` berada di luar jangkauan (misalnya melebihi jumlah halaman yang ada), tampilkan halaman terakhir.
        book_list = paginator.page(paginator.num_pages)
        
    return render(request, 'book_list.html', {'book_list': book_list})


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
