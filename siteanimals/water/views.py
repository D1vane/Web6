from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Water,Water_Kinds,WaterTags
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
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'tags': an.tags.all()
               }
    return render(request, 'water/water_animal_view.html', data_an)
def show_animals_tags(request, animal_slug, water_tag_slug):
    an = get_object_or_404(Water, page_name=animal_slug)
    tags_id = get_object_or_404(WaterTags, slug=water_tag_slug)
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'tags': an.tags.all()
               }
    return render(request, 'water/water_animal_view.html', data_an)
def show_tags(request, water_tag_slug):
    tag = get_object_or_404(WaterTags, slug=water_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Water.objects.filter(tags=tag.id)
        }
    return render(request, 'water/water_animals.html', data_tags)