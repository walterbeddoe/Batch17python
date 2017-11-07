#!/usr/bin/python
# -*- coding: utf-8 -*-

#googlear cmpuertas logicas
#operador and or

#x = int(input("Ingresa un numero X \n"))
#y = int(input("Ingresa un numero Y \n"))
#
#if x == 3 and y ==3:
#	print("Se cumple AND")
#else:
#	print("No")
#
#if x == 3 or y ==3:
#	print("Se cumple OR")
#else:
#	print("No")

"""x = int(input("Ingresa un numero X \n"))
y = int(input("Ingresa un numero Y \n"))

result = x%y

if result == 0:
	print("Division Exacta")
else:
	print("Division No Exacta")	


x = int(input("Ingresa un numero X \n"))
y = int(input("Ingresa un numero Y \n"))

if x<y:
	print(str (x) + " es menor")

if y>x:
	print(str (y) + " es mayor")

elif y == x:
	print("Son iguales")

x = int(input("Ingresa el año actual \n"))
y = int(input("Ingresa año en que naciste \n"))

result = x - y
print( "Han pasado " + str(result) + " años")

if y>x:
	print ("Faltan " + str(result) + " años")"""

x = int(input("Ingresa un numero X \n"))
y = int(input("Ingresa un numero Y \n"))
z = int(input("Ingresa un numero Z \n"))

if x > y and x > z:
	print("X es mayor")
if y > x and y > z:
	print("Y es mayor")
elif z > x and z > y:
	print("Z es mayor")
else:
	print ("Todos son iguales")