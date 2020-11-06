from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/book', views.addBook),
    path('books/<id>', views.viewBook),
]