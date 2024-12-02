from POO.Ej_Mundo_Pc.computadora import Ordenador
from POO.Ej_Mundo_Pc.monitor import Monitor
from POO.Ej_Mundo_Pc.orden import Orden
from POO.Ej_Mundo_Pc.raton import Raton
from POO.Ej_Mundo_Pc.teclado import Teclado



teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
ordenador1 = Ordenador('HP', monitor1, teclado1, raton1)

#Creamos la lista de ordenadores
ordenadores1= [ordenador1]
orden1=Orden(ordenadores1)

teclado2= Teclado('Gamer', 'Bluethooth')
raton2= Raton('Gamer', 'Bluethooth')
monitor2=Monitor('Gamer', 34)
ordenador2=Ordenador('Gamer', monitor2,teclado2,raton2)

orden1.agregar_ordenadores(ordenador2)
print(orden1)

 