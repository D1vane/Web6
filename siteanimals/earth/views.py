from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
        data_inf = [{'kinds': 'Волк', 'name': 'wolf'},
                    {'kinds': 'Заяц', 'name': 'rabbit'},
                    {'kinds': 'Лиса', 'name': 'fox'}
                    ]
        data = {'title': 'Наземные обитатели',
                'header': 'Виды наземных животных',
                'data_inf': data_inf}
        return render(request, 'earth/earth.html', data)
def wolf (request):
    return HttpResponse("<h1>Волк</h1>")
def rabbit (request):
    return HttpResponse("<h1>Заяц</h1>")
def fox (request):
    return HttpResponse("<h1>Лиса</h1>")
def wolf_by_slug(request,wolf_slug):
    return HttpResponse(f"<h1>Виды волков</h1><h3>slug:{wolf_slug}</h3>")
def rabbit_by_slug(request,rabbit_slug):
    return HttpResponse(f"<h1>Виды зайцев</h1><h3>slug:{rabbit_slug}</h3>")
def fox_by_slug(request,fox_slug):
    return HttpResponse(f"<h1>Виды лис</h1><h3>slug:{fox_slug}</h3>")
