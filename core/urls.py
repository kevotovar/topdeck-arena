from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('acerca-de', views.about, name='about'),
]
