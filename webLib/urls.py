from django.urls import path
from webLib.views import main, authors, books, about

urlpatterns = {
    path('', main, name='webLib'),
    path('authors', authors, name='authors'),
    path('books', books, name='books'),
    path('about', about, name='about'),
}