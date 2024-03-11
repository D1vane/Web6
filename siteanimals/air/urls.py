from django.urls import path
from air import views

urlpatterns = [
    path ('',views.index),
    path ('pigeon/',views.pigeon,name='pigeon'),
    path ('rook/',views.rook,name='rook'),
    path ('seagull/',views.seagull,name='seagull'),
    path('pigeon/<slug:pigeon_slug>/', views.pigeon_by_slug),
    path('rook/<slug:rook_slug>/', views.rook_by_slug),
    path('seagull/<slug:seagull_slug>/', views.seagull_by_slug),
]