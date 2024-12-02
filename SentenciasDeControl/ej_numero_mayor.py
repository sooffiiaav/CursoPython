

numero1=int(input('Dime un numero:'))
numero2=int(input('Dime un numero:'))

if numero1>numero2:
    print(f'El numero mayor es: {numero1}')
else:
    print(f'El numero mayor es: {numero2}')

resolucion= f'El num mayor es: {numero1}' if numero1>numero2 else f'El num mayor es: {numero2}'
print(f'{resolucion}')
