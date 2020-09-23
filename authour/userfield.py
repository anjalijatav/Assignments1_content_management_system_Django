from django.db import models
# from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin

from .contentfield import Contentfield

class UserfieldManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user"""

        if not email:
            raise ValueError('Email address is required')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        # user.set_password(password)
        user.save(using=self._db)

        return user

class Userfield(models.Model):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    # password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    if not name:
        raise ValueError('Name is required')
    phone = models.CharField(max_length=10, default="", editable=False)
    if not phone:
        raise ValueError('Phone Number is required')
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=6, default="", editable=False)
    if not pincode:
        raise ValueError('pincode is required')
    objects = UserfieldManager()

    USERNAME_FIELD = 'email'
    # def __str__(self):
    #     return "self.name"