from django.urls import path
from . import views

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/loan/', views.ajax_create_loan, name='ajax_create_loan'),
    path('book/<int:book_id>/read/', views.ajax_read_book, name='ajax_read_book'),
]
