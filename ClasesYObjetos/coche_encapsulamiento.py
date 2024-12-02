

class Coche:

    def __init__(self,marca, modelo,color):
        self.marca = marca # Atributo publico, podemos acceder a el sin necesidad de ningun encapsulamiento
        self._modelo = modelo #Atributo protegido, debemos acceder a el mediante los metodos get y set
        self.__color = color #Atributo privado

    def conducir(self):
        print(f''' Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')


if __name__ == '__main__':
    #Creacion de nuestro primer objeto
    coche1= Coche('Toyota', 'Yaris','Azul')
    coche1.conducir()
    #No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2' #Esto no es aconsejable
    coche1.__color = 'Azul 2' #Ignora la modificacion
    coche1.conducir()