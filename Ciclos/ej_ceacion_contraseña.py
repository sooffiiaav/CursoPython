

contraseña=(input('Introduce una contraseña:'))
while len(contraseña)<6:
    print('Contraseña invalida. Debe de tener al menos 6 caracteres')
    contraseña = (input('Introduce otra contraseña:'))

else:
    print('Contraseña valida')
