from django.urls import path
from bookmarks.views import bookmark_page

app_name = 'bookmarks'

urlpatterns = [
    path('', bookmark_page , name='bookmark_page'),
]