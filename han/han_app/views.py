# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from han.han_app.models import Document
from han.han_app.models import *
from han.han_app.forms import DocumentForm
from han.han_app.forms import *
from django.template.context_processors import csrf
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
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
	return render_to_response("usuarios.html",{'documento':personas})

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
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Entrada"})

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
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Pendientes"})

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
	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Enviados"})

def enviar_mensaje(request):
	formulario = Form_enviar_mensaje()
	print "aca algooo"
	print request

	return render_to_response("enviar_mensaje.html",{'formulario':formulario,'tipo':"Enviar Mensajes"})

def enviar_mensaje_procesar(request,destinatarios):
	print "procesar"
	form = Form_enviar_mensaje(request.GET)
	
	mensaje = request.GET['mensaje']

	destinatarios = request.GET['destinatarios']

	for d in destinatarios.split(","):
		print d
		try:
			usuario = Usuario.objects.all().filter(telefono=d)[0]
			print usuario
			d = Buzon_pendientes(nombre_persona=usuario.nombre, 
				numero_telefono=usuario.telefono, 
				contenido_mensaje=mensaje, 
				grupo_asociado=usuario.grupo_asociado,
				)
			d.save()
		except Exception,e:
			print e
			d = Buzon_pendientes(nombre_persona="numero no valido", 
			numero_telefono=d, 
			contenido_mensaje=mensaje, 
			grupo_asociado=d,
			)
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

	return render_to_response("buzon.html",{'buzon':personas,'tipo':"Buzon de Mensajes Pendientes"})



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