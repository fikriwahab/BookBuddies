from django.urls import path
from dashboard_member.views import *

app_name = 'dashboard_member'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('logout', sign_out, name='logout'),
    path('profile', profile, name='profile'),
    path('bookmarks', bookmarks, name='bookmarks'),
    path('recommended', recommended, name='recommended'),
    path('api/edit-profile/', edit_profile, name='edit_profile'),
]