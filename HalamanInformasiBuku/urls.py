from django.urls import path
from HalamanInformasiBuku.views import book_detail, ajax_create_loan, ajax_read_book

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('ajax/create_loan/<int:book_id>/', ajax_create_loan, name='ajax_create_loan'),
    path('ajax/read_book/<int:book_id>/', ajax_read_book, name='ajax_read_book'),
]
