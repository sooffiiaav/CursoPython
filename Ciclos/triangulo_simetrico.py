

filas=int(input('Dime el numero de filas: '))
for fila in range(1,filas+1):
    espacios_blancos=' '*(filas-fila)
    asteriscos='*'*(2*fila-1)
    print(f'{espacios_blancos}{asteriscos}')