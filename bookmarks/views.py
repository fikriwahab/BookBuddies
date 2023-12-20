from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from katalog.models import Book

def bookmark_page(request):
    if not request.user.is_authenticated:
        return redirect('katalog:login')  # Redirect jika pengguna tidak login

    bookmarks = Bookmark.objects.filter(user=request.user)
    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmark_page.html', context)

def add_bookmark(request, book_id):
    if request.method == 'POST':
        user = request.user
        book = get_object_or_404(Book, id=book_id)

        # Periksa apakah buku sudah ada di bookmark pengguna
        if not Bookmark.objects.filter(user=user, book=book).exists():
            bookmark = Bookmark(user=user, book=book)
            bookmark.save()
            return JsonResponse({'message': 'Buku telah ditambahkan ke bookmark.'})
        else:
            return JsonResponse({'message': 'Buku sudah ada di bookmark.'})
    
    return JsonResponse({'message': 'Gagal menambahkan buku ke bookmark.'})
