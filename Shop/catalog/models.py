from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(
       'Имя',
        max_length=200)
    last_name = models.CharField(
        'Фамилия',
        max_length=200)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

# 4.1.5.Серия - ​справочник


class Seria(models.Model):
    name = models.CharField(
        'Серия',
        max_length=200)
    description = models.TextField(
        'Описание',
        max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

# 4.1.14.Издательство - ​справочник


class PublishingHouse(models.Model):
    name = models.CharField(
        'Название издательства',
        max_length=200)
    description = models.TextField(
        'Описание',
        max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Genre(models.Model):
    name = models.CharField(
        'Название жанра',
        max_length=200)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
