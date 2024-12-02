
agenda={
    'nombre1':
        {'telefono':682532627,
         'email':'pepito@gmail.com',
         'direccion':'calle ola ola'
         },
    'nombre2':
        {'telefono': 629778305,
         'email': 'alfredo@gmail.com',
         'direccion': 'calle pepesancho'
         },
    'nombre3':
        {'telefono': 68229545,
         'email': 'jose@gmail.com',
         'direccion': 'calle buenas'
         }

}
print(f'-----Lista de contactos:-----\n'
      f'{agenda}')
print()
#Acceder a la informacion:
print(f'''
Info contact2:
Telefono:{agenda['nombre2']['telefono']}
Email:{agenda['nombre2']['email']}
Direccion:{agenda['nombre2']['direccion']}
''')
print()
#Agregar nuevo contacto
agenda['contacto4']={
    'telefono': 625874595,
    'email': 'ana@gmail.com',
    'direccion': 'calle linda'
    }
print(agenda)

#Eliminar un contacto
del agenda['nombre2']
print(agenda)
#agenda.pop('nombre2')

print('\nContactos de la agenda:')
for nombre,detalles in agenda.items():
    print(f'''
    Nombre: {nombre},
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}
''')
