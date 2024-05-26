import datetime
from django.contrib import admin
from .models import Earth, Earth_Facts
from django.db import models
from django.utils.html import mark_safe


class FactFilter(admin.SimpleListFilter):
    title = 'Наличие факта'
    parameter_name = 'unique_fact_flag'

    def lookups(self, request, model_admin):
        return [
            ('empty', 'Животные без фактов'),
            ('fact', 'Животные с интересным фактом'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'empty':
            return queryset.filter(unique_fact__isnull=True)
        elif self.value() == 'fact':
            return queryset.filter(unique_fact__isnull=False)


@admin.register(Earth)
class EarthAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ('id', 'animal', 'time_create', 'is_red_book', 'class_of_animal',
                    'count_symbols', 'name_to_slug', 'animal_image')
    # Ссылка для перехода к записи
    list_display_links = ('id', 'animal')
    # Сортировка
    ordering = ['time_create', 'animal']
    # Редактируемые поля
    list_editable = ('is_red_book',)
    # Количество записей на одной странице
    list_per_page = 5
    # Действия
    actions = ['set_red_book', 'delete_red_book']
    # Поле поиска
    search_fields = ['animal', 'class_of_animal__name']
    # Фильтры
    list_filter = [FactFilter,'class_of_animal__name', 'is_red_book']
    # Отображаемые поля
    fields = ['animal','is_red_book','class_of_animal','content','unique_fact','image','animal_image','tags','page_name']
    # Неимзеняемые поля
    readonly_fields = ['page_name','animal_image']
    # Расположение тегов
    filter_vertical = ['tags']
    @admin.display(description="Изображение")
    def animal_image(self,earth:Earth):
        if earth.image:
            return mark_safe(f'<img src={earth.image.url} width="50" height="60">')
        return "Без изображения"
    @admin.display(description="Количество символов")
    def count_symbols(self, earth: Earth):
        if earth.unique_fact is None:
            len_fact=0
        else:
            len_fact = len(earth.unique_fact.content)
        return f"Содержит {len(earth.content) + len_fact} символов."

    @admin.display(description="Совпадение длины слага с именем")
    def name_to_slug(self, earth: Earth):
        temp = "Нет"
        if (len(earth.animal) == len(earth.page_name)):
            temp = "Да"
        else:
            temp = "Нет"
        return temp

    @admin.action(description="Занести в красную книгу")
    def set_red_book(self, request, queryset):
        count = queryset.update(is_red_book=Earth.Status.RARE)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Убрать из красной книги")
    def delete_red_book(self, request, queryset):
        count = queryset.update(is_red_book=Earth.Status.USUAL)
        self.message_user(request, f"Изменено {count} записи(ей).")


# Register your models here.
@admin.register(Earth_Facts)
class FactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')
    ordering = ['id']
    list_per_page = 5
