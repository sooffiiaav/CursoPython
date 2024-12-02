

class Coche2:

    def __init__(self,marca, modelo,color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f''' Conduciendo el coche:
           Marca: {self._marca}
           Modelo: {self._modelo}
           Color: {self._color}''')

    #def get_marca(self):
    #   return self._marca

    #def set_marca(self, marca):
    #   self._marca = marca  #Para asignar valor

    @property #Para indicar que es un atributo de nuestra clase
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca  #Para asignar valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo  #Para asignar valor

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color  #Para asignar valor




if __name__ == '__main__':
    # Creacion de nuestro primer objeto
    coche1 = Coche2('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    print(f'Atributos del coche1: {coche1.__dict__}') #Para saer los atributos


    coche1.marca= 'Toyota 3'
    coche1.modelo= 'Yaris 5'
    coche1.color= 'Verde'
    print(f'Atributo de marca del coche 1: {coche1.marca}, modelo: {coche1.modelo}, color: {coche1.color}')

    #Para agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'valor nuevo atributo') #No es recomendable, solo se le  agrega a coche1 pero si queremos crear mas, este no aperece
    coche1.conducir()
    print(coche1.nuevo_atributo)