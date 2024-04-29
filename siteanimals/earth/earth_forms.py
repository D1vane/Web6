from django import forms
from .models import Earth_Kinds
from django.core.validators import MinLengthValidator,MaxLengthValidator,deconstructible,ValidationError

@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя-.,: "
    code = 'russian'
    def __init__(self,message=None):
        self.message = message if message else ("Должны присутстовать только русские буквы,'.', ',', "
                                                "'-',':' и пробел.")
    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message,code=self.code,params={"value":value})


class AddAnimalForm(forms.Form):
    def clean_animal(self):
        animal = self.cleaned_data['animal']
        ALLOWED_SYMBOLS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя- "

        if not (set(animal) <= set(ALLOWED_SYMBOLS)):
            raise ValidationError("Должны присутстовать только русские буквы,дефис и пробел.")
        return animal

    animal = forms.CharField(max_length=255, label="Животное")
    page_name = forms.SlugField(max_length=255,label="URL",
                                validators=[MaxLengthValidator(100,message="Максимум 100 символов")])
    content = forms.CharField(widget=forms.Textarea,label="Информация о животном",
                              validators= [MinLengthValidator(10,message="Минимум 10 символов"),RussianValidator()])
    is_red_book = forms.BooleanField(required=False,label="Занесен в красную книгу")
    class_of_animal = forms.ModelChoiceField(queryset=Earth_Kinds.objects.all(),label="Класс животного",
                                             empty_label="Выбрать класс")