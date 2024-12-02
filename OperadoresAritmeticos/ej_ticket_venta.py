print('***TICKET DE VENTA***')

precio_leche=float(input('Dime el precio del producto: '))
precio_pan=float(input('Dime el precio del producto: '))
precio_mandarina=float(input('Dime el precio del producto: '))
precio_lechuga=float(input('Dime el precio del producto: '))

preguntar_desc=int(input('Quieres aplicar algun descuento?'))


subtotal=precio_leche+precio_pan+precio_mandarina+precio_lechuga
descuento=subtotal*(preguntar_desc/100)

subtotal_con_descuento=subtotal - descuento


impuesto=subtotal_con_descuento*0.16

precio_final= subtotal_con_descuento + impuesto

resultado=print(f'El precio final de tu compra es de: {precio_final}')

print(f'''
Subtotal: ${subtotal:.2f}
Impuesto (16%): ${impuesto:.2f}
Precio final: ${precio_final:.2f}
''')
