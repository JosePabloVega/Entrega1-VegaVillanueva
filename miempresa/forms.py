from django import forms
from django.utils.safestring import mark_safe

class EmpleadoFormulario(forms.Form):
    nombrecompleto = forms.CharField(max_length=70, label = "Nombre completo")
    puesto = forms.CharField(max_length=50)
    contratacion = forms.DateField(label = mark_safe("Fecha de contratación<br />(aaaa-mm-dd)"))
    sueldo = forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombrecompleto = forms.CharField(max_length=70,label="Nombre completo")
    empresa = forms.CharField(max_length=50)
    contratacion = forms.DateField(label = mark_safe("Fecha de contratación<br />(aaaa-mm-dd)"))

class ProyectoFormulario(forms.Form):
    cliente = forms.CharField(max_length=50, label = mark_safe("Cliente<br />(Nombre de la empresa)"))
    actividad = forms.CharField(max_length=100)
    fechasolicitud = forms.DateField(label = mark_safe("Fecha de solicitud<br />(aaaa-mm-dd)"))
    fechalimite = forms.DateField(label = mark_safe("Fecha límite de entrega<br />(aaaa-mm-dd)"))
