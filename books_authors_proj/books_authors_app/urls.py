from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/book', views.addBook),
    path('books/add/authorToBook/<num>', views.addauthorToBook),
    path('books/<num>', views.viewBook),
]