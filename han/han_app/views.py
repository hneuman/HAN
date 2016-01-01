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

from django.template.context_processors import csrf
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.template import RequestContext

from django.apps import apps

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

	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Pendientes"},RequestContext(request, {}))


def agregar_usuario(request):
	c = {}
	c.update(csrf(request))
	print "agregar "
	print "agregar >>> %s"%request

	if request.method == "POST":
		form = Form_usuario(request.POST)
		print "procesar"
		if form.is_valid():
			print " >>>>>>>>>>>>>>>> %s "%request.POST.getlist('metodo')[0]
			if(request.POST.getlist('metodo')[0]=="nuevo"):
				usuario = Usuario(
					nombre=form.cleaned_data['nombre'],
					telefono=form.cleaned_data['telefono'],
					email=form.cleaned_data['email'],
					grupo_asociado=form.cleaned_data['grupo_asociado'],
					)
				aviso="Usuario Agregado Satisfactoriamente"

			else:
				usuario = Usuario.objects.get(pk=int(request.POST.getlist('metodo')[0]))

				usuario.nombre=form.cleaned_data['nombre']
				usuario.telefono=form.cleaned_data['telefono']
				usuario.email=form.cleaned_data['email']
				usuario.grupo_asociado=form.cleaned_data['grupo_asociado']
				aviso="Usuario Modificado Satisfactoriamente"

				
			usuario.save()
		form = Form_usuario()
		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':aviso,'metodo':'nuevo'},RequestContext(request, {}),c)

	else:
		form = Form_usuario()
		print "retornar post"
		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':"Agregar nuevo usuario",'metodo':'nuevo'}, RequestContext(request, {}),c)


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

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
			})


		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Editar Usuario",'aviso':"Editar Usuario",'metodo':int(id_usuario)},RequestContext(request, {}),c)

	except Exception,e:
		print e
		form = Form_usuario()
		print "retornar post"
		return render_to_response("agregar_usuario.html",{'formulario':form,'tipo':"Agregar Usuario",'aviso':"El usuario que intentas modificar, no existe",'metodo':'nuevo'}, RequestContext(request, {}),c)


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
		return render_to_response("grupos.html",{'formulario':form,'tipo':"Agregar Grupo",'aviso':aviso,'metodo':'nuevo','documento':False},RequestContext(request, {}),c)

	else:
		form = Form_grupo()
		grupo = Grupo.objects.all()

		print "retornar post"
		return render_to_response("grupos.html",{'formulario':form,'tipo':"Agregar Grupo",'aviso':"Agregar nuevo Grupo",'metodo':'nuevo','documento':grupo}, RequestContext(request, {}),c)

