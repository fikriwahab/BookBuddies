from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Book, BookReview, Loan, Bookmark
from .forms import ReviewForm, BorrowForm


def home(request):
    # Tambahkan logika untuk halaman beranda di sini
    return render(request, 'home.html')  # Ubah 'home.html' sesuai dengan template yang Anda gunakan


# @login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book_reviews = BookReview.objects.filter(book=book)
    loan = Loan.objects.filter(book=book, user=request.user).first()
    bookmarked = Bookmark.objects.filter(user=request.user, book=book).exists()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            BookReview.objects.create(book=book, user=request.user, text=text)
            return redirect('HalamanInformasiBuku:book_detail', book_id=book_id)
    else:
        form = ReviewForm()

    context = {
        'book': book,
        'book_reviews': book_reviews,
        'loan': loan,
        'bookmarked': bookmarked,
        'form': form,
    }
    return render(request, 'book_detail.html', context)

# @login_required
def borrow_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BorrowForm()
    return render(request, 'borrow_form.html', {'book': book, 'form': form})

# @login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BorrowForm(request.POST)
    if form.is_valid():
        # name = form.cleaned_data['name']  # Ambil nama dari form
        due_date = form.cleaned_data['due_date']
        Loan.objects.create(book=book, user=request.user, due_date=due_date)
        return JsonResponse({'success': True})
    else:
        errors = form.errors
        return JsonResponse({'success': False, 'errors': errors})

# @login_required
# def add_to_bookmark(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     bookmark, created = Bookmark.objects.get_or_create(user=request.user, book=book)
#     if created:
#         return JsonResponse({'success': True, 'message': 'Bookmarked'})
#     else:
#         bookmark.delete()
#         return JsonResponse({'success': True, 'message': 'Removed from bookmarks'})
