from django.urls import path
from water import views

urlpatterns = [
    path ('',views.WaterHome.as_view(),name='home_water'),
    path ('addpage/',views.FormAdd_Animal.as_view(),name='add_page'),
    path('editpage/<int:pk>/', views.FormUpdate_Animal.as_view(), name='edit_page'),
    path('deletepage/<int:pk>/', views.FormDelete_Animal.as_view(), name='delete_page'),
    path('tag/<slug:water_tag_slug>/', views.show_tags, name='tag'),
    path ('<slug:cat_slug>/',views.WaterCats.as_view(),name ='cats'),
    path ('<slug:class_slug>/<slug:animal_slug>/',  views.show_animals, name = 'animals'),
    path ('tag/<slug:earth_tag_slug>/<slug:animal_slug>/',  views.Show_Tags.as_view(), name = 'animals_tag')


]