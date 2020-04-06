#Ejercicio 1
#Hacer un algoritmo en python 2 que le pida un numero al usuario 8 y que muestre la siguiente salida
#Ingrese un numero => 8
"""
8
9
6
7
2
3
4
5
"""



#!/usr/bin/python

e = input("Ingrese un numero => ") # Pedimos dato al usuario (entero) e => empezar
i = 1 # Creamos una variable i que tendrá la inicialización 1

for i in range(e): # Le indicamos al for que con la variable (i) inicie el conteo en 1 y que entre el rango de la variable e
    print e # Mostramos el dato que el usuario digito (8)
    e += 1  # El primer caso nos dice mostrar el 9 lo cual sumamos 1 al valor de e (8)
    print e # Mostramos el valor de la variable e
    e  -= 3 # En cada iteración aumentamos y disminuimos el valor de e para determinar el valor que nos piden en el orden pedido
    print e
    e += 1
    print e
    e -= 5
    print e
    e += 1
    print e
    e += 1
    print e
    e += 1
    print e
    break  # Hacemos que las iteraciones de detengan
