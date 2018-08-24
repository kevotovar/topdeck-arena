from django.urls import path

from . import views

urlpatterns = [
    path('iniciar-sesion', views.login, name='login'),
    path('cerrar-sesion', views.logout_view, name='logout'),
]
