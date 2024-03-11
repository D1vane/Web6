from django.urls import path
from water import views

urlpatterns = [
    path ('',views.index),
    path ('dolphine/',views.dolphine),
    path ('shark/',views.shark),
    path ('jellyfish/',views.jellyfish),
    path('dolphine/<slug:dolphine_slug>/', views.dolphine_by_slug),
    path('shark/<slug:shark_slug>/', views.shark_by_slug),
    path('jellyfish/<slug:jellyfish_slug>/', views.jellyfish_by_slug),
]