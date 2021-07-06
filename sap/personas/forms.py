from typing import Text
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import EmailInput, TextInput
from personas.models import Persona, Domicilio

# Clases que nos daran la forma de los fomularios en el CRUD(Create - Read - Update - Delete)

class PersonaForm(ModelForm):
    class Meta: 
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }