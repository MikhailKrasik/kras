# Generated by Django 2.2 on 2019-04-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0022_auto_20190409_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rate',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Рейтинг'),
        ),
    ]
