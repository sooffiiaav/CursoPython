from random import randint


salir=False
numero_secreto=randint(1,50)
intentos=0
adivinanza=None
INTENTOS_MAXIMOS=5

while adivinanza!=numero_secreto and intentos<INTENTOS_MAXIMOS:
    adivinanza = int(input('Intenta adivinar el numero'))
    if numero_secreto>adivinanza:
        print('El numero secreto es mayor')

    elif numero_secreto<adivinanza:
        print('El numero secreto es menor')
        intentos+=1
if adivinanza==numero_secreto:
    print('Felicidades! Has averiguado el numero')
else:
    print(f'Tu numero de intentos ha sido: {intentos}')




