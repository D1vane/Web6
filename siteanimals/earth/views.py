from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Earth
# Create your views here.
def index(request):
        data = {'title': 'Наземные обитатели',
                'header': 'Виды наземных животных',
                'data_inf': Earth.objects.all()}
        return render(request, 'earth/earth.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Earth, page_name=cat_slug)
    data_animal = { 'title': cat.animal,
             'header': cat.animal,
             'content': cat.content
             }
    return render(request, 'earth/earth_animals.html', data_animal)

