# Generated by Django 2.2 on 2019-04-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190407_2222'),
        ('book', '0003_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='catalog.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='seria',
            field=models.ManyToManyField(to='catalog.Seria', verbose_name='Серия'),
        ),
    ]
