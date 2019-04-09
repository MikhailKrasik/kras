# Generated by Django 2.2 on 2019-04-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190407_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestrictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Возрастные ограничения')),
            ],
            options={
                'verbose_name': 'Возрастное ограничение',
                'verbose_name_plural': 'Возрастные ограничения',
            },
        ),
    ]