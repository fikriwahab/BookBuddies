from django.urls import path
from halamanreview.views import show_review
from halamanreview.views import create_review
from halamanreview.views import show_xml
from halamanreview.views import show_json
from halamanreview.views import show_json_by_id
from halamanreview.views import show_xml_by_id

app_name = 'halamanreview'

urlpatterns = [
    path('book/<int:book_id>/', show_review, name='show_review'),
    path('create-review/', create_review, name='create_review'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]