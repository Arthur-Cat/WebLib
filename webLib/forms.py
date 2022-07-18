import email
from django import forms


class SearchAuthor(forms.Form):
    author_uuid = forms.UUIDField(label="Ключ автора", required=False)
    

class PostAuthor(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, required=False)
    age = forms.IntegerField(label='Возраст', required=False)
    email = forms.EmailField(label='Эл. почта', required=False)