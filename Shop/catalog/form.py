from django import forms
from django.forms import ModelForm
from .models import Author, Seria, Genre, PublishingHouse


class SearchForm(forms.Form):
    name = forms.CharField(label="Поиск по названию")


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class SeriaForm(ModelForm):
    class Meta:
        model = Seria
        fields = ['name', 'description']


class PublishingHouseForm(ModelForm):
    class Meta:
        model = PublishingHouse
        fields = ['name']




