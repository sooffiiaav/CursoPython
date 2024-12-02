

def sumar(a,b):
    resultado=a+b
    print(f'El resultado es: {resultado}')

def restar(a,b):
    resultado=a-b
    print(f'El resultado es: {resultado}')

def dividir(a,b):
    resultado=a/b
    print(f'El resultado es: {resultado}')

def multiplicar(a,b):
    resultado=a*b
    print(f'El resultado es: {resultado}')



while True:
    print('''MENU:
    1. Sumar
    2. Restar
    3. Dividir
    4. Multiplicar''')

    opcion= int(input('Escoge una opcion:'))

    if opcion==1:
        n1=float(input('Dime un numero:'))
        n2=float(input('Dime un numero:'))
        sumar(n1,n2)
    elif opcion==2:
        n1=float(input('Dime un numero:'))
        n2=float(input('Dime un numero:'))
        restar(n1, n2)
    elif opcion==3:
        n1=float(input('Dime un numero:'))
        n2=float(input('Dime un numero:'))
        dividir(n1, n2)
    elif opcion==4:
        n1=float(input('Dime un numero:'))
        n2=float(input('Dime un numero:'))
        multiplicar(n1, n2)
    break
else:
    print('opcion invalida')
