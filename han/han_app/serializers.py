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
	usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(),source='usuario.nombre')

	class Meta:
		model = Usuario_historial_mensaje
		fields = ('usuario','tipo_mensaje','numero_telefono','contenido_mensaje','id')


	def create(self, validated_data):
		print "********************",validated_data
		print validated_data['usuario']['nombre'].codigo_u
		#instance = self.objects.create(**validated_data)
		instance = Usuario_historial_mensaje(**validated_data)
		instance = Usuario_historial_mensaje()
		#instance.usuario.add(validated_data['usuario']['nombre'].pk)
		#instance.save()
		#instance = validated_data['usuario']['nombre']

		return instance



class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	historial_usuario = Usuario_historial_mensajeSerializer(many=True)

  	class Meta:
		model = Usuario
		fields = ('nombre','codigo_u','telefono','id','historial_usuario')
 
