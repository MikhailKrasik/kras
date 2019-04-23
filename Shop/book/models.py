from django.db import models 


class Book(models.Model):
    name = models.CharField(
        'Название книги',
        null=False,
        blank=False,
        max_length=200)

    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2)

    cover_books = models.ImageField(
        'Обложка',
        null=True,
        upload_to='image',
        max_length=200)

    pages = models.IntegerField(
        'Количество страниц',
        null=True)

    authors = models.ManyToManyField(
        'catalog.Author',
        verbose_name = 'Авторы')

    seria = models.ManyToManyField(
        'catalog.Seria',
        related_name='books',
        verbose_name='Серия')

    genre = models.ManyToManyField(
        'catalog.Genre',
        verbose_name='Жанр')

    issue_year = models.IntegerField(
        'Год издания',
        null=True)

    available = models.BooleanField(
        'Доступно для заказа',
        default=True)

    rate = models.IntegerField(
       'Рейтинг',
       choices=list(zip(range(1, 11),
       range(1, 11))), 
       unique=False)

    created_date = models.DateTimeField(
        'Дата создания',
        auto_now=False,
        auto_now_add=True)

    update_date = models.DateTimeField(
        'Дата изменения',
        auto_now=True,
        auto_now_add=False)

    cover = models.CharField(
        'Переплет',
        null=True,
        blank=True,
        max_length=200)

    forma=models.CharField(
        'Формат',
        null=True,
        blank=True,
        max_length=200)

    isbn = models.CharField(
        'ISBN',
        null=True,
        max_length=200)

    weight = models.DecimalField(
        'Вес(гр)',
        max_digits=8,
        decimal_places=1,
        null=True)

    number_of_book = models.IntegerField(
        'Количество книг в наличии',
        null=True)

    restrictons = models.IntegerField(
        'Возрастные ограничения',
        choices=list(zip(range(1, 19),
        range(1, 19))),
        null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
