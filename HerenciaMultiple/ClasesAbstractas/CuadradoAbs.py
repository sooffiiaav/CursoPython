from HerenciaMultiple.FigurasGeometricas.Color import Color
from HerenciaMultiple.FigurasGeometricas.FiguraGeometrica import FiguraGeometrica

#la variable de lado solo la utilizamos para inicializar las variable de la clase FiguraGeometrica
class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado) #De esta forma se debe de llamar en herencia multiple
        Color.__init__(self,color)


    def calcular_area(self):
        return self._alto * self._ancho


    def __str__(self):
        return f'''
        {FiguraGeometrica.__str__(self)} #De esta forma cuando se impriman obtendremos los valores del resto
        {Color.__str__(self)}
        '''