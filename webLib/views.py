from django.shortcuts import render, redirect
from webLib.models import Author, Book
from webLib.forms import SearchAuthor, PostAuthor

def main(request):
    form = SearchAuthor(request.GET)
    form_post = PostAuthor(request.POST)
    return render(request, 'webLib/main.html', {"form": form, "form_post": form_post})

    

def authors(request):
    if "author_uuid" in request.GET:
        return redirect('author_id', request.GET['author_uuid'])
    if request.method == 'POST':
        data = dict()
        data["name"] = request.POST.get('name')
        data["age"] = request.POST.get('age')
        data["email"] = request.POST.get('email')
        Author.objects.create(**data)
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

def book_title(request, pk):
    book = Book.objects.get(pk=pk)
    all_books = {'book': book}
    return render(request, 'webLib/book_title.html', all_books)

def about(request):
    return render(request, 'webLib/about.html')

