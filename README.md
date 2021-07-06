# CRUD SAP MVT Python-Django
CRUD (Create Update Read Delete)\n
SAP  (System Administration Personnel)
MVT  (Model View Template) patron de diseño
Django -  framework backend de Python

Sencillo CURD en python con el framework
Django de Python usando el patron de diseño MVT
y usando como base de datos PostgreSQL

El sistema realiza las acciones de crea, listar, actualizar y borrar
registros de una base de datos en la cual se afectan dos tablas
 1. personas con los campos de:
    -id
    -nombre
    -apellido
    -email
    -domicilio_id
    
2. domicilios con los campos de:
    -id
    -calle
    -no_calle
    -pais

Las tablas tienen entre si una relacion de uno a uno mediante
una foreign key

Dicha base de datos de puede ver en el repositorio con el nombre
de sap_db

El proyecto esta separado por carpetas, de tal manera que cada parte
del cogigo realice especificamente su funcion
