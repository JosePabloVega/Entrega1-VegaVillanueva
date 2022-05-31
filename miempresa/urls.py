from django.urls import path
from miempresa import views
from miempresa.views import *

urlpatterns = [
    path('', views.inicio),
    path('clientes', views.buscarcliente),
    path('empleados', views.empleados),
    path('proyectos', views.proyectos),
    path('registrarcliente', views.registrarcliente),
    path('registrarempleado', views.registrarempleado),
    path('registrarproyecto', views.registrarproyecto),
    path('resultadocliente', views.buscadocliente),
    path('resultadoempleado', views.buscadoempleado),
    path('resultadoproyecto', views.buscadoproyecto),

]