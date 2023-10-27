from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from katalog.models import Book  
from .models import Loan
from .forms import BorrowForm

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    loan = Loan.objects.filter(book=book, user=request.user).first()

    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            due_date = form.cleaned_data['due_date']
            Loan.objects.create(book=book, user=request.user, due_date=due_date)
            return JsonResponse({'success': True})
        else:
            errors = form.errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = BorrowForm()  # Initialize an empty form

    context = {
        'book': book,
        'loan': loan,
        'form': form,
    }
    return render(request, 'book_detail.html', context)

def borrow_form(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BorrowForm()
    return render(request, 'borrow_form.html', {'book': book, 'form': form})
