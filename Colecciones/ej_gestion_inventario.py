
print('***Sistema de inventarios***')
n_productos=int(input('Cuantos productos deseas agregar'))
contador=0
inventario=[]

for i in range (n_productos):
    print(f'Proporciona los valores del producto {i+1} :')
    nombre=input('Nombre:')
    precio=float(input('Precio:'))
    cantidad=input('Cantidad:')
    contador+=1

    producto={'id':i,'nombre':nombre,'precio':precio,'cantidad':cantidad}

    inventario.append(producto)
print(inventario)

id_buscar=int(input('Introduce el id del producto que deseas buscar:'))
producto_encontrado=None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado=producto
        break
if producto_encontrado is not None:
   print('Producto encontrado:')
   print(f'''
    Id:{producto_encontrado.get('id')}
    Nombre:{producto_encontrado.get('nombre')}
    Precio:{producto_encontrado.get('precio')}
    Cantidad:{producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con id: {id_buscar} no encontrado')
