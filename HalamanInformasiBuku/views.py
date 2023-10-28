from http.client import HTTPResponse
from smtplib import SMTPResponseException
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
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
import json

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user.id).first()

    if request.method == "GET":
        data = {
            'book_title': book.title,
            'book_author': book.authors,
            'average_rating': book.average_rating,
            'isbn': book.isbn,
            'isbn13': book.isbn13,
            'language_code': book.language_code,
            'num_pages': book.num_pages,
            'ratings_count': book.ratings_count,
            'text_review_count ': book.text_review_count ,
            'publication_date': book.publication_date,
            'publisher': book.publisher,

            'loan_status': 'Dipinjam' if loan else 'Tersedia'
        }
        # return JsonResponse(data)
        return render(request, 'book_info.html', data)
    else:
        form = BorrowForm()  # Initialize an empty form
        context = {
            'book': book,
            'loan': loan,
            'form': form,
        }
        return render(request, 'book_info.html', context)


def is_book_available(book):
    # Fungsi untuk mengecek ketersediaan buku
    if Loan.objects.filter(book=book, returned=False).exists():
        return False  # Buku sudah dipinjam
    if book.stock > 0:
        return True  # Buku tersedia
    return False  # Buku tidak tersedia

@csrf_exempt
def tambah_peminjam(request, book_id):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        
        name = received_data.get('name')
        due_date = received_data.get('due_date')
        address = received_data.get('address')

        try:
            book = Book.objects.get(id=book_id)

            # Memeriksa ketersediaan buku sebelum menambahkan peminjam
            if not is_book_available(book):
                return JsonResponse({'message': 'Buku tidak tersedia untuk dipinjam saat ini!'}, status=400)

            peminjam_baru = Loan.objects.create(
                book=book,
                nama=name,
                tanggal_pengembalian=due_date,
                alamat=address
            )
            peminjam_baru.save()

            return JsonResponse({'message': 'Peminjaman buku berhasil disimpan!'})

        except Book.DoesNotExist:
            return JsonResponse({'message': 'Buku tidak ditemukan!'}, status=404)

    return JsonResponse({'message': 'Permintaan tidak valid.'}, status=400)


def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HTTPResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HTTPResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    product_item = Book.objects.all()
    return HTTPResponse(serializers.serialize('json', product_item))