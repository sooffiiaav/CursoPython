from email.policy import default

print('***Sistema de Administración de Cuentas***')

salir=False
while not salir:

    print('Menu:\n'
      '\t1. Crear cuenta\n'
      '\t2. Elimina cuenta\n'
      '\t3. Salir')

    opcion=int(input('Escoje una opcion:'))
    if opcion==1:
        print('Creando cuenta...\n')
    elif opcion==2:
        print('Eliminando cuenta...\n')
    elif opcion==3:
        print('Saliendo del programa...\n')
        salir=True
    else:
        print('Opcion invalida')
