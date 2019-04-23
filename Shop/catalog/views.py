from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from catalog.models import Seria, Author, Genre, PublishingHouse
from catalog.form import SearchForm
from django.shortcuts import render


class SeriaDetail(DetailView):
    model = Seria


class AuthorDetail(DetailView):
    model = Author


class PublishingHouseDetail(DetailView):
    model = PublishingHouse


class GenreDetail(DetailView):
    model = Genre


class SeriaList(ListView):
    model = Seria
    
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search',0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)

        return qs
    
class AuthorList(ListView):
    model = Author 

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if qs.filter(first_name__icontains=search).exists():
            return qs.filter(first_name__icontains=search)

        return qs

class PublishingHouseList(ListView):
    model = PublishingHouse  

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)

        return qs

class GenreList(ListView):
    model = Genre   

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if qs.filter(name__icontains=search).exists():
            return qs.filter(name__icontains=search)

        return qs


class Catalogs(TemplateView):
    model = 'catalog/catalogs.html'


class GenreCreate(CreateView):
    model = Genre
    fields = ['name']
