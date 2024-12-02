



class Animal:

    def hacer_sonido(self):
        print('Hago un sonido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

#Funcion Polimorfica:
def hacer_sonido_animal(animal): #duck typing
    animal.hacer_sonido()


print('Clase Padre Animal:')
animal1=Animal()
hacer_sonido_animal(animal1)
print()
print('Clase Hijo Perro:')
perro1=Perro()
hacer_sonido_animal(perro1)
print()
print('Clase Hija Gato:')
gato1=Gato()
hacer_sonido_animal(gato1)
