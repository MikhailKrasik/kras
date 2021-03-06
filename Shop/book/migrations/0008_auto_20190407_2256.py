# Generated by Django 2.2 on 2019-04-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_cover_format'),
        ('book', '0007_auto_20190407_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ManyToManyField(to='catalog.Cover', verbose_name='Переплет'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='forma',
        ),
        migrations.AddField(
            model_name='book',
            name='forma',
            field=models.ManyToManyField(to='catalog.Format', verbose_name='Формат'),
        ),
    ]
