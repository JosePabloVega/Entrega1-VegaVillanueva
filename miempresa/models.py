from django.db import models

class Empleado(models.Model):
    nombrecompleto = models.CharField(max_length=70)
    puesto = models.CharField(max_length=50)
    contratacion = models.DateField()
    sueldo = models.IntegerField()

class Cliente(models.Model):
    nombrecompleto = models.CharField(max_length=70)
    empresa = models.CharField(max_length=50)
    proyectos = models.IntegerField()

class Proyecto(models.Model):
    cliente = models.CharField(max_length=50)
    actividad = models.CharField(max_length=100)
    fechasolicitud = models.DateField()
    fechalimite = models.DateField()
