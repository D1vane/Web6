from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,Http404
from .models import Underground,Underground_Kinds,UndergroundTags
# Create your views here.
def index (request):
    get_data = Underground_Kinds.objects.all()
    data = {'title': 'Подземные обитатели',
            'header': 'Виды подземных животных',
            'data_inf': get_data}
    return render(request, 'underground/underground.html', data)
def mole_population(request,year):
    if (year > 2024 or year < 1900):
        return redirect(index)
    if year == 2000:
        raise Http404()
    return HttpResponse(f"<h1>Численность кротов: </h1><h3>{year}</h3>")
def show_cats(request, cat_slug):
    cat = get_object_or_404(Underground_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Underground.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'underground/underground_animals.html', data_animal)
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Underground, page_name=animal_slug)
    classes = get_object_or_404(Underground_Kinds, slug=class_slug)
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': an.unique_fact.content,
               'tags': an.tags.all()
               }
    return render(request, 'underground/underground_animal_view.html', data_an)
def show_animals_tags(request, animal_slug, underground_tag_slug):
    an = get_object_or_404(Underground, page_name=animal_slug)
    tags_id = get_object_or_404(UndergroundTags, slug=underground_tag_slug)
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': an.unique_fact.content,
               'tags': an.tags.all()
               }
    return render(request, 'underground/underground_animal_view.html', data_an)
def show_tags(request, underground_tag_slug):
    tag = get_object_or_404(UndergroundTags, slug=underground_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Underground.objects.filter(tags=tag.id)
        }
    return render(request, 'underground/underground_animals.html', data_tags)