from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from katalog.models import Book
from .forms import BookForm

# Create your views here.


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    # member_count = Member.objects.count()
    book_count = Book.objects.count()

    context = {
        'page_title': 'Dashboard',
        # 'member_count': member_count,
        'book_count': book_count,
    }

    return render(request, 'index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def profile(request):
    return render(request, 'profile.html', {'user': request.user, 'page_title': 'Profile'})


@user_passes_test(lambda u: u.is_superuser)
def bookmarks(request):
    return render(request, 'bookmarks.html', {'page_title': 'Bookmarks'})


@user_passes_test(lambda u: u.is_superuser)
def recommended(request):
    return render(request, 'recommended.html', {'page_title': 'Recommended'})


@user_passes_test(lambda u: u.is_superuser)
def sign_out(request):
    logout(request)
    return redirect('/')


@user_passes_test(lambda u: u.is_superuser)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'create_book.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def manage_book(request):
    books = Book.objects.all()
    return render(request, 'manage_book.html', {'book_list': books})


@user_passes_test(lambda u: u.is_superuser)
def delete_book(request, book_id):
    try:
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        response = {'success': True}
    except Book.DoesNotExist:
        response = {'success': False, 'error_message': 'Book not found'}
    return JsonResponse(response)


@user_passes_test(lambda u: u.is_superuser)
def manage_member(request):
    # members = Member.objects.all()

    #asumsi dummy data seperti ini
    dummy_data = [
        {
            "id": 1,
            "username": "john_doe",
            "join_date": "2023-01-15",
            "borrowed_books": [
                {
                    "title": "Book 1",
                    "borrow_date": "2023-01-20",
                    "return_date": "2023-02-05"
                },
                {
                    "title": "Book 2",
                    "borrow_date": "2023-02-10",
                    "return_date": "2023-03-02"
                }
            ]
        },
        {
             "id": 2,
            "username": "jane_smith",
            "join_date": "2023-02-05",
            "borrowed_books": [
                {
                    "title": "Book 2",
                    "borrow_date": "2023-02-15",
                    "return_date": "2023-03-10"
                }
            ]
        },
        {
             "id": 3,
            "username": "alice_walker",
            "join_date": "2023-03-01",
            "borrowed_books": [
                {
                    "title": "Book 3",
                    "borrow_date": "2023-03-10",
                    "return_date": "2023-04-01"
                }
            ]
        }
    ]

    return render(request, 'manage_member.html', {'member_list': dummy_data})


@user_passes_test(lambda u: u.is_superuser)
def delete_member(request, member_id):
    try:
        member = get_object_or_404(Member, pk=member_id)
        member.delete()
        response = {'success': True}
    except Member.DoesNotExist:
        response = {'success': False, 'error_message': 'Member not found'}
    return JsonResponse(response)
