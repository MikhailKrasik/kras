# Generated by Django 2.2 on 2019-04-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_agerestrictions'),
        ('book', '0010_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='age_restrictions',
            field=models.ManyToManyField(to='catalog.AgeRestrictions', verbose_name='Возрастные ограничения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Вес(гр)'),
        ),
    ]