print ("Contador de impares")
valores = int(input("¿Cuantos valores vas a introducir?"))

if valores < 1:
	print("Imposisble")
else: 
	pares = 0 
	for i in range(1, valores):
		numero = int(input("Escribe el valor")
		if numero % 2 == 0:
			pares += 1
			print("Ha escrito" + str(pares) + "Números pares y " +
				str(valores - pares) + "Números impares")