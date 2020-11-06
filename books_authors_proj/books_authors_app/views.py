from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

# Loads up root and renders database
def index(request):
    context = {
        'all_books': Book.objects.all(),
        'all_Authors': Author.objects.all()
    }
    return render(request, 'index.html', context)

# Takes user input for a new book and adds it to the database
def addBook(request):
    return redirect('/')

# Takes the user to a new template and allow them to view the details of the selected book
def viewBook(request):
    context = {
        'all_books': Book.objects.all(),
        'all_Authors': Author.objects.all()
    }
    return render(request, '', context)