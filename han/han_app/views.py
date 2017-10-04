# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from han.han_app.models import Document
from han.han_app.models import *
from han.han_app.forms import DocumentForm
from han.han_app.forms import Form_usuario
from han.han_app.forms import Form_enviar_mensaje
from han.han_app.forms import Form_grupo
from han.han_app.forms import Form_usuario_envia

from django.template.context_processors import csrf
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from django.apps import apps
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from han.han_app.serializers import *
from datetime import datetime
from django.db import transaction

import re
#@api_view(['GET', 'POST'])
class Buzon_pendientesSerializerViewSet(viewsets.ModelViewSet):
	queryset = Buzon_pendientes.objects.all()
	print queryset
	serializer_class = Buzon_pendientesSerializer



class api_enviarSerializer(viewsets.ModelViewSet):
#    if request.method == 'GET':
#	    queryset = Buzon_pendientes.objects.all()
#	    serializer_class = Buzon_pendientesSerializer
    
#    if request.method == 'POST':
	#serializer = Buzon_pendientesSerializer(data=request.data)
	queryset = Buzon_pendientes.objects.all()
	print queryset
	serializer_class = api_enviarSerializer


class Buzon_enviadosSerializerViewSet(viewsets.ModelViewSet):

	queryset = Buzon_enviados.objects.all()
	print queryset
	serializer_class = Buzon_enviadosSerializer


class Usuario_enviaSerializerViewSet(viewsets.ModelViewSet):
	queryset = Usuario_envia.objects.all()
	print queryset
	serializer_class = Usuario_enviaSerializer


@api_view(['GET', 'POST'])
def api_mensajes_listar(request,id=None):
    """
    Listar los mensajes, TODOS, o por cantidad establecida.!
    """
    if request.method == 'GET':
    	if id:
    		#snippets =  buzon_pendientes.objects.get(pk=int(id))
    		snippets = Buzon_pendientes.objects.filter(pk=int(id))
    		snippets = Buzon_pendientes.objects.all()[:id]

    	else:
    		snippets = Buzon_pendientes.objects.all()
        serializer = Buzon_pendientesSerializer(snippets, many=True)
        print serializer.data
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def api_enviar_mensaje(request,id=None,cantidad_sms=int(1)):
	"""
	List all snippets, or create a new snippet.
	"""
	print id , " <<<<< ******* <<<<< "
	print cantidad_sms , " <<<<< ******* <<<<< "
	print request.data
	try:
		if request.method == 'GET':
			#snippets =  buzon_pendientes.objects.get(pk=int(id))
			with transaction.atomic():
				snippets = Buzon_pendientes.objects.select_for_update().filter(asignado=False)[:cantidad_sms]

				serializer = Buzon_pendientesSerializer(snippets, many=True)

				print ">>>>>>>> ", serializer.data, " <<<<<<<"

				print ">>>>>>>> snippets ", snippets, "snippets <<<<<<<"

				for snip in snippets:

					buzon = snip
					###buzon = Buzon_pendientes.objects.filter(snippets)	 	
					buzon.asignado_hora = datetime.now()
					buzon.asignado=True
					buzon.asignado_hora = datetime.now()

					buzon.save()

				serializer = Buzon_pendientesSerializer(snippets, many=True)
				return Response(serializer.data)


		if request.method == 'POST':
			#snippets =  buzon_pendientes.objects.get(pk=int(id))
			print "api_envia_POST"
			try:
				#snippets = Buzon_pendientes.objects.filter(asignado=False)[:1]
				
				if 'cantidad_sms' in request.data:
					cantidad_sms = int(request.data['cantidad_sms'])
				else:
					cantidad_sms = 1

				with transaction.atomic():
					snippets = Buzon_pendientes.objects.select_for_update().filter(asignado=False)[:cantidad_sms]

					for snip in snippets:

						buzon = snip
						###buzon = Buzon_pendientes.objects.filter(snippets)	 	
						buzon.asignado_hora = datetime.now()
						print ">>>>>> >  >  Type %s  < < < < <" %type(snippets)
						buzon.asignado=True
						buzon.asignado_hora = datetime.now()

						try:
							buzon.asignado_a=request.data['usuario_envia']
						except:
							pass
						buzon.save()

					print " >>><<>>>   %s   <<<<<<< !!!! "%(buzon)

					print " en EL POST >>> %s " %snippets
					serializer = Buzon_pendientesSerializer(snippets, many=True)
					
					#snippets.asignado=True
					#	snippets.save()
					print serializer.data
					#transaction.commit()
					return Response(serializer.data)
			except Exception,e:
				print e
				return Response(status=status.HTTP_404_NOT_FOUND)
	except Exception,e:

		print "ERROR  >> api_enviar_mensaje <<< >>> %s " %e
		#buzon = Buzon_pendientes.objects.all()
		#serializer = Buzon_pendientesSerializer(buzon, many=True)
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def api_usuario_envia(request):
	"""
	List all snippets, or create a new snippet.
	"""
	try:
		
		if request.method == 'GET':
			usuario_envia = Usuario_envia.objects.all()[:1]
			serializer = Usuario_enviaSerializer(usuario_envia, many=True)
			print serializer.data
			return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

		if request.method == 'POST':
			print request.data 
			print request.data['usuario_envia']
			#snippets =  buzon_pendientes.objects.get(pk=int(id))
			usuario_envia = Usuario_envia.objects.all().filter(id_usuario_envia=request.data['usuario_envia'])[:1]
			print usuario_envia
			serializer = Usuario_enviaSerializer(usuario_envia, many=True)
			print serializer.data
			return Response(serializer.data,status=status.HTTP_200_OK)

	except Exception,e:
		print " >> api_usuario_envia %s << " %e
		return Response(status=status.HTTP_404_NOT_FOUND)

	return Response(status=status.HTTP_206_PARTIAL_CONTENT)


