from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = [('A', 'Admin'), ('M', 'Member'), ('G', 'Guest')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=USER_ROLES)
