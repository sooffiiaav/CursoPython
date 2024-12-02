

class Animal:

    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')


#Programa principal

print('Clase Padre, soy un Animal')
animal1=Animal()
animal1.comer()
animal1.dormir()

print('\nClase hija, soy un Perro')
perro1= Perro()
perro1.dormir()
perro1.comer()
perro1.hacer_sonido()