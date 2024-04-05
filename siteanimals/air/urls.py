from django.urls import path
from air import views

urlpatterns = [
    path ('',views.index),
    path('<slug:cat_slug>/', views.show_cats),
    path ('<slug:class_slug>/<slug:animal_slug>/',  views.show_animals, name = 'animals')
]