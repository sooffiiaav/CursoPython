'''
Partes: al inicio: expresion de cada uno de los elementos,
segunda parte recorremos lista,
tercera parte (opcional) ponemos una condicion con el if
'''
print('Una lista con el cuadrado de cada numero')
numeros=[1,2,3,4,5]
cuadrados=[x**2 for x in numeros]
print(cuadrados)

print("Lista de numeros pares")
numeros=range(10+1)

pares=[x for x in numeros if x%2 ==0]
print(pares)

print("Lista para saludar a cada nombre")
nombres=['Ana','Miguel','Paola']
saludando=[f'Hola {nombre}' for nombre in nombres ]
print(saludando)

