
#Definimos set vacio
suscriptores=set()

n_suscriptores=int(input('Cuantos suscriptores hay en la lista'))
contador=0

while contador<n_suscriptores:
    correo=input('Introduce un correo para la suscripcion:')
    contador+=1
    suscriptores.add(correo)

for lista in suscriptores:
    print(lista)