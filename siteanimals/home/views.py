from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data_inf = [{'content':'Наземные животные','kinds':'Виды наземных животных','name': 'earth'},
                {'content':'Подземные животные','kinds':'Виды подземных животных','name': 'underground'},
                {'content':'Водные животные','kinds':'Виды водных животных','name': 'water'},
                {'content':'Воздушные животные','kinds':'Виды воздушных животных','name': 'air'}
                ]
def index (request):
    data = {'title': 'Животные мира',
            'header': 'Классификация по среде обитания'}
    return render(request,'home/main_page.html',data)
def page_not_found(request,exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")