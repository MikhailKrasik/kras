from django.db import models
#4.Карточка Товара
# 4.1.Поля
# 4.# 1.1.Название книги
# 4.1.2.Фото обложки
# 4.1.3.Цена (BYN)
# 4.1.4.Авторы книги (может содержать несколько авторов) - ​справочник+
# 4.1.5.Серия - ​справочник+
# 4.1.6.Жанры (один или несколько жанров) - ​справочник +
# 4.1.7.Год издания
# 4.1.8.Страниц
# 4.1.9.Переплет
# 4.1.10.Формат
# 4.1.11.ISBN
# 4.1.12.Вес (гр)
# 4.1.13.Возрастные ограничения
# 4.1.14.Издательство - ​справочник+
# 4.1.15.Количество книг в наличии
# 4.1.16.Активный (доступен для заказа, Да/Нет)
# 4.1.17.Рейтинг (0 - 10)
# 4.1.18.Дата внесения в каталог
# 4.1.19.Дата последнего изменения карточки


# 4.1.4.Авторы книги (может содержать несколько авторов) - ​справочник+

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

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'






     








# Create your models here.
