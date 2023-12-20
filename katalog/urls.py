from django.urls import path
from . import views
from BookBuddies import settings
from django.conf.urls.static import static
app_name = "katalog"

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),

    path('api/book_list/', views.book_list_api, name='book_list_api'),
    path('api/book/<int:book_id>/', views.book_detail_api, name='book_detail_api'),
    path('api/search/', views.search_books, name='search_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)