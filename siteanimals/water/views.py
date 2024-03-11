from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    data_inf = [{'kinds': 'Дельфин', 'name': 'dolphine'},
                {'kinds': 'Акула', 'name': 'shark'},
                {'kinds': 'Медуза', 'name': 'jellyfish'}
                ]
    data = {'title': 'Водные обитатели',
            'header': 'Виды водных животных',
            'data_inf': data_inf}
    return render(request, 'water/water.html', data)
def dolphine (request):
    return HttpResponse("<h1>Дельфин</h1>")
def shark (request):
    return HttpResponse("<h1>Акула</h1>")
def jellyfish (request):
    return HttpResponse("<h1>Медуза</h1>")
def dolphine_by_slug(request,dolphine_slug):
    return HttpResponse(f"<h1>Виды дельфинов</h1><h3>slug:{dolphine_slug}</h3>")
def shark_by_slug(request,shark_slug):
    return HttpResponse(f"<h1>Виды акул</h1><h3>slug:{shark_slug}</h3>")
def jellyfish_by_slug(request,jellyfish_slug):
    return HttpResponse(f"<h1>Виды медуз</h1><h3>slug:{jellyfish_slug}</h3>")