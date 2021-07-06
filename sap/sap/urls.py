"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona, domicilios, detalleDomicilio, nuevoDomicilio, editarDomicilio, eliminarDomicilio
from webapp.views import bienvenido#, despedida, contacto

# Administracion de las url que debera tomar el sistema
urlpatterns = [
    path('admin/', admin.site.urls),

    # Personas
    path('', bienvenido, name='index'), # Pagina principal, lista los registros de personas_persona
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona),

    # Domicilios
    path('domicilios', domicilios, name='domicilios'), # lista los registros de personas_domicilio
    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('nuevo_domicilio', nuevoDomicilio),
    path('editar_domicilio/<int:id>', editarDomicilio),
    path('eliminar_domicilio/<int:id>', eliminarDomicilio)
]
