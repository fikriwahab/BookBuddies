from django.urls import path
from BookBuddies import settings
from HalamanInformasiBuku.views import book_detail, get_user_borrowed_books, tambah_peminjam,  get_json, get_borrowers_by_book_id, create_borrower
from django.conf.urls.static import static

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('tambah_peminjam/<int:book_id>/', tambah_peminjam, name='tambah_peminjam'),
    path('get_json/<int:book_id>/', get_json, name='get_json'),
    path('get_borrowers/<int:book_id>/', get_borrowers_by_book_id, name='get_borrowers_by_book_id'),
    path('user_borrowed_books/', get_user_borrowed_books, name='user_borrowed_books'),
    path('create-borrower/', create_borrower, name='create_borrower'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)