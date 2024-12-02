USUARIO= 'sofia'
PASSWORD= '1234'

user=input('Introduce tu usuario:')
contraseña=input('Introduce contraseña:')

if user==USUARIO.strip().lower() and contraseña==PASSWORD:
    print('Autenticacion valida')
else:
    print('Autenticacion invalida')