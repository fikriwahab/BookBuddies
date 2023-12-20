from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255, required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'full_name', 'password1', 'password2']
