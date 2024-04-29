from django.shortcuts import render
from django.http import HttpResponse
from .home_forms import UploadFileForm
from .models import UploadFiles
import uuid
# Create your views here.
data_inf = [{'content':'Наземные животные','kinds':'Виды наземных животных','name': 'earth'},
                {'content':'Подземные животные','kinds':'Виды подземных животных','name': 'underground'},
                {'content':'Водные животные','kinds':'Виды водных животных','name': 'water'},
                {'content':'Воздушные животные','kinds':'Виды воздушных животных','name': 'air'}
                ]
def index (request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {'title': 'Животные мира',
            'header': 'Классификация по среде обитания',
            'form': form}
    return render(request,'home/main_page.html',data)
def page_not_found(request,exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
def handle_uploaded_files(f):
    name = f.name
    ext = ''
    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]
    suffix = str(uuid.uuid4())
    with open (f"uploads/{name}_{suffix}{ext}","wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)