from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from katalog.models import Book
from HalamanInformasiBuku.models import Loan
from HalamanInformasiBuku.forms import BorrowForm

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user).first()

    if request.is_ajax():
        # Jika permintaan datang melalui AJAX, kembalikan data dalam format JSON
        data = {
            'book_title': book.title,
            'book_author': book.author,
            'book_description': book.description,
            'loan_status': 'Dipinjam' if loan else 'Tersedia'
        }
        return JsonResponse(data)
    else:
        form = BorrowForm()  # Initialize an empty form
        context = {
            'book': book,
            'loan': loan,
            'form': form,
        }
        return render(request, 'book_detail.html', context)

@csrf_exempt  # Hanya jika Anda ingin mengabaikan token CSRF dalam permintaan AJAX POST
def ajax_create_loan(request, book_id):
    if request.method == 'POST' and request.is_ajax():
        book = get_object_or_404(Book, id=book_id)
        form = BorrowForm(request.POST)
        if form.is_valid():
            due_date = form.cleaned_data['due_date']
            Loan.objects.create(book=book, user=request.user, due_date=due_date)
            return JsonResponse({'success': True})
        else:
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors})

@csrf_exempt  # Hanya jika Anda ingin mengabaikan token CSRF dalam permintaan AJAX POST
def ajax_read_book(request, book_id):
    if request.is_ajax():
        book = get_object_or_404(Book, id=book_id)
        data = {
            'book_title': book.title,
            'book_author': book.author,
            'book_description': book.description,
        }
        return JsonResponse(data)
