# Mostrar menú
# Función para mostrar inventario
def mostrar_inventario():
    print('Lista de productos:')
    for producto in inventario:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Proveedor: {producto['proveedor']}")

# Función para agregar producto al inventario
def añadir_producto(nombre, cantidad, proveedor):
    nuevo_producto = {
        'id': len(inventario) + 1,  # Generar un nuevo ID, automáticamente incrementado
        'nombre': nombre,
        'cantidad': int(cantidad),  # Convertir cantidad a int
        'proveedor': proveedor
    }
    inventario.append(nuevo_producto)
    print('Añadido al inventario correctamente')

# Función para buscar un producto por su ID
def buscar_producto(id):
    encontrado = False
    for producto in inventario:
        if producto['id'] == id:
            print(f'Producto encontrado:')
            print(f"\tNombre: {producto['nombre']}")
            print(f"\tCantidad: {producto['cantidad']}")
            print(f"\tProveedor: {producto['proveedor']}")
            encontrado = True
            break
    if not encontrado:
        print('ID inexistente')

# Inventario inicial
inventario = [{
    'id': 1,
    'nombre': 'peras',
    'cantidad': 10,
    'proveedor': 'Palomo'
    },
    {
    'id': 2,
    'nombre': 'manzanas',
    'cantidad': 14,
    'proveedor': 'Golden'
    },
    {
    'id': 3,
    'nombre': 'sandías',
    'cantidad': 4,
    'proveedor': 'Patricio'
    }
]


while True:
    print('''MENU:
    \t1. Mostrar inventario
    \t2. Agregar nuevo producto
    \t3. Buscar producto por ID
    \t4. Salir''')

    opciones = int(input('¿Qué opción escoges? '))

# Ejecutar según la opción seleccionada
    if opciones == 1:
        mostrar_inventario()
        break
    elif opciones == 2:
        nombre = input('Dime el producto que deseas añadir: ')
        cantidad = input('Dime la cantidad de producto que hay: ')
        proveedor = input('Dime el proveedor del producto: ')
        añadir_producto(nombre, cantidad, proveedor)
        break
    elif opciones == 3:
        id_usuario = int(input('Dime el id del producto que quieras: '))
        buscar_producto(id_usuario)
        break
    elif opciones == 4:
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida')
