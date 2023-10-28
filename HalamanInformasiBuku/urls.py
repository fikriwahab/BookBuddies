from django.urls import path
from HalamanInformasiBuku.views import book_detail, create_loan, show_json, show_json_by_id, show_xml, show_xml_by_id, get_product_json

app_name = 'HalamanInformasiBuku'

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('book/<int:book_id>/loan/', create_loan, name='create_loan'),
    path('show-xml/', show_xml, name='show_xml'),
    path('show-json/', show_json, name='show_json'),
    path('show-xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('show-json/<int:id>/',show_json_by_id, name='show_json_by_id'),
    path('get-product-json/', get_product_json, name='get_product_json'),
]
