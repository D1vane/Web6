from django.db import models
# Create your models here.
class RedBookAnimal(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_red_book=Earth.Status.RARE)
class Underground(models.Model):
    class Status(models.IntegerChoices):
        USUAL = 0, 'Распространенное'
        RARE = 1, 'Редкое'
    # Название страницы с животным
    page_name = models.CharField(max_length=255,default='underground')
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
    # Класс животного
    class_of_animal = models.ForeignKey('Underground_Kinds', on_delete=models.PROTECT, null=True)
    # Особенность животного
    unique_fact = models.OneToOneField('Underground_Facts', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='fact')
    # Теги
    tags = models.ManyToManyField('UndergroundTags', blank=True, related_name='tags')


class UndergroundTags(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag


class Underground_Facts(models.Model):
    content = models.TextField(blank=True)


class Underground_Kinds(models.Model):
    # Имя класса
    name = models.CharField(max_length=50, db_index=True)
    # Имя страницы
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class UploadImage(models.Model):
    # Заголовок изображения
    caption = models.CharField(max_length=255)
    # Изображение
    photo = models.ImageField(upload_to='underground/static/images')
