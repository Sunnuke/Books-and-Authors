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


# Author side
# Loads up root and renders database
def authors(request):
    context = {
        'all_books': Book.objects.all(),
        'all_Authors': Author.objects.all()
    }
    return render(request, 'author.html', context)

# Takes user input for a new author and adds it to the database
def addAuthor(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

# Adds a book to the viewed author
def addbookToAuthor(request, num):
    key = int(num)
    boo = int(request.POST['alist'])
    Author.objects.get(id=key).books.add(Book.objects.get(id=boo))
    return redirect('/authors')

# Takes the user to a new template and allow them to view the details of the selected author
def viewAuthor(request, num):
    key = int(num)
    print(key)
    context = {
        'author': Author.objects.get(id=key).books.all(),
        'viewauthor': Author.objects.get(id=key),
        'Books': Book.objects.all(),
    }
    return render(request, 'authorView.html', context)