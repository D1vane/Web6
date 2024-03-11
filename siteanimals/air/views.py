from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
        data_inf = [{'kinds': 'Голубь', 'name': 'pigeon'},
                    {'kinds': 'Грач', 'name': 'rook'},
                    {'kinds': 'Чайка', 'name': 'seagull'}
                    ]
        data = {'title': 'Воздушные обитатели',
                'header': 'Виды воздушных животных',
                'data_inf': data_inf}
        return render(request, 'air/air.html', data)
def pigeon (request):
    return HttpResponse("<h1>Голубь</h1>")
def rook (request):
    return HttpResponse("<h1>Грач</h1>")
def seagull (request):
    return HttpResponse("<h1>Чайка</h1>")
def pigeon_by_slug(request,pigeon_slug):
    return HttpResponse(f"<h1>Виды голубей</h1><h3>slug:{pigeon_slug}</h3>")
def rook_by_slug(request,rook_slug):
    return HttpResponse(f"<h1>Виды грачей</h1><h3>slug:{rook_slug}</h3>")
def seagull_by_slug(request,seagull_slug):
    return HttpResponse(f"<h1>Виды чаек</h1><h3>slug:{seagull_slug}</h3>")