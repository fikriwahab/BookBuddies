from django.urls import path
from HalamanReview.views import *


app_name = 'HalamanReview'

urlpatterns = [
    path('review/<int:book_id>/', show_review, name='show_review'),
    path('add_review/<int:book_id>/', add_review, name='add_review'),
    path('xml/', show_xml, name='show_xml'), 
    path('show-json/', show_review_json, name='show-json'),
    path('get_all_books/', get_all_books, name='get_all_books'),
    path('get_all_reviews/', get_all_reviews, name='get_all_reviews'),
    path('get_my_reviews/', get_my_reviews, name='get_my_reviews'),
    path('get_book/', get_book, name='get_book'),
    path('book_reviews/', book_reviews, name='book_reviews'),
    path('create_review_flutter/', create_review_flutter, name='create_review_flutter'),
    path('delete_review_flutter/', delete_review_flutter, name='delete_review_flutter'),
    path('edit_review_flutter/', edit_review_flutter, name='edit_review_flutter'),
]