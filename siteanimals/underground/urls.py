from django.urls import path,register_converter
from underground import views,converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path ('',views.index),
    path('<slug:cat_slug>/', views.show_cats,name='cats'),
    path ('<slug:class_slug>/<slug:animal_slug>/',  views.show_animals, name = 'animals')
]