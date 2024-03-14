from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Air
# Create your views here.
def index(request):
        data = {'title': 'Воздушные обитатели',
                'header': 'Виды воздушных животных',
                'data_inf': Air.objects.all()}
        return render(request, 'air/air.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Air, page_name=cat_slug)
    data_animal = { 'title': cat.animal,
             'header': cat.animal,
             'content': cat.content
             }
    return render(request, 'air/air_animals.html', data_animal)