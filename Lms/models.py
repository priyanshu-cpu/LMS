from django.db import models

# Create your models here.

class Books(models.Model):
    bookName = models.CharField(max_length=255)
    bookAuthor = models.CharField(max_length=255)
    quantity = models.IntegerField()
    isAvailable = models.BooleanField()
    