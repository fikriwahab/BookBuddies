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
            'language_code': book.language_code,
            'num_pages': book.num_pages,
            'ratings_count': book.ratings_count,
            'text_review_count': book.text_review_count,
            'publication_date': book.publication_date,
            'publisher': book.publisher,
            'loan_status': 'Dipinjam' if loan else 'Tersedia'
        }
        return render(request, 'book_info.html', {'book': book})
    elif request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            # Lakukan sesuatu dengan data yang diterima dari formulir
            # Contoh: Simpan data atau lakukan operasi lain
            # Redirect atau tampilkan kembali halaman detail buku setelah POST
            return HttpResponseRedirect(request.path_info)  # Redirect ke halaman detail buku
        else:
            # Jika formulir tidak valid, tampilkan kembali halaman detail buku dengan pesan kesalahan
            context = {'book': book, 'loan': loan, 'form': form}
            return render(request, 'book_info.html', context)



def is_book_available(book):
    # Fungsi untuk mengecek ketersediaan buku
    if Loan.objects.filter(book=book, returned=False).exists():
        return False  # Buku sudah dipinjam
    if book.stock > 0:
        return True  # Buku tersedia
    return False  # Buku tidak tersedia

@csrf_exempt
@login_required
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

@staff_member_required
def get_product_json(request):
    product_item = Book.objects.all()
    return HTTPResponse(serializers.serialize('json', product_item))