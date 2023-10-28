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


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user.id).first()

    if request.method == "GET":
        data = {
            'book_title': book.title,
            'book_author': book.authors,
            'average_rating': book.average_rating,
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
        return render(request, 'book_info.html', context)

@csrf_exempt
def create_loan(request, book_id):
    if request.method == 'POST':
        # Ambil data dari POST request
        name = request.POST.get("name")
        due_date = request.POST.get("due_date")
        book = get_object_or_404(Book, id=book_id)
        
        # Cek apakah buku tersedia
        if is_book_available(book):
            try:
                # Tambahkan data peminjam ke dalam tabel Loan
                Loan.objects.create(book=book, name=request.user, due_date=due_date)
                return JsonResponse({'success': True, 'message': 'Peminjaman berhasil'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': 'Error: ' + str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'message': 'Buku tidak tersedia untuk dipinjam'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

def is_book_available(book):
    # Cek apakah buku sudah memiliki peminjam (Loan) atau belum
    if Loan.objects.filter(book=book, returned=False).exists():
        return False  # Buku sudah dipinjam
    # Cek apakah jumlah buku yang tersedia cukup
    if book.stock > 0:
        return True  # Buku tersedia
    return False  # Buku tidak tersedia


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