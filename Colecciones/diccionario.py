
#Creamos un diccionario de persona con clave y valor

persona={
    'nombre': 'miguel',
    'edad':19,
    'ciudad':'Toledo'

}

print(persona)

print()

#Acceso a los elementos
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}') #menos usado
print(f'Ciudad: {persona['ciudad']}')
print()

#Modificar un valor
persona['edad']=21
print(f'Edad: {persona.get('edad')}')
print()
#Agregar un nuevo elemento:
persona['profesion']='Ingeniero'
print(persona)
print()
#Eliminar elemento
del persona['ciudad']
print(persona)

persona.pop('profesion')
print(persona)
print()

#Iterar elementos de un dic (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

#Obtener valores
for valor in persona.values():
    print(f'-Valor: {valor}')

#Obtener llaves
for llaves in persona.keys():
    print(f'Llave: {llaves}')
