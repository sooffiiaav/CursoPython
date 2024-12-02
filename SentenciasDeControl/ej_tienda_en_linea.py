print('***Tienda de descuentos***')

gasto=float(input('Dime cuanto te has gastado en la tienda'))
miembro=input('Eres miembro de la tienda? (Si/No)?')

if (gasto>=1000 and miembro.strip().lower()=='si'):
    print('Tienes un descuento del 10%')
    print(f'Precio inicial de la compra: {gasto}')
    descuento1=gasto*0.10
    print(f'Precio final con descuento:{descuento1}')
elif miembro.strip().lower()=='si':
    print("Descuento del 5%")
    print(f'Precio inicial de la compra: {gasto}')
    descuento2 = gasto * 0.05
    print(f'Precio final con descuento:{descuento2}')
elif not(gasto>1000 and miembro.strip().lower()=='si'):
    print('Descuento del 0%')
    print(f'Precio inicial de la compra: {gasto}')
    print(f'Precio final de la compra: {gasto}')