from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # authors (MTM/related_name)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    books = models.ManyToManyField (Book, related_name="authors")
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)