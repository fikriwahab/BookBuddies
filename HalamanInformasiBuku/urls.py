from django.urls import path
from HalamanInformasiBuku.views import book_detail, tambah_peminjam,  get_product_json

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('tambah_peminjam/<int:book_id>/', tambah_peminjam, name='tambah_peminjam'),
    path('get-product-json/', get_product_json, name='get_product_json'),
]
