# Generated by Django 4.2.10 on 2024-03-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earth', '0003_earth_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earth',
            name='is_red_book',
            field=models.BooleanField(choices=[(0, 'Распространенное'), (1, 'Редкое')], default=0),
        ),
    ]