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



urlpatterns = patterns('han.han_app.views',
	(r'^api/', include(router.urls)),
	(r'^mensajes_list/(?P<id>[0-9]*)?$','mensajes_list'),
	(r'^api_enviar_mensaje/?','api_enviar_mensaje'),
	(r'^api_usuario_envia/?','api_usuario_envia'),
	(r'^actualizar_enviar_mensaje/(?P<id>[0-9]*)?/?$','actualizar_enviar_mensaje'),
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
	(r'^grupo_usuario/(?P<id_grupo>\d*)/?$','grupo_usuario'),

	(r'operaciones_globales/?$','operaciones_globales'),
	(r'contactanos/?$','contactanos'),
	(r'informacion/?$','informacion'),
	(r'ingreso/?$','ingreso'),
	(r'crear_usuario/?$','crear_usuario'),
	(r'^usuario_envia/?$','usuario_envia'),
	(r'^pagar_usuario/(?P<id_usuario>[0-9]*)?/?$','pagar_usuario'),
	(r'agregar_usuario_envia/?$','agregar_usuario_envia'),
	(r'','usuario'),
    (r'api/?$', 'Buzon_pendientesSerializerViewSet'),



)
"""
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
"""