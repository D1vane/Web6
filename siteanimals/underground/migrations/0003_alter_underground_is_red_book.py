# Generated by Django 4.2.10 on 2024-03-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('underground', '0002_underground_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='underground',
            name='is_red_book',
            field=models.BooleanField(choices=[(0, 'Распространенное'), (1, 'Редкое')], default=0),
        ),
    ]