print('***Sistema de descuentos***')

productos_descuento=10
cantidad_productos=(int(input('Cuantos productos has comprado')))
tener_registro=input('Estas registrado en la tienda(Si/No)?')

tiene_descuento= (cantidad_productos>= productos_descuento and tener_registro.strip().lower()=='si')
print(f'Tienes acceso al descuento VIP? {tiene_descuento}')


