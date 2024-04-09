import datetime

from django.contrib import admin
from .models import Earth,Earth_Facts
from django.db import models
class SizeFilter(admin.SimpleListFilter):
    title = 'Размер поста'
    parameter_name = 'size_of_post'
    def lookups(self, request, model_admin):
        return [
            ('small',('Маленькая (<1000 символов)')),
            ('medium',('Средняя (1000-5000 символов)')),
            ('large',('Большая (>5000 символов)'))
            ]
    def queryset(self, request, queryset):
        if self.value() == 'small':
            return queryset.filter()
        if self.value() == 'medium':
            return queryset.filter()
        if self.value() == 'large':
            return queryset.filter()
@admin.register(Earth)
class EarthAdmin(admin.ModelAdmin):
    # Отображение полей
    list_display = ('id', 'animal', 'time_create','is_red_book','class_of_animal','count_symbols','name_to_slug')
    # Ссылка для перехода к записи
    list_display_links = ('id', 'animal')
    # Сортировка
    ordering = ['time_create','animal']
    # Редактируемые поля
    list_editable = ('is_red_book',)
    # Количество записей на одной странице
    list_per_page = 5
    actions = ['set_red_book','delete_red_book']
    search_fields = ['animal','class_of_animal__name']
    list_filter= [SizeFilter,'class_of_animal__name','is_red_book']
    @admin.display(description= "Количество символов")
    def count_symbols(self,earth:Earth):
        return f"Содержит {len(earth.content)+len(earth.unique_fact.content)} символов."
    @admin.display(description="Совпадение длины слага с именем")
    def name_to_slug(self, earth:Earth):
        temp = "Нет"
        if (len(earth.animal)==len(earth.page_name)):
            temp = "Да"
        else:
            temp = "Нет"
        return temp
    @admin.action(description = "Занести в красную книгу")
    def set_red_book(self,request,queryset):
        count = queryset.update(is_red_book=Earth.Status.RARE)
        self.message_user(request,f"Изменено {count} записи(ей).")

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
