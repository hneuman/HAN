from django.contrib.auth.models import User, Group
from han.han_app.models import *

from rest_framework import serializers
 

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class Buzon_pendientesSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Buzon_pendientes
		fields = ('nombre_persona','numero_telefono', 'contenido_mensaje','grupo_asociado','id')


class api_enviarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buzon_pendientes
        fields = ('numero_telefono',)

class Buzon_enviadosSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Buzon_enviados
		fields = ('nombre_persona','numero_telefono', 'contenido_mensaje','grupo_asociado','id')


class Usuario_enviaSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Usuario_envia
		fields = ('nombre_usuario_envia','id_usuario_envia','contador','id')


class Usuario_historial_mensajeSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	usuario = serializers.PrimaryKeyRelatedField(
		read_only=True
	)

	class Meta:
		model = Usuario_historial_mensaje
		fields = ('usuario','tipo_mensaje','numero_telefono','contenido_mensaje','id')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	historial_usuario = Usuario_historial_mensajeSerializer(many=True)

  	class Meta:
		model = Usuario
		fields = ('nombre','codigo_u','telefono','id','historial_usuario')
 
