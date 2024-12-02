
personas=[{
    'nombre':'sofia',
    'apellido':'velardiez',
    'edad':19
    },
    {
    'nombre':'miguel',
    'apellido':'gomez',
    'edad':21
    }]
print(personas)

#Acceder a un diccionario desde una lista
print(f''' Detalle del primer elemento de la lista:
    Nombre: {personas[0]['nombre']}
    Apellido: {personas[0]['apellido']}
    Edad: {personas[0]['edad']}
''')

#Recorrer los elementos de la lista:
print()
for contador,persona in enumerate(personas):
    print(f'{contador+1} - Persona: {persona}')
    print(f'Detalles:\n '
          f'    \nNombre: {persona['nombre']}'
          f'    \nApellido: {persona['apellido']}'
          f'    \nEdad: {persona['edad']}'
        )
