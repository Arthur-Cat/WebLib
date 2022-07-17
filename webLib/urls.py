from django.urls import path
from webLib.views import main, authors, books, about, author_id, book_title

urlpatterns = [
    path('', main, name='webLib'),
    path('authors', authors, name='authors'),
    path('authors/<uuid:pk>', author_id, name='author_id'),     
    path('books/<int:pk>', book_title, name='book_title'),    
    path('books', books, name='books'),
    path('about', about, name='about'),
]