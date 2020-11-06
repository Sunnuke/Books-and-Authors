from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/book', views.addBook),
    path('books/add/authorToBook/<num>', views.addauthorToBook),
    path('books/<num>', views.viewBook),
    path('authors', views.authors),
    path('add/author', views.addAuthor),
    path('authors/add/bookToAuthor/<num>', views.addbookToAuthor),
    path('authors/<num>', views.viewAuthor),
]