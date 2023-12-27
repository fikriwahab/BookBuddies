from django.urls import path
from . import views

app_name = 'dashboard_member'

urlpatterns = [
    path('', views.member_dashboard, name='member_dashboard'),
]
