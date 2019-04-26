
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from catalog.form import *
from django.shortcuts import render
from catalog.models import *
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


class AuthorCreate(CreateView):
    model = Author
    template_name = 'catalog/create_form.html'
    form_class = AuthorForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author-list-view')
        return reverse_lazy('author-create-view')


class GenreCreate(CreateView):
    model = Genre
    template_name = 'catalog/create_form.html'
    form_class = GenreForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre-list-view')
        return reverse_lazy('genre-create-view')


class SeriaCreate(CreateView):
    model = Seria
    template_name = 'catalog/create_form.html'
    form_class = SeriaForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('sera-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('seria-list-view')
        return reverse_lazy('seria-create-view')


class PublishingHouseCreate(CreateView):
    model = PublishingHouse
    template_name = 'catalog/create_form.html'
    form_class = PublishingHouseForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publishinghouse-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publishinghouse-list-view')
        return reverse_lazy('publishinghouse-create-view')



class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'catalog/update_form.html'
    form_class = AuthorForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author-list-view')
        return reverse_lazy('author-update-view')


class GenreUpdate(UpdateView):
    model = Genre
    template_name = 'catalog/update_form.html'
    form_class = GenreForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre-list-view')
        return reverse_lazy('genre-update-view')


class SeriaUpdate(UpdateView):
    model = Seria
    template_name = 'catalog/update_form.html'
    form_class = SeriaForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('seria-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('seria-list-view')
        return reverse_lazy('seria-update-view')


class PublishingHouseUpdate(UpdateView):
    model = PublishingHouse
    template_name = 'catalog/update_form.html'
    form_class = PublishingHouseForm

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publishinghouse-detail-view', kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publishinghouse-list-view')
        return reverse_lazy('publishinghouse-update-view')
