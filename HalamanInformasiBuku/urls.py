from django.urls import path
from BookBuddies import settings
from HalamanInformasiBuku.views import book_detail,  tambah_peminjam,  get_json, get_borrowers_by_book_id
from HalamanInformasiBuku.views import create_flutter
from django.conf.urls.static import static
from .views import update_book_status, show_json

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('tambah_peminjam/<int:book_id>/', tambah_peminjam, name='tambah_peminjam'),
    path('get_json/<int:book_id>/', get_json, name='get_json'),
    path('get_borrowers/<int:book_id>/', get_borrowers_by_book_id, name='get_borrowers_by_book_id'),
    path('create-flutter/', create_flutter , name='create_flutter'),
    path('api/update-book-status/', update_book_status, name='update_book_status'),
    path('json/', show_json, name='show_json'), 



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)