from django.conf.urls.static import static
from django.urls import path
from BookBuddies import settings
from bookmarks import views
from bookmarks.views import add_bookmark, bookmark_page

app_name = 'bookmarks'

urlpatterns = [
    path('bookmarks_page/', bookmark_page , name='bookmark_page'),
    path('add_bookmark/<int:book_id>/', add_bookmark, name='add_bookmark'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)