Ejercicio 1
Hacer un script que le pida un numero al usuario 8 y que muestre la siguiente salida
Ingrese un numero => 8
8
9
6
7
2
3
4
5



#!/usr/bin/python
import time

e = input("Ingrese un numero => ")
t = 1

for t in range(e):
    print e
    e += 1
    print e
    e  -= 3
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
    break
