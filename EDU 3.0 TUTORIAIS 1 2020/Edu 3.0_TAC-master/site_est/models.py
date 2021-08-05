from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs', max_length=100, blank=True)

    link = models.CharField(null=True, blank=True, max_length=100)
    

    def __str__(self):
        return self.title