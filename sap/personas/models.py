from django.db import models

# Create your models here.

# Creamos los modelos que sera los actores principales en el aplicativo


# Domicilio nos define la direccion de residencia que cada usuario
class Domicilio(models.Model):
    # los campos calle, no_calle, pais, seran los mismos de la base de datos en la tabla personas_domicilio
    # se hace excepcion de campo id, django lo administra en caso de necesitarlo
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle}, {self.no_calle}, {self.pais} '


# Persona es el actor principal del sistema
# tiene relacion directa con Domicilio mediante una foreignkey (llave foranea)
class Persona(models.Model):
    # Al igual que Domicilio, los siguientes campos
    # corresponden a los campos de la base de datos de la tabla personas_persona
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # Creamos la relacion con Domicilio mediante una llave foranea
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona {self.id}: {self.nombre}, {self.apellido}, {self.email} '