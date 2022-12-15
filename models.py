from django.db import models
from django.contrib.auth.models import AbstractUser
import re
from django.core.exceptions import ValidationError
from .managers import CustomUserManager



class CustomUser(AbstractUser):
        username = None
        email = models.EmailField('email address', unique=True)
        phone_number = models.CharField(max_length=11, null=True, blank=True)
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        objects = CustomUserManager()

        def __str__(self):
            return self.email

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

def __str__(self):
    return str(self.user)

class Article(models.Model):
    news = models.TextField(blank=True)


    def __str__(self):
        return self.news


class DropBox(models.Model):
    document = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Drop Boxes'

