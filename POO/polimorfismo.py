

class Animal:

    def hacer_sonido(self):
        print('Hago un sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')


print('Clase Padre Animal:')
animal1=Animal()
animal1.hacer_sonido()
print()
print('Clase Hijo Perro:')
perro1=Perro()
perro1.hacer_sonido() #Polimorfismo
print()
print('Clase Hija Gato:')
gato1=Gato()
gato1.hacer_sonido() #Polimorfismo
