
#NO FUNCIONA
snacks = [
    {'id': 1, 'nombre': 'patatas', 'precio': 30},
    {'id': 2, 'nombre': 'refresco', 'precio': 50},
    {'id': 3, 'nombre': 'sandwich', 'precio': 120}
]

#Lista de productos comprados (vacio)
productos=[]

def mostrar_snacks():
    print('---Snacks Disponibles---')
    for snack in snacks:
        print(
            f' print(f"ID: {snacks.get('id')} -> {snacks.get('nombre')} - ${snacks.get('precio')}")')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id')==id_buscar:
            return snack
    return None

def comprar_snack():
    id_snack=int(input('Que snack quieres comprar?'))
    snack_encontrado= buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')


def mostrar_ticket():
    pass


while True:
    print('''Menu Snacks:
        1. Mostrar snacks
        2. Comprar snacks
        3. Mostrar ticket
        4. Salir''')
    opcion=int(input('Escoge una opcion:'))

    if opcion==1:
        mostrar_snacks()
    elif opcion==2:
        comprar_snack()
    elif opcion==3:
        mostrar_ticket()
    elif opcion==4:
        print('Saliendo del programa...')
        break
    else:
        print('Opcion invalida')
