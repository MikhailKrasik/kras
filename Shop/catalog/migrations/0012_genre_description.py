# Generated by Django 2.2 on 2019-04-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_delete_agerestrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
