from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Water,Water_Kinds
# Create your views here.
def index (request):
    data = {'title': 'Водные обитатели',
            'header': 'Виды водных животных',
            'data_inf': Water_Kinds.objects.all()}
    return render(request, 'water/water.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Water_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Water.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'water/water_animals.html', data_animal)
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Water, page_name=animal_slug)
    classes = get_object_or_404(Water_Kinds, slug=class_slug)
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': an.unique_fact.content
               }
    return render(request, 'water/water_animal_view.html', data_an)