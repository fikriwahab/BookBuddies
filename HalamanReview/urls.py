from django.urls import path
from halamanreview.views import show_review
from halamanreview.views import add_review
from halamanreview.views import show_xml
from halamanreview.views import show_review_json


app_name = 'halamanreview'

urlpatterns = [
    path('review/<int:book_id>/', show_review, name='show_review'),
    path('add_review/<int:book_id>/', add_review, name='add_review'),
    path('xml/', show_xml, name='show_xml'), 
    path('show-json/', show_review_json, name='show-json')
]