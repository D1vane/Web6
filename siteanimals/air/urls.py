from django.urls import path
from air import views

urlpatterns = [
    path ('',views.index),
    path('<slug:cat_slug>/', views.show_cats)
]