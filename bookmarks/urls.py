from django.urls import path
from bookmarks import views
from bookmarks.views import add_bookmark, bookmark_page

app_name = 'bookmarks'

urlpatterns = [
    path('bookmarks/', bookmark_page , name='bookmark_page'),
    path('', add_bookmark, name='add_bookmark'),
]