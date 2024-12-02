#NO CONSEGUI TERMINARLLO
print('''Menu Snacks:
1. Mostrar snacks
2. Comprar snacks
3. Mostrar ticket
4. Salir''')
opcion=int(input('Que opcion escoges?'))
snacks_disponibles=[
    {
    'id':1,
    'nombre':'patatas',
    'precio': 2.00
    },
    {
    'id': 2,
    'nombre': 'doritos',
    'precio': 1.00
    },
    {
    'id': 3,
    'nombre': 'jumpers',
    'precio': 2.30
    }
]

ticket_final=[{

}]

def mostrar_snacks():
    print('---Snacks Disponibles---')
    for productos in snacks_disponibles:
        print(f' print(f"ID: {snacks_disponibles['id']} -> {snacks_disponibles['nombre']} - ${snacks_disponibles['precio']}")')

def comprar_snack(id):
    encontrado = False
    for producto in snacks_disponibles:
        if producto['id'] == id:
            print(f'Snack agregado:')
            print(f"\tNombre: {snacks_disponibles['nombre']}")
            print(f"\tCantidad: {snacks_disponibles['precio']}")
            encontrado = True
            break
    if not encontrado:
        print('ID inexistente')



if opcion==1:
    mostrar_snacks()
elif opcion==2:
    id=int(input('Que snack quieres comprar? (id)'))
    comprar_snack(id)
elif opcion==4:
    print('Saliendo del programa...')
