from django.urls import path
from miempresa import views
from miempresa.views import *

urlpatterns = [
    path('', views.inicio),
    path('clientes', views.clientes),
    path('empleados', views.empleados),
    path('proyectos', views.proyectos),
]