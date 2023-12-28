from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from katalog.models import Book
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import UserSerializer

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    user = request.user

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


def dashboard (request):
    book_count = Book.objects.count()

    context = {
        'page_title': 'Dashboard',
        'book_count': book_count,
    }

    return render(request, 'index.html', context)


def profile(request):
    return render(request, 'profile.html', {'user': request.user, 'page_title': 'Profile'})

def bookmarks(request):
    return render(request, 'bookmarks.html', {'page_title': 'Bookmarks'})

def recommended(request):
    return render(request, 'recommended.html', {'page_title': 'Recommended'})

def sign_out(request):
    logout(request)
    return redirect('/')
