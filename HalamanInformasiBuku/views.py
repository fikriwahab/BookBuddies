from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from katalog.models import Book
from HalamanInformasiBuku.models import Loan
from HalamanInformasiBuku.forms import BorrowForm
import csv
from django.shortcuts import render
from django.http import JsonResponse
from katalog.models import Book

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user.id).first()

    if request.method == "GET":
        data = {
            'book_title': book.title,
            'book_author': book.authors,
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

@csrf_exempt  
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

@csrf_exempt  
def ajax_read_book(request, book_id):
    if request.is_ajax():
        book = get_object_or_404(Book, id=book_id)
        data = {
            'book_title': book.title,
            'book_author': book.author,
            'book_description': book.description,
        }
        return JsonResponse(data)
