from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.template import loader
from miempresa.models import *
from miempresa.forms import *
# from miempresa.models import Curso
# from miempresa.forms import CursoFormulario


def inicio(request):
    return render(request,'miempresa/inicio.html')


# Clientes

def registrarcliente(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            nombrecompleto = miFormulario.cleaned_data['nombrecompleto']
            empresa = miFormulario.cleaned_data['empresa']
            contratacion = miFormulario.cleaned_data['contratacion']
            Cliente(nombrecompleto=nombrecompleto, empresa=empresa, contratacion=contratacion).save()
            return render(request, "miempresa/registrarcliente.html")
    elif request.method == "GET":
        miFormulario = ClienteFormulario()
    
    else:
        return HttpResponseBadRequest("Error. No conzco ese método para esta request")
    
    return render(request, 'miempresa/registrarcliente.html', {'miFormulario':miFormulario})

def buscarcliente(request):
    return render(request,"miempresa/clientes.html")
    
def buscadocliente(request):
    if request.GET['buscar']:
        empresa = request.GET['buscar']
        clientes = Cliente.objects.filter(empresa__contains = empresa)
        return render(request, "miempresa/resultadocliente.html", {"nombrecompleto":clientes,"empresa":empresa})
    else:
        respuesta = "No enviaste datos"
    
    return render(request,'miempresa/resultadocliente.html',{'respuesta': respuesta})


# Empleados

def empleados(request):
        return render(request,'miempresa/empleados.html')

def registrarempleado(request):
    if request.method == 'POST':
        miFormulario = EmpleadoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            nombrecompleto = miFormulario.cleaned_data['nombrecompleto']
            puesto = miFormulario.cleaned_data['puesto']
            contratacion = miFormulario.cleaned_data['contratacion']
            sueldo = miFormulario.cleaned_data['sueldo']
            Empleado(nombrecompleto=nombrecompleto, puesto=puesto, contratacion=contratacion, sueldo=sueldo).save()
            return render(request, "miempresa/registrarempleado.html")
    elif request.method == "GET":
        miFormulario = EmpleadoFormulario()
    
    else:
        return HttpResponseBadRequest("Error. No conzco ese método para esta request")
    
    return render(request, 'miempresa/registrarempleado.html', {'miFormulario':miFormulario})

def buscarempleado(request):
    return render(request,"miempresa/empleados.html")
    
def buscadoempleado(request):
    if request.GET['buscare']:
        nombre = request.GET['buscare']
        empleados = Empleado.objects.filter(nombrecompleto__contains = nombre)
        return render(request, "miempresa/resultadoempleado.html", {"nombrecompleto":empleados,"empresa":'empresa'})
    else:
        respuesta = "No enviaste datos"
    
    return render(request,'miempresa/resultadoempleado.html',{'respuesta': respuesta})

# Proyectos

def proyectos(request):
        return render(request,'miempresa/proyectos.html')

def registrarproyecto(request):
    if request.method == 'POST':
        miFormulario = ProyectoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            cliente = miFormulario.cleaned_data['cliente']
            actividad = miFormulario.cleaned_data['actividad']
            fechasolicitud = miFormulario.cleaned_data['fechasolicitud']
            fechalimite = miFormulario.cleaned_data['fechalimite']
            Proyecto(cliente=cliente, actividad=actividad, fechasolicitud=fechasolicitud, fechalimite=fechalimite).save()
            return render(request, "miempresa/registrarproyecto.html")
    elif request.method == "GET":
        miFormulario = ProyectoFormulario()
    
    else:
        return HttpResponseBadRequest("Error. No conzco ese método para esta request")
    
    return render(request, 'miempresa/registrarproyecto.html', {'miFormulario':miFormulario})

def buscarproyecto(request):
    return render(request,"miempresa/clientes.html")
    
def buscadoproyecto(request):
    if request.GET['buscarp']:
        actividad = request.GET['buscarp']
        proyectos = Proyecto.objects.filter(actividad__contains = actividad)
        return render(request, "miempresa/resultadocliente.html", {"nombrecompleto":proyectos,"Actividad":actividad})
    else:
        respuesta = "No enviaste datos"
    
    return render(request,'miempresa/resultadocliente.html',{'respuesta': respuesta})