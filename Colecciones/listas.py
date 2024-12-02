from os import remove

mi_lista=[1,2,3,4,5]
print(f'{mi_lista} -> Lista original')

#Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

#Acceder a los elementos por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')

#Accedemos al ultimo indice de la lista
print(f'Accedemos al ultimo indice de la lista:{mi_lista[-1]}')

#Modificar elementos
mi_lista[1]=10
print(f'Modificamos el valor del indice 1: {mi_lista}')

#Agregar nuevos elementos al final de la lista:
mi_lista.append(6)
print(f'Agregando el numero 6: {mi_lista}')

#Añadir un nuevo elemento en un indice concreto
mi_lista.insert(2,15)#El primer numero es el indice en el que lo queremos agregar
print(f'Se añadio el valor de 15 en el indice 2: {mi_lista}')

#eliminar elementos de una lista
#remove
mi_lista.remove(5) #se elimina el valor 5
print(mi_lista)

#eliminamos por indice
mi_lista.pop(1)
print(mi_lista)

#eliminar indice
del mi_lista[2]
print(mi_lista)

#obtener sublistas
sublista= mi_lista[1:3] #genera una sublista desde el indice 1 al 2 (el 3 no se incluye)
print(sublista)
