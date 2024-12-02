
mensaje=input('Introduce un mensaje: ')
repeticiones= int(input('Dime cuantas veces quieres que se repita el mensaje: '))

for _ in range(repeticiones): #el guion bajo es en caso de que no usemos la variable i en ningun momento
    #print(f'{i+1}-{mensaje}')
    print(mensaje)