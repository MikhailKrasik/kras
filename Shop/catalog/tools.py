from django.db import models
from data.models import *
from books.models import *

def c_author(obj1, obj2):
    c_author = Author(first_name=obj1, last_name=obj2)
    c_author.save()

def c_genre(obj1): 
    c_genre = Genre(name=obj1)
    c_genre.save()

def c_series(obj1, obj2): 
    c_series = Seria(name=obj1, description=obj2)
    c_series.save()

def c_publish(obj1, obj2:
    c_publish = PublishingHouse(name=obj1)
    c_publish.save()


def delfunc(fc_name, pk_key):
    print(fc_name)
    fc_name.objects.get(pk=pk_key).delete()


def obj_count1():
    objcount1 = Author.objects.all()
    print (len(objcount1))

def create_data():
    a_list = []
    for i in range(1, 100)):
        obj = Genre(name='Жанр ' + i)
        a_list.append(obj)
    Genre.objects.bulk_create(a_list)

def count_data(table_name):
    data = table_name.objects.count()

def create_book(bk):
    obj = Book(
        name=bk['name'],
        price=bk['price'],
        year=bk['year'],
        page=bk['page'],
        isbn=bk['isbn'],
        weight=bk['weight'],
        age_limit=bk['age_limit'],
        book_amount=bk['amount'],
        available=bk['available'],
        rate=bk['rate'])
    obj.serie = Series.objects.get(name=bk['serie_name'])
    obj.bind = Binding.objects.get(binding_type=bk['type'])
    obj.publish=PublishingHouse.objects.get(name = bk['publish_name'])
    obj.save()
    aut  = Author.objects.get(pk=bk['author_pk'])
    genr = Genre.objects.get(name=bk['genre_name'])
    obj.author.add(aut)
    obj.genre.add(genr)

    new_book = {
        'name': 'Book',
        'price': 25,
        'year': 2000,
        'page': 132,
        'isbn': '111111',
        'weight': 21,
        'age_limit': 15,
        'amount': 2,
        'available': True,
        'rate': 4,
        'serie_name': '11111',
        'type': 'Твердый переплет',
        'size_pk': 12,
        'publish_name': 'Амаз',
        'author_pk': 2,
        'genre_name': 'Love}


def upd_or_cr(name):
    obj. created = Seria.objects.update_or_create(name=name)
    

def books_list(book_name, key):
    obj = book_name.objects.get(pk=key)
    for i in obj.books.all():
        print(i)
