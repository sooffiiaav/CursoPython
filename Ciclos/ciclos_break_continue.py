
#Ejemplo con break
for numero in range(1,10):
    if numero%2==0: #numero par
        print(numero)
        break #Salimos del ciclo inmediatamente

#Ejemplo con continue
for numero in range(1,10):
    if numero%2==1: #numero impar
        continue
    print(numero)
