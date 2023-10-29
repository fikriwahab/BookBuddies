from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Bookmark

def bookmark_page(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmark_page.html', context)

def add_bookmark(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        user = request.user
        # Periksa apakah buku sudah ada di bookmark pengguna
        if not Bookmark.objects.filter(user=user, book_id=book_id).exists():
            bookmark = Bookmark(user=user, book_id=book_id)
            bookmark.save()
            return JsonResponse({'message': 'Buku telah ditambahkan ke bookmark.'})
    return JsonResponse({'message': 'Gagal menambahkan buku ke bookmark.'})