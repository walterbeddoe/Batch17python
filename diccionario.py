diccionario= {'nombre':'Walter','edad':'29', 'cursos':['Python','Flask']}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'][0]) #lista con iteracion 

dic = dict( nombre='Juan', apellido='Beddoe', edad=22)
#print(dic)
print("______________________________")

for key,value in diccionario.items():
	print(key + " : " + str(value))

lista_cursos = diccionario['cursos']
lista_cursos.append('Java')
print(lista_cursos)
print(diccionario)

print("______________________________")

#devuelve el numero de elementos que tiene el diccionario
print(len(diccionario))

print("______________________________")

#devuelve una lista con las claves del diccionario
print(diccionario.keys())

print("______________________________")

#devuelve una lista con los valores del diccionario 
print(diccionario.values())

print("______________________________")

#devuelve el valor del elemento con su clave y si no lo encuentra sustituye por uno default
print(diccionario.get("nombree","Juanito"))

print("______________________________")

diccionario['key'] = 'value'
print(diccionario)

print("______________________________")

#elimina un valor del diccionario

diccionario.pop('key')
print(diccionario)


#devuelve la copia de un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de un diccionario a otro , concatenarlos
diccionario.update(dic)
print(diccionario)