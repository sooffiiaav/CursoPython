

nombre=input('Dime tu nombre:')
dias_estancia=int(input('Cuantos dias te alojaras en el hotel?'))
vistas_mar=input('Deseas vistas al mar (Si/No)?')

PRECIO_VISTAS=190.50
PRECIO_NO_VISTAS=150.50

if vistas_mar.strip().lower()=='si':
    precio=PRECIO_VISTAS*dias_estancia
    print(f'Nombre:{nombre}')
    print(f'Precio final de la estancia:{precio:.2f}')
else:
    precio=PRECIO_NO_VISTAS*dias_estancia
    print(f'Nombre:{nombre}')
    print(f'Precio final de la estancia:{precio:.2f}')
