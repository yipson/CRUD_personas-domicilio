from personas.models import Persona, Domicilio
from django.contrib import admin

# Register your models here.

# Registramos los modelos usados para administrarlos desde el panel Admin-Django
admin.site.register(Persona)
admin.site.register(Domicilio)