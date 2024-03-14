from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,Http404
from .models import Underground
# Create your views here.
def index (request):
    get_data = Underground.objects.all()
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
    cat = get_object_or_404(Underground, page_name=cat_slug)
    data_animal = { 'title': cat.animal,
             'header': cat.animal,
             'content': cat.content
             }
    return render(request, 'underground/underground_animals.html', data_animal)
