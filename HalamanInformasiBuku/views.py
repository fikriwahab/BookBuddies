from datetime import datetime
from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from katalog.models import Book
from HalamanInformasiBuku.models import Loan
from HalamanInformasiBuku.forms import BorrowForm
from django.http import HttpResponseRedirect
import csv
from django.shortcuts import render
from katalog.models import Book
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse
from HalamanInformasiBuku.models import Loan
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user.id).first()

    if request.method == "GET":
        data = {
            'book_cover' : book.cover,
            'book_title': book.title,
            'book_author': book.authors,
            'average_rating': book.average_rating,
            'isbn': book.isbn,
            'isbn13': book.isbn13,
            'num_pages': book.num_pages,
            'text_review_count': book.text_review_count,
            'publication_date': book.publication_date,
            'publisher': book.publisher,
            'loan_status': 'Dipinjam' if loan else 'Tersedia'
        }
        return render(request, 'book_info.html', {'book': book})
    elif request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
           
            return HttpResponseRedirect(request.path_info)  # Redirect ke halaman detail buku
        else:
            # Jika formulir tidak valid, tampilkan kembali halaman detail buku dengan pesan kesalahan
            context = {'book': book, 'loan': loan, 'form': form}
            return render(request, 'book_info.html', context)


def is_book_available(book):
    # Fungsi untuk mengecek ketersediaan buku
    if Loan.objects.filter(book=book).exists():
        return False  # Buku sudah dipinjam
    return True  # Buku tidak tersedia

@csrf_exempt
@login_required
def tambah_peminjam(request):
    if request.user.is_authenticated:
        form = BorrowForm(request.POST)
        data = {}
        if request.method == 'POST' and form.is_valid():
            name = form.cleaned_data['name']
            due_date = form.cleaned_data['due_date']
            address = form.cleaned_data['address']
            try:
                due_date = due_date.strptime(due_date, "%Y-%m-%d %H:%M:%S.%f").date()
                due_date = due_date.strftime("%Y-%m-%d")

                book = Book.objects.get(name=name)
                if is_book_available(book):
                    peminjam_baru = Loan.objects.create(
                        book=book,
                        user=request.user,
                        name=name,
                        due_date=due_date,
                        address=address
                    )
                    data['name'] = name
                    data['due_date'] = due_date
                    data['address'] = address
                    return JsonResponse(data)
                else:
                    return JsonResponse({'message': 'Buku tidak tersedia untuk dipinjam saat ini!'}, status=400)
            except Book.DoesNotExist:
                return JsonResponse({'message': 'Buku tidak ditemukan!'}, status=404)
        else:
            return JsonResponse({'message': 'Permintaan tidak valid.'}, status=400)
    else:
        return redirect('katalog:login')


def get_product_json(request):
    product_item = Book.objects.all()
    return HTTPResponse(serializers.serialize('json', product_item))


def get_json(request, book_id):
    if request.user.is_superuser:
        loan_details = Loan.objects.filter(book_id=book_id).values('name', 'due_date', 'address')
        
        loan_list = list(loan_details)

        return JsonResponse(loan_list, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)







