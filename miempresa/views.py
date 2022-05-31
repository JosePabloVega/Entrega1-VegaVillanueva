from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
# from miempresa.models import Curso
# from miempresa.forms import CursoFormulario


def inicio(request):
    return render(request,'miempresa/inicio.html')

def clientes(request):
        return render(request,'miempresa/clientes.html')

def empleados(request):
        return render(request,'miempresa/empleados.html')

def proyectos(request):
        return render(request,'miempresa/proyectos.html')
