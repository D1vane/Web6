from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,Http404
from .models import Underground,Underground_Kinds,UndergroundTags
from .underground_forms_models import AddAnimalForm
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index (request):
    get_data = Underground_Kinds.objects.all()
    data = {'title': 'Подземные обитатели',
            'header': 'Виды подземных животных',
            'data_inf': get_data}
    return render(request, 'underground/underground.html', data)
class UndergroundHome(TemplateView):
    template_name = 'underground/underground.html'
    extra_context = {
        'title': 'Подземные обитатели',
        'header': 'Виды подземных животных',
        'data_inf': Underground_Kinds.objects.all()
    }
def mole_population(request,year):
    if (year > 2024 or year < 1900):
        return redirect(index)
    if year == 2000:
        raise Http404()
    return HttpResponse(f"<h1>Численность кротов: </h1><h3>{year}</h3>")
def show_cats(request, cat_slug):
    cat = get_object_or_404(Underground_Kinds, slug=cat_slug)
    data_animal = {'title': f'Класс: {cat.name}',
             'header': cat.name,
             'content': Underground.objects.filter(class_of_animal=cat.id)
             }
    return render(request, 'underground/underground_animals.html', data_animal)
class UndergroundCats (ListView):
    model = Underground
    template_name = 'underground/underground_animals.html'
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
        return Underground.objects.filter(class_of_animal__slug=self.kwargs['cat_slug']).select_related('class_of_animal')
def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Underground, page_name=animal_slug)
    classes = get_object_or_404(Underground_Kinds, slug=class_slug)
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
    return render(request, 'underground/underground_animal_view.html', data_an)
class Show_Tags(DetailView):
    model = Underground
    template_name = 'underground/underground_animal_view.html'
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
        return get_object_or_404(Underground,page_name=self.kwargs[self.slug_url_kwarg])
def show_animals_tags(request, animal_slug, underground_tag_slug):
    an = get_object_or_404(Underground, page_name=animal_slug)
    tags_id = get_object_or_404(UndergroundTags, slug=underground_tag_slug)
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
    return render(request, 'underground/underground_animal_view.html', data_an)
def show_tags(request, underground_tag_slug):
    tag = get_object_or_404(UndergroundTags, slug=underground_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Underground.objects.filter(tags=tag.id)
        }
    return render(request, 'underground/underground_animals.html', data_tags)
def add_animal(request):
    if request.method == 'POST':
        form = AddAnimalForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home_underground')
            except:
                form.add_error(None,'Ошибка добавления животного')
    else:
        form = AddAnimalForm()
    return render(request, 'underground/underground_addpage.html', {'title': 'Добавление животного',
                                                        'header': 'Добавление животного',
                                                        'form': form})
class Add_Animal(View):
    def get (self,request):
        form = AddAnimalForm()
        return render(request, 'underground/underground_addpage.html', {'title': 'Добавление животного',
                                                            'header': 'Добавление животного',
                                                            'form': form})
    def post (self,request):
        form = AddAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_underground')
        return render(request, 'underground/underground_addpage.html', {'title': 'Добавление животного',
                                                            'header': 'Добавление животного',
                                                            'form': form})
class FormAdd_Animal(LoginRequiredMixin,CreateView):
    model = Underground
    template_name = 'underground/underground_addpage.html'
    success_url = reverse_lazy('home_underground')
    extra_context = {
        'title': 'Добавление животного',
        'header': 'Добавление животного'
    }
    fields = '__all__'
    def form_valid(self, form):
        u = form.save(commit=False)
        u.author = self.request.user
        return super().form_valid(form)
class FormUpdate_Animal(LoginRequiredMixin,UpdateView):
    model = Underground
    fields = ['animal','content','is_red_book','class_of_animal','unique_fact','tags','image']
    template_name = 'underground/underground_addpage.html'
    success_url = reverse_lazy('home_underground')
    extra_context = {
        'title': 'Редактирование животного',
        'header': 'Редактирование животного'
    }
class FormDelete_Animal(LoginRequiredMixin,DeleteView):
    model = Underground
    template_name = 'underground/underground_addpage.html'
    success_url = reverse_lazy('home_underground')
    extra_context = {
        'title': 'Удаление животного',
        'header': 'Удаление животного'
    }