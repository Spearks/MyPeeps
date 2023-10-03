from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):

    username = models.CharField(max_length=16, unique=True)

    name = models.CharField(max_length=32, blank=False)

    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = "__all__"