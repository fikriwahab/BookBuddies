from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review 
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from halamanreview.forms import ReviewForm
from django.contrib.auth.models import User
from katalog.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse

# Create your views here.
def show_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book_id=book_id)

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
            return HttpResponseRedirect(reverse('halamanreview:show_review'))
    else:
        form = ReviewForm()

    context = {'form': form, 'book': book}
    return render(request, "add_review.html", context)

@login_required(login_url='/login/')
@csrf_exempt
def review_page(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')

        if  text is None:
            data = json.loads(request.body)
            text = data['text']
        if text is not None:
            Review.objects.create(
                user=user, comment=text, rating=rating)
            
            return JsonResponse({'message': 'Harapan Created!', 'error': False})



@login_required(login_url='/login/')
@csrf_exempt
def delete_ajax(request, key):
    if request.method == 'POST':
        mytask = get_object_or_404(Review, user=request.user, pk=key)
        mytask.delete()

    return JsonResponse({'error': False})