from .models import Book
from django import forms
from django.forms import widgets, fields
from django.core import validators
from django.core.exceptions import ValidationError


class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Ключ автора", required=False)
    

class PostAuthor(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, required=False)
    age = forms.IntegerField(label='Возраст', required=False)
    email = forms.EmailField(label='Эл. почта', required=False)


class BookForm(forms.ModelForm):
    title = forms.CharField(
        label='Имя',
        max_length=150,
        required=False,
        validators=[validators.RegexValidator(regex='^.{3,}$')],
        error_messages={'invalid': 'Недостимый формат. Сделайте название больше'}
    )

    
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            'description': 'Описание',
            'page_num': 'Кол-во страниц', 
            'author': 'Писатель', 
            }
        widgets = {'description': widgets.TextInput}


