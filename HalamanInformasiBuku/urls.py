from django.urls import path
from BookBuddies import settings
from HalamanInformasiBuku.views import book_detail, tambah_peminjam,  get_product_json, get_json
from django.conf.urls.static import static
from . import views

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('tambah_peminjam/<int:book_id>/', tambah_peminjam, name='tambah_peminjam'),
    path('get-product-json/', get_product_json, name='get_product_json'),
<<<<<<< HEAD
    path('get-json/', get_json, name='get_json'),
=======
    path('get_json/<int:book_id>/', get_json, name='get_json'),


>>>>>>> origin/dev
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)