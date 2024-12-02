
n_calificaciones=int(input('Cuantas calificaciones van a ser?'))
contador=0
suma=0
array=[]

while contador<n_calificaciones:
    calificacion=int(input('Introduce una calificacion:'))
    contador+=1
    array.append(calificacion)

for notas in array:
    suma+=notas

promedio=suma/n_calificaciones
print(f'El promedio de las notas es: {promedio}')



