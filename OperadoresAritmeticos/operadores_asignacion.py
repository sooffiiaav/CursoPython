numero= 5
print(f'Valor de numero: {numero}')

numero= 10
print(f'Valor de numero: {numero}')


x, y, z= 10, 9, 7
print(f'x: {x}')
print(f'x: {y}')
print(f'x: {z}')

#Para asignar ek mismo valor a multiples variables:
valor=9
variable1=variable2=valor
print(f'Variable1:{variable1}')


#Intercambio de valores de una variable, sin utilizar variables temporales
x,y= 5, 10
#Aplicando el concepto de asignacion multiples, intercambiamos valores
x,y=y,x
print(f'X:{x}')
print(f'Y:{y}')

#Recibir multiples valores de la entrada del usuario
nombre, apellido=input('Ingresa tu nombre y apellido separados por coma').split(',')

print(f'Nombre: {nombre}')
print(f'Apellido: {apellido}')




