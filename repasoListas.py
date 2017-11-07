#repaso listas
"""
palabras = int(input("¿Cuantas palabras tiene la lista?  \n"))

nombres = []
if palabras > 0:
	for i in range(palabras):
		nombre = input("Ingresa la palabra: \n")
		nombres.append(nombre)
	print(nombres)
else:
	print("No se puede! ")


print("La lista tiene: ", len(nombres), "palabras")
"""
"""
palabras = int(input("¿Cuantas palabras tiene la lista?  \n"))

nombres = []
if palabras > 0:
	for i in range(palabras):
		nombre = input("Ingresa la palabra: \n").upper()
		nombres.append(nombre)
	print("La lista es: ", nombres)
else:
	print("No se puede! ")

busca = input("¿Que palabra quieres buscar?  \n").upper()

if nombres.count(busca) <=1:
	print("La palabra", busca, "aparece", nombres.count(busca), "vez en la lista")
else: 
	print("La palabra", busca, "aparece", nombres.count(busca), "veces en la lista")
"""
"""
palabras = int(input("¿Cuantas palabras tiene la lista?  \n"))

nombres = []
if palabras > 0:
	for i in range(palabras):
		nombre = input("Ingresa la palabra: \n").upper()
		nombres.append(nombre)
	print("La lista es: ", nombres)
else:
	print("No se puede! ")

busca = input("¿Que palabra quieres buscar?  \n").upper()

print(nombres)

primera = nombres.index(busca)

segunda = input("Con que palabra quieres sustituir?").upper()

nombres[primera]=segunda

print("La lista actualizada es: ", nombres)

"""



palabras = int(input("¿Cuantas palabras tiene la lista?  \n"))

nombres = []
if palabras > 0:
	for i in range(palabras):
		nombre = input("Ingresa la palabra: \n").upper()
		nombres.append(nombre)
	print("La lista es: ", nombres)
else:
	print("No se puede! ")

#busca = input("¿Que palabra quieres buscar?  \n").upper()

#print(nombres)

#primera = nombres.index(busca)

segunda = input("Que palabra quieres quitar?").upper()

for i in nombres:
	if i == nombre:
		#primera = nombres.index(busca)
		nombres.remove(segunda)

print("La lista actualizada es: ", nombres)




