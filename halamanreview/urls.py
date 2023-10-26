from django.urls import path
from halamanreview.views import show_reviewbuku

app_name = 'halamanreview'

urlpatterns = [
    path('', show_reviewbuku, name='show_reviewbuku'),
]