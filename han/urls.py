"""han URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from han.han_app import *

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]
urlpatterns = patterns('han.han_app.views',
	(r'^main/?$','usuario'),
	(r'^archivo/?$','func_subir_archivo'),
	(r'^buzon_entrada/?$','buzon_entrada'),
	(r'^buzon_pendientes/?$','buzon_pendientes'),
	(r'^buzon_enviado/?$','buzon_enviados'),
	(r'^enviar_mensaje/?$','enviar_mensaje'),
	(r'^enviar_mensaje_procesar/(\.*,?)*/?$','enviar_mensaje_procesar'),
	(r'agregar_usuario/?$','agregar_usuario'),
	(r'^editar_usuario/(?P<id_usuario>\d*)/?$','editar_usuario'),
	(r'grupos/?$','grupos'),
	(r'^operaciones_globales/?$','operaciones_globales'),

	(r'','usuario'),




)