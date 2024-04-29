from django import forms
from .models import Earth,Earth_Kinds,Earth_Facts
from django.core.validators import ValidationError
class AddAnimalForm(forms.ModelForm):
    def clean_animal(self):
        animal = self.cleaned_data['animal']
        ALLOWED_SYMBOLS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя- "

        if not (set(animal) <= set(ALLOWED_SYMBOLS)):
            raise ValidationError("Должны присутстовать только русские буквы,дефис и пробел.")
        return animal
    def clean_content(self):
        content = self.cleaned_data['content']
        ALLOWED_SYMBOLS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя-.,: "

        if not (set(content) <= set(ALLOWED_SYMBOLS)):
            raise ValidationError("Должны присутстовать только русские буквы,'.', ',', "
                                                "'-',':' и пробел.")
        return content
    class Meta:
        model = Earth
        fields = ['animal','content','is_red_book','class_of_animal','unique_fact','tags']
    class_of_animal = forms.ModelChoiceField(queryset=Earth_Kinds.objects.all(),empty_label="Выбрать класс",
                                             label="Класс животного")
    unique_fact = forms.ModelChoiceField(queryset=Earth_Facts.objects.all(), empty_label="Выбрать факт",
                                             label="Факт о животном")
