

productos=[
            ('P001','Camisa',20.00),
           ('P002','Pantalon',30.00),
           ('P003','Sudadera',40.00)
]



#Imprimimos la info de cada producto y calculamos el precio total
precio_total=0

print('Info productos:')
for productos in productos:
    id,descripcion,precio=productos
    print(f'Id: {id}  Descripcion: {descripcion}  Precio: {precio}')
    precio_total+=precio #producto[2] tambien se podria poner
    print(f'El precio final: {precio_total}')