from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect, reverse
from .models import Earth,Earth_Kinds,EarthTags,Earth_Facts
from .earth_forms_models import AddAnimalForm
from django.views import View
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
class EarthHome(TemplateView):
    template_name = 'earth/earth.html'
    extra_context = {
        'title': 'Наземные обитатели',
        'header': 'Виды наземных животных',
        'data_inf': Earth_Kinds.objects.all()
    }
class EarthCats (ListView):
    model = Earth
    template_name = 'earth/earth_animals.html'
    context_object_name = 'content'
    allow_empty = False
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['content'][0].class_of_animal
        context['title'] = f'Класс: {cat.name}'
        context['header'] = cat.name
        return context
    def get_queryset(self):
        return Earth.objects.filter(class_of_animal__slug=self.kwargs['cat_slug']).select_related('class_of_animal')

def show_animals(request, animal_slug, class_slug):
    an = get_object_or_404(Earth, page_name=animal_slug)
    classes = get_object_or_404(Earth_Kinds, slug=class_slug)
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
    return render(request, 'earth/earth_animal_view.html', data_an)
class Show_Tags(DetailView):
    model = Earth
    template_name = 'earth/earth_animal_view.html'
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
        return get_object_or_404(Earth,page_name=self.kwargs[self.slug_url_kwarg])
def show_tags(request, earth_tag_slug):
    tag = get_object_or_404(EarthTags, slug=earth_tag_slug)
    data_tags = {
        'title': f'Тег: {tag.tag}',
        'header': tag.tag,
        'content': Earth.objects.filter(tags=tag.id)
        }
    return render(request, 'earth/earth_animals.html', data_tags)

class FormAdd_Animal(PermissionRequiredMixin,LoginRequiredMixin,DataMixin,CreateView):
    permission_required = 'earth.add_earth'
    template_name = 'earth/earth_addpage.html'
    success_url = reverse_lazy('home_earth')
    fields = '__all__'
    title_page = 'Добавление животного'
    def form_valid(self, form):
        e = form.save(commit=False)
        e.author = self.request.user
        return super().form_valid(form)

class FormUpdate_Animal(PermissionRequiredMixin,LoginRequiredMixin,DataMixin,UpdateView):
    model = Earth
    permission_required = 'earth.change_earth'
    fields = ['animal','content','is_red_book','class_of_animal','unique_fact','tags','image']
    template_name = 'earth/earth_addpage.html'
    success_url = reverse_lazy('home_earth')
    title_page = 'Редактирование животного'
    context_object_name = 'content'
    slug_url_kwarg = 'animal_slug'
    def get_queryset(self):
        return Earth.objects.filter(class_of_animal__slug=self.kwargs['cat_slug']).select_related('class_of_animal')
    def get_object(self, queryset=None):
        return get_object_or_404(Earth,page_name=self.kwargs[self.slug_url_kwarg])

class FormDelete_Animal(PermissionRequiredMixin,LoginRequiredMixin,DataMixin,DeleteView):
    permission_required = 'earth.delete_earth'
    template_name = 'earth/earth_addpage.html'
    success_url = reverse_lazy('home_earth')
    title_page = 'Удаление животного'
    context_object_name = 'content'
    slug_url_kwarg = 'animal_slug'

    def get_queryset(self):
        return Earth.objects.filter(class_of_animal__slug=self.kwargs['cat_slug']).select_related('class_of_animal')

    def get_object(self, queryset=None):
        return get_object_or_404(Earth, page_name=self.kwargs[self.slug_url_kwarg])

