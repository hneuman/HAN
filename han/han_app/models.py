from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import subirArchivo
import django
# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Persona(models.Model):
	nombre_persona =  models.CharField(max_length=100)
	cedula_persona =  models.CharField(max_length=100)

	numero_telefono = models.CharField(max_length=100)
	grupo_asociado =  models.CharField(max_length=100)


class Usuario(models.Model):
	"""
	Description: Modelo Usuario
	"""
	nombre = models.CharField(max_length=100,default='Sin Nombre')
	cedula = models.CharField(max_length=100, default='0000000')
	direccion = models.TextField(default="-----------------")
	codigo_u = models.CharField(max_length=100,default='no Codigo')
	telefono =  models.CharField(max_length=100,default='No Telefono')
	email = models.CharField(max_length=100,default='No Email')
	genero = models.CharField(max_length=100,default='No Genero')
	fecha_nacimiento = models.DateField(auto_now=True)
	nacionalidad = models.CharField(max_length=20, default='V')
	grupo_asociado =  models.CharField(max_length=100, default="sin grupo")

	def __unicode__(self):
		return self.nombre

class Usuario_historial_mensaje(models.Model):
	usuario = models.ForeignKey(Usuario,related_name='historial_usuario')
	tipo_mensaje =  models.CharField(max_length=100)
	numero_telefono = models.CharField(max_length=100)
	contenido_mensaje =  models.TextField()	

	class Meta:
		ordering = ('id',)

	def __unicode__(self):
		return self.numero_telefono + " -> " + self.contenido_mensaje

class Buzon_entrada(models.Model):
	nombre_persona =  models.CharField(max_length=100)
	numero_telefono = models.CharField(max_length=100)
	grupo_asociado =  models.CharField(max_length=100)		
	contenido_mensaje =  models.TextField()	
	def __unicode__(self):
		return self.contenido_mensaje	

class Buzon_pendientes(models.Model):
	nombre_persona =  models.CharField(max_length=100)
	numero_telefono = models.CharField(max_length=100)
	grupo_asociado =  models.CharField(max_length=100)	
	contenido_mensaje =  models.TextField()	
	asignado =  models.BooleanField(default=False)
	asignado_a =  models.CharField(max_length=100,default="")	
	asignado_hora = models.DateTimeField(default=django.utils.timezone.now)

	def __unicode__(self):
		return self.contenido_mensaje	

class Buzon_enviados(models.Model):
	nombre_persona =  models.CharField(max_length=100)
	numero_telefono = models.CharField(max_length=100)
	grupo_asociado =  models.CharField(max_length=100)	
	usuario_envia =  models.CharField(max_length=100,default='')		
	contenido_mensaje =  models.TextField()			
	def __unicode__(self):
		return self.contenido_mensaje	


class Grupo(models.Model):
	nombre_grupo = models.CharField(max_length=100)
	integrantes = models.ManyToManyField(Usuario,related_name='usuario_grupo')

	def __unicode__(self):
		return self.nombre_grupo	

class Usuario_envia(models.Model):
	nombre_usuario_envia =  models.CharField(max_length=100)
	id_usuario_envia =  models.CharField(max_length=100)
	contador = models.IntegerField()

	def __unicode__(self):
		return self.id_usuario_envia	
