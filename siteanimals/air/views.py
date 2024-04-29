from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Air, Air_Kinds,AirTags
from .air_forms_models import AddAnimalForm
# Create your views here.
def index(request):
        data = {'title': 'Воздушные обитатели',
                'header': 'Виды воздушных животных',
                'data_inf': Air_Kinds.objects.all()}
        return render(request, 'air/air.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Air_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Air.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'air/air_animals.html', data_animal)
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Air, page_name=animal_slug)
    classes = get_object_or_404(Air_Kinds, slug=class_slug)
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'image': an.image,
               'tags': an.tags.all()
               }
    return render(request, 'air/air_animal_view.html', data_an)
def show_animals_tags(request, animal_slug, air_tag_slug):
    an = get_object_or_404(Air, page_name=animal_slug)
    tags_id = get_object_or_404(AirTags, slug=air_tag_slug)
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'image': an.image,
               'tags': an.tags.all()
               }
    return render(request, 'air/air_animal_view.html', data_an)
def show_tags(request, air_tag_slug):
    tag = get_object_or_404(AirTags, slug=air_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Air.objects.filter(tags=tag.id)
        }
    return render(request, 'air/air_animals.html', data_tags)
def add_animal(request):
    if request.method == 'POST':
        form = AddAnimalForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None,'Ошибка добавления животного')
    else:
        form = AddAnimalForm()
    return render(request, 'air/air_addpage.html', {'title': 'Добавление животного',
                                                        'header': 'Добавление животного',
                                                        'form': form})