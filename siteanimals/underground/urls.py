from django.urls import path,register_converter
from underground import views,converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path ('',views.UndergroundHome.as_view(),name='home_underground'),
    path ('addpage/',views.FormAdd_Animal.as_view(),name='add_page'),
    path('<slug:cat_slug>/<slug:animal_slug>/editpage/', views.FormUpdate_Animal.as_view(), name='edit_page'),
    path('<slug:cat_slug>/<slug:animal_slug>/deletepage/', views.FormDelete_Animal.as_view(), name='delete_page'),
    path('tag/<slug:underground_tag_slug>/', views.show_tags, name='tag'),
    path('<slug:cat_slug>/', views.UndergroundCats.as_view(), name ='cats'),
    path ('<slug:class_slug>/<slug:animal_slug>/',  views.show_animals, name = 'animals'),
    path('tag/<slug:earth_tag_slug>/<slug:animal_slug>/', views.Show_Tags.as_view(), name='animals_tag')

]