from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Water
# Create your views here.
def index (request):

    data = {'title': 'Водные обитатели',
            'header': 'Виды водных животных',
            'data_inf': Water.objects.all()}
    return render(request, 'water/water.html', data)
def show_cats(request, cat_slug):
    cat = get_object_or_404(Water, page_name=cat_slug)
    data_animal = { 'title': cat.animal,
             'header': cat.animal,
             'content': cat.content
             }
    return render(request, 'water/water_animals.html', data_animal)