from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('earth/',include('earth.urls'), name='earth'),
    path('water/',include('water.urls'), name='water'),
    path('underground/',include('underground.urls'), name='underground'),
    path('air/',include('air.urls'), name='air'),
]