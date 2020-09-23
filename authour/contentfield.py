from django.db import models
from django.conf import settings
# from django.shortcuts import render

class ContentfieldManager(models.Manager):
    """User Portfolio Manager"""
    # def create_user_portfolio(self, user_id, **extra_fields):

    def create_content_data(self, user_id, **extra_fields):
        content_data = self.model(user_id=user_id, **extra_fields)
        content_data.save(using=self._db)


        return content_data


class Contentfield(models.Model):
    """User portfolio model"""

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)

    def document_file(self, filename):

        path = 'content_management_system/file/{}'.format(filename)
        return path

    document = models.ImageField(upload_to=document_file)
    categories = models.CharField(max_length=255)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    objects = ContentfieldManager()

    def __str__(self):
        return 'Created!'
