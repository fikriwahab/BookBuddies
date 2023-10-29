from django.urls import path
from DashboardAdmin.views import *

app_name = 'DashboardAdmin'

urlpatterns = [
    path('', index, name='dashboard'),
    path('logout', sign_out, name='logout'),
    path('profile', profile, name='profile'),
    path('bookmarks', bookmarks, name='bookmarks'),
    path('recommended', recommended, name='recommended'),
    path('create-book', create_book, name='create_book'),
    path('manage_book', manage_book, name='manage_book'),
    path('delete_book/<int:book_id>', delete_book, name='delete_book'),
    path('manage_member', manage_member, name='manage_member'),
    path('delete_member/<int:member_id>', delete_member, name='delete_member'),
]