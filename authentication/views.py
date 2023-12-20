from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .serializer import UserSerializer, ProfileSerializer

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        # Menggunakan AuthenticationForm untuk proses login
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Memeriksa kredensial pengguna
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)  # Masukkan pengguna ke dalam sesi
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!",
                    # "redirect_url": reverse('katalog:book_list')  # Reverse URL untuk katalog:book_list
                }, status=200)
        return JsonResponse({
            "status": False,
            "message": "Invalid login credentials. Please try again."
        }, status=401)
    else:
        # Handle GET request, jika diperlukan
        # Misalnya, tampilkan halaman login
        return JsonResponse({
            "status": False,
            "message": "Invalid request method. Use POST for login."
        }, status=405)


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Menggunakan auth_login
            # Return JsonResponse dan redirect ke katalog:book_list.
            return JsonResponse({
                "status": True,
                "message": "Registration successful!",
                "redirect_url": reverse('katalog:book_list')  # Reverse URL untuk katalog:book_list
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            # Return JsonResponse untuk kegagalan registrasi.
            return JsonResponse({
                "status": False,
                "message": "Invalid registration credentials. Please try again."
            }, status=400)
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def logout_view(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!",
            # "redirect_url": reverse('authentication:login_view')  # Reverse URL untuk authentication:login_view
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)
    

@api_view(['POST'])
def api_user_register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return JsonResponse({
            'message': 'User registration successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, safe=False)
    return JsonResponse(serializer.errors, safe=False)


def api_user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully.'}, safe=False)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return JsonResponse(serializer.data, safe=False)