
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from authentication.forms import CustomUserCreationForm
from .models import Book

from .serializer import BookSerializer

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


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('katalog:book_list')
        else:
            messages.error(request, "Invalid registration credentials. Please try again.")
    else:
        form = CustomUserCreationForm()
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



def book_list_api(request):
    book_objects = Book.objects.all()

    sort_by = request.GET.get('sort_by', 'title') 
    order = request.GET.get('order', 'asc')    

    if order == 'desc':
        sort_by = f'-{sort_by}'

    book_objects = book_objects.order_by(sort_by)

    books_per_page = request.GET.get('show', 10) if request.GET.get('show', 10) else 10
    paginator = Paginator(book_objects, books_per_page)
    page = request.GET.get('page', 1) if request.GET.get('page', 1) else 1

    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)

    serializer = BookSerializer(book_list, many=True)

    return JsonResponse({'books': serializer.data}, safe=False)


def book_detail_api(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        
        serializer = BookSerializer(book)
        
        return JsonResponse(serializer.data)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)


def search_books(request):
    query = request.GET.get('query', '')

    books = Book.objects.filter(
        Q(title__icontains=query) | Q(authors__icontains=query)
    )

    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False)


"""
    title = models.CharField(_("title"), max_length=255)
    authors = models.CharField(_("authors"), max_length=255)
    average_rating = models.FloatField(_("average_rating"))
    isbn = models.CharField(_("isbn"), max_length=150)
    isbn13 = models.CharField(_("isbn 13"), max_length=150)
    language_code = models.CharField(_("language code"), max_length=10)
    num_pages = models.IntegerField(_("number of pages"))
    ratings_count = models.BigIntegerField(_("rating count"))
    text_reviews_count = models.BigIntegerField(_("text review count"))
    publication_date = models.DateField(_("publication date"), auto_now=True)
    publisher = models.CharField(_("publisher"), max_length=150)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    is_desired = models.BooleanField(default=False, help_text="Is this book desired?")"""