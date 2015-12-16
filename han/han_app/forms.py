from django import forms
from han.han_app.models import *
from django.forms import ModelForm

class subirArchivo(forms.Form):
    titulo = forms.CharField(max_length=50)
    archivo = forms.FileField()



class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )


class Form_enviar_mensaje(forms.Form):
	mensaje = forms.CharField(widget = forms.Textarea, label='Mensaje a Enviar' )
	destinatarios = forms.CharField( label = "Destinatarios")

class Form_usuario(forms.Form):
    nombre = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    grupo_asociado = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'placeholder': 'Grupo Asociado'}))
    telefono = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'placeholder': 'Telefono'}))
    email = forms.CharField(max_length=100,widget = forms.TextInput(attrs={'placeholder': 'Correo'}))

