#!/usr/bin/python

# Declaramos la clase Persona que contendra propiedades
class Persona:
    cedula = "F-14549805"  # Las propiedades serán datos al azar del objeto persona
    nombre = "Miguel"
    apellido = "Gomez"
    sexo = "M"


example = Persona # Asignamos el objeto a una variable llamada example
print type(example) # Mostramos en pantalla el tipo de dato de la variable example
print dir(example) # Mostramos las propiedades por medio de un diccionario
print example.cedula # Mostramos el dato de la propiedad cedula 
print example.nombre
print example.apellido
print example.sexo

# Mostramos un saludo donde mostramos los datos de las propiedades nombre, apellido y cedula
print "Hola, mucho gusto, mi nombre es " + example.nombre + " " + example.apellido + ", \nmi cedula de identidad es " + example.cedula



