from cProfile import label
from .models import Book
from django import forms
from django.forms import widgets


class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Ключ автора", required=False)
    

class PostAuthor(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, required=False)
    age = forms.IntegerField(label='Возраст', required=False)
    email = forms.EmailField(label='Эл. почта', required=False)


class BookForm(forms.ModelForm):
    

    
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            'title': 'Название', 
            'description': 'Описание',
            'page_num': 'Кол-во страниц', 
            'author': 'Писатель', 
            }
        widgets = {'description': widgets.TextInput}