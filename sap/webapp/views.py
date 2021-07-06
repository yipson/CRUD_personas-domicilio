from personas.models import Persona
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Pagina principal
def bienvenido(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all() # retorna todos los objetos de tipo persona que hay en la base de datos
    personas = Persona.objects.order_by('id') # Nos da un ordenamiento ascendente, o descendente si enviamos el parametro -id
    return render(request, 'bienvenido.html', { 'no_personas': no_personas,
                                                'personas': personas
                                            })