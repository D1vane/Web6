from django.urls import path
from water import views

urlpatterns = [
    path ('',views.index),
    path('<slug:cat_slug>/', views.show_cats)
]