from django.urls import path

from . import views

urlpatterns = [
    path('registrarse', views.signup, name='signup'),
    path('iniciar-sesion', views.login, name='login')
]
