from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound,Http404
# Create your views here.
def index (request):
    data_inf = [{'kinds': 'Крот', 'name': 'mole'},
                {'kinds': 'Сурок', 'name': 'marmot'},
                {'kinds': 'Луговая собака', 'name': 'pdog'}
                ]
    data = {'title': 'Подземные обитатели',
            'header': 'Виды подземных животных',
            'data_inf': data_inf}
    return render(request, 'underground/underground.html', data)
def mole_population(request,year):
    if (year > 2024 or year < 1900):
        return redirect(index)
    if year == 2000:
        raise Http404()
    return HttpResponse(f"<h1>Численность кротов: </h1><h3>{year}</h3>")
def mole (request):
    return HttpResponse("<h1>Крот</h1>")
def marmot (request):
    return HttpResponse("<h1>Сурок</h1>")
def prairie_dog (request):
    return HttpResponse("<h1>Луговая собачка</h1>")
def mole_by_slug(request,mole_slug):
    if request.GET:
        print (request.GET)
    return HttpResponse(f"<h1>Виды кротов</h1><h3>slug:{mole_slug}</h3>")
def marmot_by_slug(request,marmot_slug):
    print (request.POST)
    return HttpResponse(f"<h1>Виды сурков</h1><h3>slug:{marmot_slug}</h3>")
def pdog_by_slug(request,pdog_slug):
    return HttpResponse(f"<h1>Виды луговых собачек</h1><h3>slug:{pdog_slug}</h3>")
