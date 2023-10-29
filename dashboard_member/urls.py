from django.urls import path
from dashboard_member.views import *

app_name = 'dashboard_member'

urlpatterns = [
    path('', index, name='dashboard'),
    path('logout', sign_out, name='logout'),
    path('profile', profile, name='profile'),
    path('bookmarks', bookmarks, name='bookmarks'),
    path('recommended', recommended, name='recommended'),
    path('create-book', create_book, name='create_book'),
    path('manage_book', manage_book, name='manage_book'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),
]