from django.shortcuts import render
from webLib.models import Author, Book

def main(request):
    return render(request, 'webLib/main.html')

def authors(request):
    all_authors = {'authors': Author.objects.all()}
    return render(request, 'webLib/authors.html', all_authors)

def books(request):
    all_books = {'books': Book.objects.all()}
    return render(request, 'webLib/books.html', all_books)