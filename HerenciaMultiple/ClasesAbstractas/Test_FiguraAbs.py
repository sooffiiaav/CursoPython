from CuadradoAbs import Cuadrado
from HerenciaMultiple.FigurasGeometricas.FiguraGeometrica import FiguraGeometrica
from HerenciaMultiple.FigurasGeometricas.Rectangulo import Rectangulo

#cuadrado1= Cuadrado(5,'Rojo')

#print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')

#MRO: PARA SABER LA JERARQUÍA DE CLASE QUE SIGUE SEGUN LLAMAMOS AL METODO
#print(Cuadrado.mro())

#No se puede instanciar una clase abstracta:
#figura=FiguraGeometrica()


print('CUADRADO'.center(50,'-'))
cuadrado1=Cuadrado(5,'Azul')
print(cuadrado1)
print(f'Area del cuadrado1:{cuadrado1.calcular_area()}')
print('RECTANGULO'.center(50,'-'))
rectangulo1=Rectangulo(6,5,'Verde')
print(rectangulo1)
print(f'Calculo del area del rectangulo: {rectangulo1.calcular_area()}')

#Si no queremos que se modifiquen los valores, lo que debemos hacer es eliminar los metodos setter