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
#de la api rest
from rest_framework import routers
from han.han_app import views
#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

router = routers.DefaultRouter()

router.register(r'pendiente', views.Buzon_pendientesSerializerViewSet,'pendiente')
router.register(r'api_enviar', views.api_enviarSerializer,'api_enviar')
router.register(r'enviados', views.Buzon_enviadosSerializerViewSet,'enviados')
router.register(r'usuario_envia', views.Usuario_enviaSerializerViewSet,'usuario_envia')
router.register(r'usuarios', views.UsuarioSerializerViewSet,'usuarios')
router.register(r'usuario_historial_mensaje', views.Usuario_historial_mensaje_SerializerViewSet,'usuario_historial_mensaje')

urlpatterns = patterns('han.han_app.views',
	(r'^api/', include(router.urls)),
	(r'^api_mensajes_listar/(?P<id>[0-9]*)?$','api_mensajes_listar'),
	(r'^api_enviar_mensaje/(?P<id>[0-9]*)?/?(?P<cantidad_sms>[0-9]*)?/?$','api_enviar_mensaje'),
	(r'^api_usuario_envia/?','api_usuario_envia'),
	(r'^api_bulto_mensaje/?','api_bulto_mensaje'),
	(r'procesar_mensaje_entrante/?$','procesar_mensaje_entrante'),
	(r'^actualizar_enviar_mensaje/(?P<id>[0-9]*)?/?$','actualizar_enviar_mensaje'),
	(r'^main/?$','usuario'),
	(r'^archivo/?$','func_subir_archivo'),
	(r'^buzon_entrada/?$','buzon_entrada'),
	(r'^buzon_pendientes/?$','buzon_pendientes'),
	(r'^buzon_enviado/?$','buzon_enviados'),
	(r'^enviar_mensaje/?$','enviar_mensaje'),
	(r'^enviar_mensaje_procesar/(\.*,?)*/?$','enviar_mensaje_procesar'),
	(r'agregar_usuario/?$','agregar_usuario'),
	(r'^editar_usuario/(?P<id_usuario>\w*)/?$','editar_usuario'),
	(r'grupos/?$','grupos'),
	(r'^grupo_usuario/(?P<id_grupo>\d*)/?$','grupo_usuario'),
	(r'operaciones_globales/?$','operaciones_globales'),
	(r'contactanos/?$','contactanos'),
	(r'informacion/?$','informacion'),
	(r'ingreso/?$','ingreso'),
	(r'crear_usuario/?$','crear_usuario'),
	(r'^usuario_envia/?$','usuario_envia'),
	(r'^pagar_usuario/(?P<id_usuario>[0-9]*)?/?$','pagar_usuario'),
	(r'agregar_usuario_envia/?$','agregar_usuario_envia'),
	(r'borrar_bandeja/?$','borrar_bandeja'),
	(r'^ver_historial/(?P<pk>\d*)/?$','ver_historial'),
	(r'^api_ver_historial/(?P<pk>\d*)/?$','api_ver_historial'),
	(r'','usuario'),




)
"""
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
"""