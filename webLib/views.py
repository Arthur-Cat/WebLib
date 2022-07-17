from django.shortcuts import render
from webLib.models import Author, Book

def main(request):
    return render(request, 'webLib/main.html')

def authors(request):
    all_authors = {'authors': Author.objects.all()}
    return render(request, 'webLib/authors.html', all_authors)

def author_id(request, pk):
    author = Author.objects.get(pk=pk)
    books_amout = author.book_set.count()
    found_author = {'author': author, 'books_amout': books_amout}
    return render(request, 'webLib/author_id.html', found_author)

def books(request):    
    all_books = {'books': Book.objects.all()}
    return render(request, 'webLib/books.html', all_books)

def book_title(request, title_1):
    book = Book.objects.get(title_1=title_1)
    all_books = {'book': book}
    return render(request, 'webLib/book_title.html', all_books)

def about(request):
    return render(request, 'webLib/about.html')

