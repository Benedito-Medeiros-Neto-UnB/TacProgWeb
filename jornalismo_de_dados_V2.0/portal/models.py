from django.conf import settings
from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    text = models.TextField()

    def __str__(self):
      return self.text

class Article(models.Model):
    url = models.TextField()
    title = models.TextField()
    authors = models.TextField()

    def __str__(self):
      return self.title

class Reference(models.Model):
    url = models.TextField()
    title = models.TextField()

    def __str__(self):
      return self.title