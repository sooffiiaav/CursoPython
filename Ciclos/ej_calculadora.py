

salir=False
while not salir:
    print('CALCULADORA:\n'
          '\t1. Suma\n'
          '\t2. Resta\n'
          '\t3. Multiplicacion\n'
          '\t4. Division\n')
    opcion=int(input('Que operacion vas a realizar'))

    if opcion==1:
        num1=float(input('Dime un numero:'))
        num2 = float(input('Dime un numero:'))
        resultado=num1+num2
        print(f'Resultado: {resultado}')

    elif opcion==2:
        num1 = float(input('Dime un numero:'))
        num2 = float(input('Dime un numero:'))
        resultado = num1 - num2
        print(f'Resultado: {resultado}')

    elif opcion==3:
        num1 = float(input('Dime un numero:'))
        num2 = float(input('Dime un numero:'))
        resultado = num1 * num2
        print(f'Resultado: {resultado}')

    elif opcion==4:
        num1 = float(input('Dime un numero:'))
        num2 = float(input('Dime un numero:'))
        resultado = num1 / num2
        print(f'Resultado: {resultado}')
    salir=True
else:
    print('Opcion invalida')
