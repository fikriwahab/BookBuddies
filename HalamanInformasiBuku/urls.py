from django.urls import path
from HalamanInformasiBuku.views import book_detail, borrow_book, borrow_form

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    # path('bookmark/<int:book_id>/', views.add_to_bookmark, name='add_to_bookmark'),
    path('borrow_form/<int:book_id>/', borrow_form, name='borrow_form'),
    path('borrow_book/<int:book_id>/', borrow_book, name='borrow_book'),
]
