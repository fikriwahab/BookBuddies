from django.shortcuts import render, redirect
from .models import Bookmark

def bookmark_page(request):
    # Pastikan hanya pengguna yang telah masuk ke akun (role "Member") yang dapat mengakses halaman Bookmark
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect pengguna yang belum masuk ke halaman login

    # Ambil daftar buku yang telah ditandai sebagai Bookmark oleh pengguna saat ini
    bookmarks = Bookmark.objects.filter(user=request.user)

    context = {'bookmarks': bookmarks}

    return render(request, 'bookmark_page.html', context)