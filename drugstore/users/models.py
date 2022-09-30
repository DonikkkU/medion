from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=False)
    email = models.EmailField(max_length=254, blank=True, null=False)
    created = models.DateField(auto_now_add=True)