@api_view(['GET', 'POST'])
def actualizar_enviar_mensaje(request,id=None):
	"""
	List all snippets, or create a new snippet.
	"""
	#id=0
	if id:
		snippets = Buzon_pendientes.objects.all().filter(pk=int(id))[:1]
		serializer = Buzon_pendientesSerializer(snippets, many=True)

	if request.method == 'GET':
		#snippets =  buzon_pendientes.objects.get(pk=int(id))
		try:
			buzon = Buzon_pendientes.objects.all().filter(pk=int(id))[0]
			print ">>>> ", buzon


			d = Buzon_enviados(nombre_persona=buzon.nombre_persona, 
				numero_telefono=buzon.numero_telefono, 
				contenido_mensaje=buzon.contenido_mensaje, 
				)
			d.save()
			buzon.delete()

			return Response(serializer.data,status=status.HTTP_200_OK)

		except Exception,e:
			print e
			return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'POST':
		with transaction.atomic():	
			print request.data 
			print "POR AQUI ANDO"
			snippets = Buzon_pendientes.objects.all().filter(pk=request.data['id'])[:1]
			serializer = Buzon_pendientesSerializer(snippets, many=True)
			
			buzon = Buzon_pendientes.objects.all().filter(pk=request.data['id'])[0]
			print ">>>> ", buzon
			print ">>>> ", snippets

			try:
				usuario_envia = request.data['usuario_envia']
				usuario = Usuario_envia.objects.select_for_update().get(id_usuario_envia=usuario_envia)
				usuario.contador = usuario.contador + 1
				usuario.save()
			except Exception,e:
				print "ERROR >>> %s <<<< " %e
				usuario_envia = ""

			d = Buzon_enviados(nombre_persona=buzon.nombre_persona, 
				numero_telefono=buzon.numero_telefono, 
				contenido_mensaje=buzon.contenido_mensaje, 
				usuario_envia= usuario_envia, 

				)
			d.save()
			buzon.delete()
		
		return Response(serializer.data,status=status.HTTP_200_OK)

		#return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

	return Response(status=status.HTTP_304_NOT_MODIFIED)

