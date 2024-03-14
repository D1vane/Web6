from django.db import models

# Create your models here.
class RedBookAnimal(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_red_book=Air.Status.RARE)
class Air(models.Model):
    class Status(models.IntegerChoices):
        USUAL = 0, 'Распространенное'
        RARE = 1, 'Редкое'
    # Название страницы с животным
    page_name = models.CharField(max_length=255,default='air')
    # Название животного
    animal = models.CharField(max_length=255)
    # Информация о животном
    content = models.TextField(blank=True)
    # Время создания страницы о животном
    time_create = models.DateTimeField(auto_now_add=True)
    # Время обновления информации о животном
    time_update = models.DateTimeField(auto_now=True)
    # Занесено ли животное в красную книгу
    is_red_book = models.BooleanField(choices=Status.choices,default=Status.USUAL)
class UploadImage(models.Model):
    # Заголовок изображения
    caption = models.CharField(max_length=255)
    # Изображение
    photo = models.ImageField(upload_to='air/static/images')
