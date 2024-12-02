from POO.Ej_Mundo_Pc.monitor import Monitor
from POO.Ej_Mundo_Pc.raton import Raton
from POO.Ej_Mundo_Pc.teclado import Teclado


class Ordenador:

    contador_ordenadores=0
    def __init__(self,nombre,monitor,teclado,raton):
        Ordenador.contador_ordenadores+=1
        self.id_ordenadores=Ordenador.contador_ordenadores
        self.nombre=nombre
        self.monitor=monitor
        self.teclado=teclado
        self.raton=raton

    def __str__(self):
        return f'''
        Id: {self.id_ordenadores}, Nombre: {self.nombre}, 
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Ratón: {self.raton}'''

if __name__ == '__main__':

    teclado1=Teclado('HP','USB')
    raton1=Raton('HP','USB')
    monitor1=Monitor('HP',27)
    ordenador1=Ordenador('HP',monitor1,teclado1,raton1)
    print(ordenador1)