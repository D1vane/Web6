from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Air, Air_Kinds,AirTags
from .air_forms_models import AddAnimalForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
        data = {'title': 'Воздушные обитатели',
                'header': 'Виды воздушных животных',
                'data_inf': Air_Kinds.objects.all()}
        return render(request, 'air/air.html', data)
class AirHome(TemplateView):
    template_name = 'air/air.html'
    extra_context = {
        'title': 'Воздушные обитатели',
        'header': 'Виды воздушных животных',
        'data_inf': Air_Kinds.objects.all()
    }
def show_cats(request, cat_slug):
    cat = get_object_or_404(Air_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Air.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'air/air_animals.html', data_animal)
class AirCats (ListView):
    model = Air
    template_name = 'air/air_animals.html'
    context_object_name = 'content'
    paginate_by = 5
    allow_empty = False
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['content'][0].class_of_animal
        context['title'] = f'Класс: {cat.name}'
        context['header'] = cat.name
        return context
    def get_queryset(self):
        return Air.objects.filter(class_of_animal__slug=self.kwargs['cat_slug']).select_related('class_of_animal')
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Air, page_name=animal_slug)
    classes = get_object_or_404(Air_Kinds, slug=class_slug)
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'image': an.image,
               'tags': an.tags.all()
               }
    return render(request, 'air/air_animal_view.html', data_an)
def show_animals_tags(request, animal_slug, air_tag_slug):
    an = get_object_or_404(Air, page_name=animal_slug)
    tags_id = get_object_or_404(AirTags, slug=air_tag_slug)
    if an.unique_fact is None:
        fact = ""
    else:
        fact = an.unique_fact.content
    data_an = {'title': an.animal,
               'header': an.animal,
               'content': an.content,
               'fact': fact,
               'image': an.image,
               'tags': an.tags.all()
               }
    return render(request, 'air/air_animal_view.html', data_an)
class Show_Tags(DetailView):
    model = Air
    template_name = 'air/air_animal_view.html'
    slug_url_kwarg = 'animal_slug'
    context_object_name = 'animal'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['animal'].animal
        context['header'] = context['animal'].animal
        context['content'] = context['animal'].content
        context['fact'] = context['animal'].unique_fact.content
        context['image'] = context['animal'].image
        context['tags'] = context['animal'].tags.all()
        return context
    def get_object(self, queryset=None):
        return get_object_or_404(Air,page_name=self.kwargs[self.slug_url_kwarg])
def show_tags(request, air_tag_slug):
    tag = get_object_or_404(AirTags, slug=air_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Air.objects.filter(tags=tag.id)
        }
    return render(request, 'air/air_animals.html', data_tags)
def add_animal(request):
    if request.method == 'POST':
        form = AddAnimalForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_air')
            except:
                form.add_error(None,'Ошибка добавления животного')
    else:
        form = AddAnimalForm()
    return render(request, 'air/air_addpage.html', {'title': 'Добавление животного',
                                                        'header': 'Добавление животного',
                                                        'form': form})
class Add_Animal(View):
    def get (self,request):
        form = AddAnimalForm()
        return render(request, 'air/air_addpage.html', {'title': 'Добавление животного',
                                                            'header': 'Добавление животного',
                                                            'form': form})
    def post (self,request):
        form = AddAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_air')
        return render(request, 'air/air_addpage.html', {'title': 'Добавление животного',
                                                            'header': 'Добавление животного',
                                                            'form': form})
class FormAdd_Animal(LoginRequiredMixin,CreateView):
    model = Air
    template_name = 'air/air_addpage.html'
    success_url = reverse_lazy('home_air')
    extra_context = {
        'title': 'Добавление животного',
        'header': 'Добавление животного'
    }
    fields = '__all__'
    def form_valid(self, form):
        a = form.save(commit=False)
        a.author = self.request.user
        return super().form_valid(form)
class FormUpdate_Animal(LoginRequiredMixin,UpdateView):
    model = Air
    fields = ['animal','content','is_red_book','class_of_animal','unique_fact','tags','image']
    template_name = 'air/air_addpage.html'
    success_url = reverse_lazy('home_air')
    extra_context = {
        'title': 'Редактирование животного',
        'header': 'Редактирование животного'
    }
class FormDelete_Animal(LoginRequiredMixin,DeleteView):
    model = Air
    template_name = 'air/air_addpage.html'
    success_url = reverse_lazy('home_air')
    extra_context = {
        'title': 'Удаление животного',
        'header': 'Удаление животного'
    }
