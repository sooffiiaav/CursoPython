from Cuadrado import Cuadrado
from HerenciaMultiple.FigurasGeometricas.Rectangulo import Rectangulo

#cuadrado1= Cuadrado(5,'Rojo')

#print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')

#MRO: PARA SABER LA JERARQUÍA DE CLASE QUE SIGUE SEGUN LLAMAMOS AL METODO
#print(Cuadrado.mro())
print('CUADRADO'.center(50,'-'))
cuadrado1=Cuadrado(5,'Azul')
print(cuadrado1)
print(f'Area del cuadrado1:{cuadrado1.calcular_area()}')
print('RECTANGULO'.center(50,'-'))
rectangulo1=Rectangulo(6,5,'Verde')
print(rectangulo1)
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')