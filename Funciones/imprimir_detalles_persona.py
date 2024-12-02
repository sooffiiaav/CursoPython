from Funciones.ejemplo_coordenadas import resultado


def detalles_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')


resultado=detalles_persona(nombre='sofia', edad=10, peso=20)
