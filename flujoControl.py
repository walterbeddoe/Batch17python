# operadores booleanos

x=4
if x == 4: 
	print("Verdad")
else:
	print("Falso")

if x == 2: 
	print("Verdad")
else:
	print("Falso")

x="Rojo"
if x == "Verde": 
	print("Cruza")
else:
	print("Espera")

x="Verde"
if x == "Verde": 
	print("Cruza")
else:
	print("Espera")

x="Verde"
if x == "Verde": 
	print("Cruza")
elif x == "Amarillo":
	print("Corre")
else:
	print("Espera")

x="Amarillo"
if x == "Verde": 
	print("Cruza")
elif x == "Amarillo":
	print("Corre")
else:
	print("Espera")