"""
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
def pagar_usuario(request,id_usuario=None):
	if request.method == 'GET':
		try:
			usuario = Usuario_envia.objects.get(pk=id_usuario)
			usuario.contador = 0
			usuario.save()
		except Exception,e:
			print "ERROR >>> %s <<<< " %e
			usuario_envia = ""
	personas = Usuario_envia.objects.all()
	return render_to_response("usuario_envia.html",{'documento':personas,'modelo':"usuario_envia"}, RequestContext(request, {}))

def usuario(request):
	personas = Usuario.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	#return render_to_response('list.html', {"contacts": contacts})


	return render_to_response("usuarios.html",{'documento':personas,'modelo':'usuario',},RequestContext(request, {}))


def buzon_entrada(request):
	personas = Buzon_entrada.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)
	#return render_to_response('list.html', {"contacts": contacts})
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Entrada",'modelo':"buzon_entrada"}, RequestContext(request, {}))

def buzon_pendientes(request):
	personas = Buzon_pendientes.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	#return render_to_response('list.html', {"contacts": contacts})
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Pendientes",'modelo':"buzon_pendientes"}, RequestContext(request, {}))

def buzon_enviados(request):
	personas = Buzon_enviados.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	#return render_to_response('list.html', {"contacts": contacts})
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Enviados",'modelo':"buzon_enviados"}, RequestContext(request, {}))

def enviar_mensaje(request):
	d={}
	print " >>>>>>>>>>>> %s  <<<<<<<< "%RequestContext(request)
	if request.method=="POST":

		lista_destinatarios=request.POST.getlist('boton_check')
		destinatarios_lista=""
		d={}
		for l in lista_destinatarios:
			d[l] =  {
				'telefono':Usuario.objects.get(pk=int(l)).telefono,
				'id':Usuario.objects.get(pk=int(l)).id,
				'nombre':Usuario.objects.get(pk=int(l)).nombre,
			}

			destinatarios_lista = destinatarios_lista + Usuario.objects.get(pk=int(l)).telefono + ","

		destinatarios_lista = destinatarios_lista[0:-1]
		print destinatarios_lista

		formulario = Form_enviar_mensaje(initial={'destinatarios':destinatarios_lista})

		print destinatarios_lista

	else:	
		formulario = Form_enviar_mensaje()
		print "whattttt"


	print "aca algooo"
	print request
	return render_to_response("enviar_mensaje.html",{'formulario':formulario,'tipo':"Enviar Mensajes",'destinatarios':d},RequestContext(request, {}))

def enviar_mensaje_procesar(request,destinatarios):
	print "procesar"

	form = Form_enviar_mensaje(request.GET)
	try:
		mensaje = request.POST['mensaje']
	except Exception,e:
		mensaje = ""
	print mensaje	
	#destinatarios = request.POST['destinatarios']
	destinatarios = request.POST.getlist('destinatario')
	print destinatarios
	for d in destinatarios:
		print d
		try:
			usuario = Usuario.objects.all().filter(id=d)[0]
			print usuario
			d = Buzon_pendientes(nombre_persona=usuario.nombre, 
				numero_telefono=usuario.telefono, 
				contenido_mensaje=mensaje, 
				grupo_asociado=usuario.grupo_asociado,
				)
			print "\n\n\n\n>>>>>>>>>>>se proceso el mensaje<<<<<<<<<<<<\n\n\n"
			d.save()
		except Exception,e:
			print e
			d = Buzon_pendientes(nombre_persona="Este Numero No Esta Registrado", 
			numero_telefono=d, 
			contenido_mensaje=mensaje, 
			grupo_asociado=d,
			)
			print "\n\n\n\n\nNO  proceso el mensaje\n\n\n\n\n\n"
			d.save()	

	personas = Buzon_pendientes.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Pendientes",'modelo':'buzon_pendientes'},RequestContext(request, {}))



@csrf_exempt
@api_view(['GET', 'POST'])
def api_bulto_mensaje(request):
	"""
	Agregar mensajes de la API con POST
	
	import requests
	#~ {'data': 
	    #~ [{'numero_telefono': '04145795060', 'nombre_persona': 'Hernan', 'contenido_mensaje': '1 solo mensajito 0'}, 
	    #~ {'numero_telefono': '04145795060', 'nombre_persona': 'Hernan', 'contenido_mensaje': '1 solo mensajito 1'}, 
	    #~ {'numero_telefono': '04145795060', 'nombre_persona': 'Hernan', 'contenido_mensaje': '1 solo mensajito 2'}, 
	    #~ {'numero_telefono': '04145795060', 'nombre_persona': 'Hernan', 'contenido_mensaje': '1 solo mensajito 3'}, 
	    #~ {'numero_telefono': '04145795060', 'nombre_persona': 'Hernan', 'contenido_mensaje': '1 solo mensajito 4'}]
	#~ }

	lista={'data':mensajes}
	headers = {'content-type': 'application/json'}
	print lista
	x = requests.post(url+'api_bulto_mensaje/',data=json.dumps(lista),headers=headers)


	x = requests.post(url+'api_bulto_mensaje/',msj_pendiente)

	"""
	try:
		
		if request.method == 'GET':
			print "------------ GET ---------"
			usuario_envia = Usuario_envia.objects.all()[:1]
			serializer = Usuario_enviaSerializer(usuario_envia, many=True)
			print serializer.data
			return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

		if request.method == 'POST':
			try:
				print "  \n %s \n\n\n" %request.data 
				print "  \n %s \n\n\n" %request.data['data']

				aList = [
					Buzon_pendientes(
					nombre_persona=i['nombre_persona'],
					numero_telefono=i['numero_telefono'],
					contenido_mensaje=i['contenido_mensaje'],
					) for i in request.data['data']
					]

				Buzon_pendientes.objects.bulk_create(aList)

				"""
				for i in request.data['data']:
					print " >>>>>>>>>>>>>>>>>>  ", i 
					d = Buzon_pendientes(
						nombre_persona=i['nombre_persona'], 
						numero_telefono=i['numero_telefono'], 
						contenido_mensaje=i['contenido_mensaje'],
						)
				"""
				#d.save()			
				print "\n\n\n\n>>>>>>>>>>>Agregado Mensaje por enviar<<<<<<<<<<<<\n\n\n"
			except Exception, e:
				print "ERRRRRRRORRRR %s ***************** " %e
			#snippets =  buzon_pendientes.objects.get(pk=int(id))
			#usuario_envia = Buzon_pendientes.objects.all().filter(id_usuario_envia=request.data['usuario_envia'])[:1]
			#print usuario_envia
			#serializer = Usuario_enviaSerializer(usuario_envia, many=True)
			#print serializer.data
			return Response(status=status.HTTP_200_OK)

	except Exception,e:
		print " >> api_usuario_envia %s << " %e
		return Response(status=status.HTTP_404_NOT_FOUND)

	return Response(status=status.HTTP_206_PARTIAL_CONTENT)


def agregar_usuario(request):
	c = {}
	c.update(csrf(request))
	print "agregar "


	if request.method == "POST":
		grupo = Grupo.objects.all()
		form = Form_usuario(request.POST)
		aviso="Verificar los datos"

		print "procesar"
		if form.is_valid():
			print " >>>>>>>>>>>>>>>> %s "%request.POST.getlist('metodo')[0]
			if(request.POST.getlist('metodo')[0]=="nuevo"):
				usuario = Usuario(
					nombre=form.cleaned_data['nombre'],
					telefono=form.cleaned_data['telefono'],
					email=form.cleaned_data['email'],
					grupo_asociado=form.cleaned_data['grupo_asociado'],
					codigo_u=form.cleaned_data['codigo_u'],
					)
				usuario.save()

				lista_grupos=request.POST.getlist('boton_check')
				print " lista_grupos %s " %lista_grupos
				for l in lista_grupos:
					grupo = Grupo.objects.get(pk=int(l))
					grupo.integrantes.add(usuario)
					grupo.save()

				aviso="Usuario Agregado Satisfactoriamente"

			else:
				usuario = Usuario.objects.get(pk=int(request.POST.getlist('metodo')[0]))

				usuario.nombre=form.cleaned_data['nombre']
				usuario.telefono=form.cleaned_data['telefono']
				usuario.email=form.cleaned_data['email']
				usuario.grupo_asociado=form.cleaned_data['grupo_asociado']
				aviso="Usuario Modificado Satisfactoriamente"
				lista_grupos=request.POST.getlist('boton_check')

				print "lista GRUPOS %s"%lista_grupos

				for l in lista_grupos:
					grupo = Grupo.objects.get(pk=int(l))
					grupo.integrantes.add(usuario)
					grupo.save()

				
			usuario.save()

		form = Form_usuario()
		grupos = Grupo.objects.all().order_by('id')

		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':aviso,'metodo':'nuevo','grupos':grupos,'grupos_pertenece':False},RequestContext(request, {}),c)

	else:

		form = Form_usuario()
		print "retornar post"
		grupos = Grupo.objects.all().order_by('id')

		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':"Agregar nuevo usuario",'metodo':'nuevo','grupos':grupos,'grupos_pertenece':False}, RequestContext(request, {}),c)



def usuario_envia(request):
	personas = Usuario_envia.objects.all()

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	#return render_to_response('list.html', {"contacts": contacts})
	return render_to_response("usuario_envia.html",{'documento':personas,'modelo':"usuario_envia"}, RequestContext(request, {}))


def agregar_usuario_envia(request):
	c = {}
	c.update(csrf(request))
	print "agregar "


	if request.method == "POST":
		form = Form_usuario_envia(request.POST)
		aviso="Verificar los datos"

		print "procesar"
		if form.is_valid():
			usuario = Usuario_envia(
				nombre_usuario_envia=form.cleaned_data['nombre_usuario_envia'],
				id_usuario_envia=form.cleaned_data['id_usuario_envia'],
				contador=0,

				)
			usuario.save()

			aviso="Usuario Agregado Satisfactoriamente"


		return render_to_response("agregar_usuario_envia.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':aviso,'metodo':'nuevo','grupos':grupos,'grupos_pertenece':False},RequestContext(request, {}),c)

	else:

		form = Form_usuario_envia()
		print "retornar post"
		return render_to_response("agregar_usuario_envia.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':"Agregar nuevo usuario",'metodo':'nuevo','grupos':grupos,'grupos_pertenece':False}, RequestContext(request, {}),c)



def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def borrar_bandeja(request):
	buzon = Buzon_pendientes.objects.all().delete()
	#for b in buzon:
	personas = Usuario.objects.all()
	return render_to_response("main.html",{'documento':personas})


def func_subir_archivo(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print ">>>>>>>>>> XXXXX %s  XXXXX <<<<<<<<<<< " %form
        print ">>>>>>>>>> XXXXX %s  XXXXX <<<<<<<<<<< " %request.FILES['docfile']
        if form.is_valid():
			newdoc = Document(docfile=request.FILES['docfile'])
			print ">>>>>>>>>> XXXXX %s  XXXXX <<<<<<<<<<< " %newdoc
			documento=request.FILES['docfile'].read()

			#for chunk in request.FILES['docfile'].chunks():
			#	print chunk
			#	documento.append(chunk)
			#print request.FILES['docfile'].read()

			reader = csv.DictReader(form.cleaned_data['docfile'], delimiter=',')
			for row in reader:	

				print " %s :: %s :: %s"%(row['tipo'],row['id_destino'],row['name'])
				print row
				persona = Usuario(grupo_asociado = row['tipo'], nombre = row['id_destino'],telefono = row['name'] )

				#persona.grupo_asociado = row['tipo']
				#persona.nombre = row['id_destino']
				#persona.telefono = row['name']
				persona.save()	
			#print reader

			#entrada = csv.DictReader(request.FILES['docfile'].read(), delimiter=',',)
			#print documento
			#print entrada 
			#for e in entrada:
			#	print e
			#newdoc.save()

			#print documento
			# Redirect to the document list after POST
			#return HttpResponseRedirect(reverse('han.han_app.views.func_subir_archivo'))
			personas = Usuario.objects.all()
			return render_to_response("main.html",{'documento':personas})
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    
    print ">>>>>>>>>> NUEVO %s <<<<<<<<<<< " %form

    # Render list page with the documents and the form
    return render_to_response(
        'main.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def operaciones_globales(request):
	
	if request.method=='POST' and 'eliminar_registros' in request.POST:

		print "eliminar REGISTROS .........."
		#print  " >>> %s <<< "%request.META['HTTP_REFERER']
		return eliminar_registros(request)

	if request.method=='POST' and 'enviar_mensaje' in request.POST:
		print "Enviar Mensajes.........."

		return enviar_mensaje(request)

	#return render_to_response("usuarios.html", RequestContext(request, {}))

def eliminar_registros(request):

	print  " >>> %s <<< "%request.POST
	request.META['CAMPO_XXXXXXXXXXXXXXXXXX']="-.-.-.- -. - . -  . - . - . - . -"
	lista_destinatarios=request.POST.getlist('boton_check')
	print lista_destinatarios
	modelo_vista=request.POST['modelo']
	apps.get_models()
	myapp = apps.get_app_config('han_app')
	#myapp.models	
	index_modelo = myapp.models.keys().index(modelo_vista)

	print " >>> %s <<< "%myapp
	print " >>> %s <<< "%myapp.models
	print " >>> %s <<< "%myapp.models[modelo_vista]
	print " >>> %s <<< "%type(myapp.models.items()[index_modelo][1])

	modelo=myapp.models.items()[index_modelo][1]
	#m = myapp.models.items()[2][1].objects.all()
	for i in lista_destinatarios:
		modelo.objects.filter(id=int(i)).delete()
	
	#m = __import__ ('han.han_app.views')
	#print " >>> %s <<< "%m
	#func = getattr(m,modelo_vista)

	return globals()[modelo_vista](request)

	#return func(request)
	#return render_to_response("usuarios.html", RequestContext(request, {}))

def editar_usuario(request,id_usuario="1"):
	
	c = {}
	c.update(csrf(request))
	print "editar_usuario "
	try:

		u = Usuario.objects.get(pk=int(id_usuario))


		form = Form_usuario(initial={'nombre':u.nombre,
			'grupo_asociado':u.grupo_asociado,
			'telefono':u.telefono,
			'email':u.email,
			'codigo_u':u.codigo_u,

			})

		grupos_pertenece = Grupo.objects.filter(integrantes=id_usuario).values('id').order_by('id')
		print " GRUPOS A LOS Q PERTENECE >>> %s "%grupos_pertenece

		l=[]
		for g in grupos_pertenece:
			l.append(g['id'])
		if len(l) >= 1:
			grupos_pertenece = l
		else:
			grupos_pertenece = False

		print " %s "%grupos_pertenece
		grupos = Grupo.objects.all().order_by('id')
		print " GRUPOSSS  PERTENECE ARMANDO LISTA >>>>> %s "%grupos
		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Editar Usuario",'aviso':"Editar Usuario",'metodo':int(id_usuario),'grupos':grupos,'grupos_pertenece':grupos_pertenece},RequestContext(request, {}),c)

	except Exception,e:
		print e
		form = Form_usuario()
		print "retornar post"
		grupos = Grupo.objects.all().order_by('id')
		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':"El usuario que intentas modificar, no existe",'metodo':'nuevo','grupos':grupos}, RequestContext(request, {}),c)


	return agregar_usuario(request)



def grupos(request):
	c = {}
	c.update(csrf(request))
	print "agregar "
	print "agregar >>> %s"%request

	if request.method == "POST":
		form = Form_grupo(request.POST)
		print "procesar"
		if form.is_valid():
			print " >>>>>>>>>>>>>>>> %s "%request.POST.getlist('metodo')[0]
			# para saber si es un grupo nuevo o se va a editar otro
			if(request.POST.getlist('metodo')[0]=="nuevo"):
				grupo = Grupo(
					nombre_grupo=form.cleaned_data['nombre_grupo'],
					)
				aviso="Grupo Agregado Satisfactoriamente"

			else:
				#usuario = Usuario.objects.get(pk=int(request.POST.getlist('metodo')[0]))

				#usuario.nombre=form.cleaned_data['nombre']
				#usuario.telefono=form.cleaned_data['telefono']
				#usuario.email=form.cleaned_data['email']
				#usuario.grupo_asociado=form.cleaned_data['grupo_asociado']
				aviso="Grupo Modificado Satisfactoriamente"
				print "nada"
				
			grupo.save()
		form = Form_grupo()
		grupo = Grupo.objects.all().order_by('id')

		return render_to_response("grupos.html",{'formulario':form,'tipo':"Agregar Grupo",'aviso':aviso,'metodo':'nuevo','documento':grupo},RequestContext(request, {}),c)

	else:
		form = Form_grupo()
		grupo = Grupo.objects.all().order_by('id')

		print "retornar post"
		return render_to_response("grupos.html",{'formulario':form,'tipo':"Agregar Grupo",'aviso':"Agregar nuevo Grupo",'metodo':'nuevo','documento':grupo}, RequestContext(request, {}),c)

def grupo_usuario(request,id_grupo):
	personas = Usuario.objects.filter(grupo=id_grupo)

	paginator = Paginator(personas, 25) # Show 25 contacts per page

	pagina_actual = request.GET.get('page')

	try:
		personas = paginator.page(pagina_actual)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		personas = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		personas = paginator.page(paginator.num_pages)

	#return render_to_response('list.html', {"contacts": contacts})

	return render_to_response("usuarios.html",{'documento':personas,'modelo':'usuario',},RequestContext(request, {}))


def contactanos(request):
	if request.method == "POST":
		print request.POST
		aviso="Se ha recibido su peticion"
		return render_to_response("contactanos.html",{"aviso":aviso},RequestContext(request, {}))
	else:
		return render_to_response("contactanos.html",RequestContext(request, {}))


def informacion(request):
	return render_to_response("informacion.html",RequestContext(request, {}))

def ingreso(request):
	#if request.method == "POST":
		#return render_to_response("informacion.html",RequestContext(request, {}))

	if request.method == 'POST':
		print "intenta hcer login"
		formulario = AuthenticationForm(request.POST)
		print formulario
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			print clave
			print acceso
			print usuario
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					print " * * * * * * * * ESTA LOGEADO * * ** * * * "
					return render_to_response("login.html",{'mensaje':"Se ha autentificado Satisfactoriamente"},RequestContext(request, {}))

				else:
					print "  -- - - - - - - -  - - - - -no esta activo"
					return render_to_response("login.html", {'mensaje':"Este usuario no esta activo"},RequestContext(request, {}))
			else:
				print " / * /* /* /*/ ** * * */ */ no existe "
				return render_to_response("login.html",{'mensaje':"Este usuario no exite"}, RequestContext(request, {}))
	else:
		print "no hcaer nada, solo mostrar form"	
		return render_to_response("login.html",RequestContext(request, {}))


def crear_usuario(request):
	if request.method == 'POST':
		print "intenta hcer login"
		print request.POST
		print request.POST['username']
		print request.POST['password']
		print request.POST['correo']
		print request.POST['telefono']

		crear_usuario=User.objects.create_user(username=request.POST['username'],
			password=request.POST['password'],
			email=request.POST['correo'],) 

		crear_usuario.save()

	return render_to_response("login.html",{'mensaje':"Usuario Creado Satisfactoriamente"},RequestContext(request, {}))



def buscar_destinatario(mensaje_a_procesar):
	try:
		print "buscar_destinatario"
		print mensaje_a_procesar
		nro_destino = ""
		patron_hm_id = "HM_ID:#\w*"
		codigo_u = re.findall(patron_hm_id,mensaje_a_procesar)[0]
		print codigo_u
		codigo_u = codigo_u.replace("HM_ID:#","")
		print codigo_u
		nro_destino = Usuario.objects.filter(codigo_u=codigo_u)[0]
		print "telefonooooo %s" %nro_destino.telefono
		return nro_destino.telefono
	except Exception,e:
		print e

@csrf_exempt
@api_view(['GET', 'POST'])
def procesar_mensaje_entrante(request):
	print "procesar_mensaje_entrante "
	try:
		if request.method == 'POST':
			print "\t es POST"
			print request.POST

			aList = [
				Buzon_pendientes(
				nombre_persona=i['nombre_persona'],
				numero_telefono=buscar_destinatario(i['contenido_mensaje']),
				contenido_mensaje=i['contenido_mensaje'],
				) for i in request.data['data']
				]

			Buzon_pendientes.objects.bulk_create(aList)
			print "\n\n\n\n>>>>>>>>>>>Agregado Mensaje por enviar<<<<<<<<<<<<\n\n\n"
			return Response(status=status.HTTP_200_OK)
	except Exception,e:
		print e
		return Response(status=status.HTTP_200_OK)
	return Response(status=status.HTTP_404_NOT_FOUND)


