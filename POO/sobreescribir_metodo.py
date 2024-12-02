
class Animal2:

    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

class Perro2(Animal2):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def dormir(self):
        print('Duermo 15 horas al dia')

    '''Sobreescritura del metodo dormir de la clase Padre:
        En estos casos lo que ocurre es que el metodo que se va
        a mantener cuando creamos un objeto Perro,
        va a ser el metodo sobreecrito
    
    '''
#Programa principal

print('Clase Padre, soy un Animal')
animal2=Animal2()
animal2.comer()
animal2.dormir()

print('\nClase hija, soy un Perro')
perro2= Perro2()
perro2.comer()
perro2.dormir() #Se llama al metodo sobreescrito de la clase hija
perro2.hacer_sonido()