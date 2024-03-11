from django.urls import path
from earth import views

urlpatterns = [
    path ('',views.index),
    path ('wolf/',views.wolf),
    path ('rabbit/',views.rabbit),
    path ('fox/',views.fox),
    path('wolf/<slug:wolf_slug>/', views.wolf_by_slug),
    path('rabbit/<slug:rabbit_slug>/', views.rabbit_by_slug),
    path('fox/<slug:fox_slug>/', views.fox_by_slug),
]