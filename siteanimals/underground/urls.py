from django.urls import path,register_converter
from underground import views,converters

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path ('',views.index),
    path ('mole/',views.mole),
    path ('marmot/',views.marmot),
    path ('pdog/',views.prairie_dog),
    path('mole/<slug:mole_slug>/', views.mole_by_slug),
    path('marmot/<slug:marmot_slug>/', views.marmot_by_slug),
    path('pdog/<slug:pdog_slug>/', views.pdog_by_slug),
    path('mole_population/<year4:year>/',views.mole_population),
]