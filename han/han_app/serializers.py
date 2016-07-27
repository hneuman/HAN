from django.contrib.auth.models import User, Group
from han.han_app.models import *

from rest_framework import serializers
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
 
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class Buzon_pendientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buzon_pendientes
        fields = ('nombre_persona','numero_telefono', 'contenido_mensaje','grupo_asociado')


class api_enviarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buzon_pendientes
        fields = ('numero_telefono',)