from django.urls import path
from earth import views

urlpatterns = [
    path ('',views.index,name='home'),
    path ('addpage/',views.add_animal),
    path('tag/<slug:earth_tag_slug>/', views.show_tags, name='tag'),
    path ('<slug:cat_slug>/',views.show_cats),
    path ('<slug:class_slug>/<slug:animal_slug>/',  views.show_animals, name = 'animals'),
    path ('tag/<slug:earth_tag_slug>/<slug:animal_slug>/',  views.show_animals_tags, name = 'animals_tag')
]