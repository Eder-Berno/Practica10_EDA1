#creando un diccionario
elementos = {'hidrogeno': 1, 'helio': 2, 'carbon': 6}

for llave, valor in elementos.items():
    print(llave, " = ", valor)
    
#Obteniendo sólo las llaves
for llave in elementos.keys():
    print(llave)

#obteniendo sólo los valores
for valor in elementos.values():
    print(valor)

#Si se necesita iterar utilizando un índice
for idx, x in enumerate(elementos):
    print("El ídice es: {} y el elemento: {}".format(idx,x))
