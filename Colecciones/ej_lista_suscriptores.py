from Colecciones.ej_lista_suscriptores_2 import suscriptores, n_suscriptores

suscriptores=set()
n_suscriptores=int(input('Cuantos suscriptores hay en la lista'))

for _ in range(n_suscriptores-1):
    suscriptores.add(input('Nuevo suscriptor: '))

print(f'Lista de suscriptores incial: {suscriptores}')

#Verificamos si un nuevo suscriptor esta en la lista
nuevo_suscriptor=input('Proporciona el nuevo suscriptor:')
if nuevo_suscriptor in suscriptores:
    print('el nuevo sus ya esta en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print('se ha agregado a la lista')
print(suscriptores)


#eliminamos un suscriptor
suscriptor_eliminar=input('Proporciona el suscriptor a eliminar')
suscriptores.remove(suscriptor_eliminar)
print(suscriptores)

#verificamos la cantidad total de suscriptores
print(f'Cantidad: {len(suscriptores)}')

print('---Lista de Suscriptores---')
for lista in suscriptores:
    print(f'-{lista}')