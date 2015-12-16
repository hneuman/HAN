from django import forms

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

