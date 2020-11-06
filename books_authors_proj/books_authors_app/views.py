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
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

# Adds author to the viewed book
def addauthorToBook(request, num):
    key = int(num)
    auth = int(request.POST['alist'])
    Book.objects.get(id=key).authors.add(Author.objects.get(id=auth))
    return redirect('/')

# Takes the user to a new template and allow them to view the details of the selected book
def viewBook(request, num):
    key = int(num)
    print(key)
    context = {
        'book': Book.objects.get(id=key).authors.all(),
        'viewbook': Book.objects.get(id=key),
        'Authors': Author.objects.all(),
    }
    return render(request, 'view.html', context)



