from django.urls import path
from webLib import views

urlpatterns = [
    path('', views.main, name='webLib'),
    path('authors', views.authors, name='authors'),
    path('<uuid:pk>', views.author_id, name='author_id'),     
    path('<int:pk>', views.book_title, name='book_title'),    
    path('books', views.books, name='books'),
    path('about', views.about, name='about'),
    path('create_book', views.create_book, name='create_book'),
    path('create_<int:pk>', views.update_book, name='update_book'),
    path('del_<int:pk>', views.delete_book, name='delete_book'),
]