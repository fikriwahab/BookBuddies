from django.urls import path
from authentication.views import login_view, register_view, logout_view, api_user_register, api_user_logout, getProfile
from rest_framework_simplejwt import views as jwt_views

app_name = 'authentication'

urlpatterns = [
    path('login_view/', login_view, name='login_view'),
    path('register_view/', register_view, name='register_view'),
    path('logout_view/', logout_view, name='logout_view'),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', api_user_register, name='api_user_register'),
    path('logout/', api_user_logout, name='api_user_logout'),

    ## Profile
    path('profile/', getProfile, name='profile'),

]