from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, ReviewBook
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from HalamanReview.forms import ReviewForm
from django.contrib.auth.models import User
from katalog.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
def show_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)

    context = {
        'book': book,
        'reviews': reviews
    }

    return render(request, "reviewbuku.html", context)


def show_xml(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@csrf_exempt
def show_review_json(request):
    data = Review.objects.all()


    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

@csrf_exempt
@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Create a new review and associate it with the book
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return HttpResponseRedirect(reverse('HalamanReview:show_review'))
    else:
        form = ReviewForm()

    context = {'form': form, 'book': book}
    return render(request, "add_review.html", context)

@login_required(login_url='/login/')
@csrf_exempt
def review_page(request):
    if request.method == 'POST':
        user = request.user
        book = request.POST.get('book')
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        if  text is None:
            data = json.loads(request.body)
            text = data['text']
        if text is not None:
            Review.objects.create(
                book=book, user=user, review=text, rating=rating)
            
            return JsonResponse({'message': 'Harapan Created!', 'error': False})



@login_required(login_url='/login/')
@csrf_exempt
def delete_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(Review, user=request.user, pk=key)
        mytask.delete()

    return JsonResponse({'error': False})

#-------------------------------------Flutter-----------------------------------------#
def get_all_books(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize('json', books.all()), content_type="application/json")

def get_all_reviews(request):
    reviews = Review.objects.all()
    return HttpResponse(serializers.serialize('json', reviews.all()), content_type="application/json")

def get_my_reviews(request):
    my_reviews = Review.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', my_reviews.all()), content_type="application/json")

@csrf_exempt
def get_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.filter(pk=data["pk"])
        return HttpResponse(serializers.serialize('json', book.all()), content_type="application/json")
    
    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def book_reviews(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["pk"])
        book_review  = Review.objects.filter(book = book)
        return HttpResponse(serializers.serialize('json', book_review.all()), content_type="application/json")
    
    return HttpResponse(serializers.serialize('json', []), content_type="application/json")

@csrf_exempt
def create_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.get(pk=data["pk"])

        Review(
            user = request.user,
            book = book,
            rating = int(data["rating"]),
            review = data["review"],
        ).save()

        # review_book, create = ReviewBook.objects.get_or_create(book=book)
        # total_rating = review_book.total_rating * review_book.total_review
        # review_book.total_review += 1
        # review_book.save()

        # review_book.total_rating = (total_rating + int(data["rating"])) / review_book.total_review
        # review_book.save()

        return JsonResponse({"status": True,}, status=200)
    
    return JsonResponse({"status": False}, status=500)

@csrf_exempt
def delete_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        review = Review.objects.get(pk=data["review_id"])
        rating = review.rating

        # review_book, create = ReviewBook.objects.get_or_create(book=review.book)
        # total_rating = review_book.total_rating * review_book.total_review
        # review_book.total_review -= 1
        # review_book.save()

        # review_book.total_rating = (total_rating - review.rating) / review_book.total_review
        # review_book.save()
        review.delete()
        
        return JsonResponse({"status": True,}, status=200)
    
    return JsonResponse({"status": False}, status=500)

@csrf_exempt
def edit_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        review = Review.objects.get(pk=data["review_id"])
        review_book, create = ReviewBook.objects.get_or_create(book=review.book)
        total_rating = (review_book.total_rating * review_book.total_review) - review.rating
        # review_book.total_review -= 1
        # review_book.save()

        review.rating = int(data["rating"])
        review.review = data["review"]
        review.save()

        # review_book.total_review += 1
        # review_book.save()

        # review_book.total_rating = (total_rating + int(data["rating"])) / review_book.total_review
        # review_book.save()

        return JsonResponse({"status": True,}, status=200)
    
    return JsonResponse({"status": False}, status=500)