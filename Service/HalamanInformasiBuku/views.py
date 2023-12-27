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


def is_book_already_borrowed(book):
    return Loan.objects.filter(book=book).exists()


@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user).first()
    is_book_borrowed = is_book_already_borrowed(book)

    if request.method == "GET":
        data = {
            'book_cover': book.cover,
            'book_title': book.title,
            'book_author': book.authors,
            'average_rating': book.average_rating,
            'isbn': book.isbn,
            'isbn13': book.isbn13,
            'num_pages': book.num_pages,
            'text_review_count': book.text_reviews_count,
            'publication_date': book.publication_date,
            'publisher': book.publisher,
            'loan_status': 'Dipinjam' if is_book_borrowed else 'Tersedia'
        }
        return render(request, 'book_info.html', {'book': book, 'loan': loan, 'is_book_borrowed': is_book_borrowed, 'data': data})
    elif request.method == "POST":
        form = BorrowForm(request.POST)
        if form.is_valid():
            # Logika pembaruan data peminjaman
            if is_book_borrowed:  # Jika buku sudah dipinjam
                loan.name = form.cleaned_data['name']
                loan.due_date = form.cleaned_data['due_date']
                loan.address = form.cleaned_data['address']
                loan.save()
            else:  # Jika buku belum dipinjam
                Loan.objects.create(
                    book=book,
                    user=request.user,
                    name=form.cleaned_data['name'],
                    due_date=form.cleaned_data['due_date'],
                    address=form.cleaned_data['address']
                )

            return HttpResponseRedirect(request.path_info)  # Redirect ke halaman detail buku
        else:
            # Jika formulir tidak valid, tampilkan kembali halaman detail buku dengan pesan kesalahan
            context = {'book': book, 'loan': loan, 'form': form, 'is_book_borrowed': is_book_borrowed}
            return render(request, 'book_info.html', context)


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
                due_date = due_date.strftime("%Y-%m-%d")
                book = Book.objects.get(name=name)
                if not is_book_already_borrowed(book, request.user):
                    Loan.objects.create(
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
                    return JsonResponse({'message': 'Buku sudah dipinjam oleh pengguna lain!'}, status=400)
            except Book.DoesNotExist:
                return JsonResponse({'message': 'Buku tidak ditemukan!'}, status=404)
        else:
            return JsonResponse({'message': 'Permintaan tidak valid.'}, status=400)
    else:
        return redirect('katalog:login')


def get_json(request, book_id):
    if request.user.is_authenticated:
        loan_details = Loan.objects.filter(book_id=book_id).values('name', 'due_date', 'address')
        
        loan_list = list(loan_details)

        return JsonResponse(loan_list, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)


@login_required
def get_borrowers_by_book_id(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(id=book_id)
            borrowers = Loan.objects.filter(book=book).values('user__username', 'name', 'due_date', 'address')

            data = list(borrowers)
            return JsonResponse({'borrowers': data})
        except Book.DoesNotExist:
            return JsonResponse({'message': 'Buku tidak ditemukan!'}, status=404)
    else:
        return JsonResponse({'message': 'Harap masuk untuk mengakses data.'}, status=403)



@login_required
def get_user_borrowed_books(request):
    if request.user.is_authenticated:
        user_borrowed_books = Loan.objects.filter(user=request.user)
        books_data = []

        for loan in user_borrowed_books:
            book_data = {
                'book_title': loan.book.title,
                'due_date': loan.due_date,
                'address': loan.address
            }
            books_data.append(book_data)

        return JsonResponse({'borrowed_books': books_data})
    else:
        return JsonResponse({"error": "Unauthorized"}, status=401)


@csrf_exempt
def create_borrower(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Assuming due_date is a string in the format 'YYYY-MM-DD'
            due_date = datetime.strptime(data["due_date"], "%Y-%m-%d").date()

            # Check if the book exists and is available
            book = Book.objects.get(name=data["name"])
            if not is_book_already_borrowed(book, request.user):
                new_borrower = Loan.objects.create(
                    user=request.user,
                    book=book,
                    name=data["name"],
                    due_date=due_date,
                    address=data["address"]
                )
                new_borrower.save()
                return JsonResponse({"status": "success"}, status=200)
            else:
                return JsonResponse({"status": "error", "message": "Buku tidak tersedia untuk dipinjam saat ini!"}, status=400)
        except Book.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Buku tidak ditemukan!"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
