from django.urls import path
from webLib.views import main, authors, books

urlpatterns = {
    path('', main, name='webLib'),
    path('authors', authors, name='webLib'),
    path('books', books, name='webLib'),
}