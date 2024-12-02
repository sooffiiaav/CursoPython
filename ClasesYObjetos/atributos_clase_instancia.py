

class Persona:

#Atributos que se asocian con la clase y no estan dentro de ningun metodo
    atributo_clase =0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia #Se asocian con los obejtos

if __name__ == '__main__':
    print('__Atributos de clase:__')
    print(f'Atributo de Clase: {Persona.atributo_clase}') #Ponemos el nombre de la clase 'Persona.'

    #Modificar Atributo de clase:
    Persona.atributo_clase=10
    print(Persona.atributo_clase)

    #Creamos un objeto person1
    person1 = Persona(15)
    print(f'Atributo de clase desde person1: {person1.atributo_clase}')
    print(f'Atributo de instancia desde person1: {person1.atributo_instancia}')

    person2=Persona(30)
    print(f'Atributo de clase desde person1: {person2.atributo_clase}')
    print(f'Atributo de instancia desde person1: {person2.atributo_instancia}')
