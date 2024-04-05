from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Earth,Earth_Kinds
# Create your views here.
def index(request):
        data = {'title': 'Наземные обитатели',
                'header': 'Виды наземных животных',
                'data_inf': Earth_Kinds.objects.all()}
        return render(request, 'earth/earth.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Earth_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Earth.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'earth/earth_animals.html', data_animal)
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Earth, page_name=animal_slug)
    classes = get_object_or_404(Earth_Kinds, slug=class_slug)
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': an.unique_fact.content
               }
    return render(request, 'earth/earth_animal_view.html', data_an)
