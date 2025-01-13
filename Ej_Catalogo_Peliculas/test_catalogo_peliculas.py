from Dominio.Pelicula import Pelicula
from Servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
while opcion !=4:
    try:
        print('Opciones')
        print('1. Agregar Película\n')
        print('2. Listar Catalogo\n')
        print("3. Eliminar archivo\n")
        print("4. Salir")
        opcion = int(input('¿Que opción escoges?'))

        if opcion == 1:
            nombre_pelicula = input('Dime el nombre de la pelicula que deseas agregar')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_pelicula()
    except Exception as e:
        print({e})
        opcion = None
else:
    print('Salimos del programa...')

