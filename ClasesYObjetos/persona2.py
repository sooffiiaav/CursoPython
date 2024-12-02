


class Persona2:

    #Atributo clase
    contador=0

    def __init__(self,nombre,apellido):
        #Incrementamos el valor del atributo de clase
        Persona2.contador +=1
        self.id=Persona2.contador
        self.nombre=nombre
        self.apellido=apellido

    def mostrar_persona(self):
        print(f'''
        Id: {self.id}
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

    @staticmethod
    def get_contador_estatico():
        print('Método estatico')
        return Persona2.contador

    @classmethod
    def get_contador_personas(cls):
        print('Metodo de clase:')
        return cls.contador

if __name__ == '__main__':

    persona1 = Persona2('Miguel','Gomez')
    persona1.mostrar_persona()
    persona2 = Persona2('Sofia','Velardiez')
    persona2.mostrar_persona()

    print(f'Contador de personas: {Persona2.contador}')
    print(f'Contador de personas: {Persona2.get_contador_estatico()}')
    print(f'Contador de personas: {Persona2.get_contador_personas()}')