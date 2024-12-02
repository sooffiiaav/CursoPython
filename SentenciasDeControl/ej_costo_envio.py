lugar=input('Es envio nacional o internacional')
peso=int(input('Introduce peso del paquete:'))

if lugar.strip().lower()=='nacional':
    precio=peso*10
    print(f'Precio final de envio nacional: {precio}')
elif lugar.strip().lower()=='internacional':
    precio=peso*20
    print(f'Precio final de envio internacional: {precio}')