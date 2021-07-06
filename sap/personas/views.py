from django.shortcuts import get_object_or_404, redirect, render
from django.forms  import modelform_factory
from personas.models import Persona, Domicilio
from personas.forms import PersonaForm, DomicilioForm

# Muestra el detalle de el registro seleccionado, corresponde a la tabla personas_persona
def detallePersona(request, id):
    # Muestra pagina 404 en caso de no encontrar la pagina
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona':persona})

# Formulario que crea nuevo registro persona
def nuevaPersona(request):
    # Validar si existe algun envio en el formulario
    if request.method == 'POST':
        # validar si los campos son validos y guardar en la base de datos
        # al pasar la validacion redirige a la pagina principal (index)
        # de lo contrario carga la pagina de nuevo
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    # se llama por primera vez el formulario o redirige de haber error con los campos
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

# Edita el registro seleccionado de la tabla personas_persona
def editarPersona(request, id):
    # recibe el id del registro, de no existir retorna error 404
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        # Se envia parametro intance para llenar los campos del fomulario con lo campturado por el id
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            # De ser valida la informacion actualiza el registro y retorna a la pagina principal (index)
            # de lo contrario actualiza la pagina
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

# Elimina el registro seleccionado de la tabla personas_persona
def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

# Lista los registros de la tabla personas_domicilio
def domicilios(request):
    no_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.order_by('id','nombre')
    return render(request, 'domicilios/listar.html', {'no_domicilios': no_domicilios, 'domicilios': domicilios})

# Muestra el detalle de el registro seleccionado, corresponde a la tabla personas_detalle
def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio})

# Formulario que crea nuevo registro domicilio
def nuevoDomicilio(request):
    if request.method == 'POST':
        # Se validan los campos, de ser correctos se guarda el registro y nos retorna a el listado de domicilios
        # de lo contrario recarga la pagina
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')
    else:
            formaDomicilio = DomicilioForm()
    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})

# Edita el registro seleccionado de la tabla personas_domicilio
def editarDomicilio(request, id):
    # captura el id del registro, de no existir retorna error 404
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        # Se envia parametro intance para llenar los campos del fomulario con lo campturado por el id
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            # De ser valida la informacion actualiza el registro y retorna al listado de domicilios
            # de lo contrario actualiza la pagina
            formaDomicilio.save()
            return redirect('domicilios')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})

# Elimina registro seleccionado de la tabla personas_domicilio
def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('domicilios')